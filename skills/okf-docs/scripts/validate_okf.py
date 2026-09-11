"""Read-only OKF v0.2 checks, independent of the hosting repository."""
import argparse
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
import os
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    yaml = None


if yaml is not None:
    class UniqueKeyLoader(yaml.SafeLoader):
        """Reject duplicate explicit keys before SafeLoader expands YAML merges."""
        # Keep optional datetimes opaque until authoring checks their fields.
        # Copy the resolver table so other PyYAML consumers are unaffected.
        yaml_implicit_resolvers = {
            key: [(tag, pattern) for tag, pattern in resolvers
                  if tag != 'tag:yaml.org,2002:timestamp']
            for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
        }

        def construct_mapping(self, node, deep=False):
            seen = set()
            for key_node, _ in node.value:
                key = ('<<' if key_node.tag == 'tag:yaml.org,2002:merge'
                       else self.construct_object(key_node, deep=deep))
                try:
                    if key in seen:
                        raise yaml.constructor.ConstructorError(
                            'while constructing a mapping', node.start_mark,
                            f'duplicate key: {key}', key_node.start_mark)
                    seen.add(key)
                except TypeError:
                    raise yaml.constructor.ConstructorError(
                        'while constructing a mapping', node.start_mark,
                        'unhashable mapping key', key_node.start_mark) from None
            return super().construct_mapping(node, deep=deep)


@dataclass(frozen=True)
class Issue:
    path: Path
    field: str
    message: str
    rule: str
    severity: str = 'error'


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def structure_lines(body):
    """Mask code, retaining paragraph/list content at its container indentation."""
    fence, list_indents, paragraph = None, [], False
    for raw in body.expandtabs(4).splitlines():
        quoted, quote_depth = raw, 0
        while re.match(r'^ {0,3}>', quoted):
            quoted = re.sub(r'^ {0,3}> ?', '', quoted, count=1)
            quote_depth += 1
        if fence:
            char, length, depth, base = fence
            if quote_depth >= depth:
                content = raw
                for _ in range(depth):
                    content = re.sub(r'^ {0,3}> ?', '', content, count=1)
                if not content.strip() or len(content) - len(content.lstrip()) >= base:
                    marker = re.match(r'^ {0,3}(`{3,}|~{3,})\s*$', content[base:])
                    if marker and marker[1][0] == char and len(marker[1]) >= length:
                        fence = None
                    yield ''
                    continue
            fence = None  # Leaving a list/quote ends its fenced block.
        line = quoted
        indent = len(line) - len(line.lstrip())
        if line.strip():
            while list_indents and indent < list_indents[-1]:
                list_indents.pop()
        base = list_indents[-1] if list_indents else 0
        content = line[base:]
        item = re.match(r'^( {0,3})(?:[-+*]|\d+[.)])( +)', content)
        fence_content = content[item.end():] if item else content
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', fence_content)
        if marker and not (marker[1][0] == '`' and '`' in marker[2]):
            if item:
                base += item.end()
                list_indents.append(base)
            fence = (marker[1][0], len(marker[1]), quote_depth, base)
            paragraph = False
            yield ''
            continue
        if item:
            list_indents.append(base + item.end())
            paragraph = False
        elif not content.strip():
            paragraph = False
        elif content.startswith('    ') and not paragraph:
            yield ''
            continue
        else:
            paragraph = not bool(re.match(r'^ {0,3}(?:#|[-=]{3,}\s*$)', content))
        # Keep quote markers so quoted headings/definitions are not root structure.
        yield ('> ' * quote_depth) + content


def reserved_issues(path, bundle, data, body, has_frontmatter, profile):
    issues = []

    def error(field, message):
        issues.append(Issue(path, field, message, 'specification'))

    content = prose(body, remove_escapes=False)
    lines = content.splitlines()
    definitions = reference_definitions(content)
    for i, line in enumerate(lines):
        if i and re.fullmatch(r' {0,3}(?:=+|-+)\s*', line) and lines[i - 1].strip():
            if not re.match(r'^ {0,3}(?:#|[-+*]\s|\d+[.)]\s)', lines[i - 1]):
                lines[i - 1] = ('# ' if line.lstrip().startswith('=') else '## ') + lines[i - 1].strip()
                lines[i] = ''
    if path.name == 'index.md':
        if profile == 'authoring':
            concept_fields = {'type', 'title', 'description', 'resource', 'tags', 'sources',
                              'generated', 'verified', 'status', 'stale_after', 'usage_window',
                              'runtime', 'parameters', 'computation', 'executor', 'attester'}
            for field in sorted(concept_fields.intersection(data)):
                issues.append(Issue(path, field, 'concept metadata does not belong on an index', 'authoring'))
        if has_frontmatter and (path.parent.resolve() != bundle.resolve()
                                or 'okf_version' not in data or 'type' in data):
            error('frontmatter', 'only a bundle-root index may declare okf_version; not a concept')
        heading, entries = False, 0
        for line in lines:
            if re.match(r'^ {0,3}#{1,6}\s+\S', line):
                if heading and entries == 0:
                    error('body', 'index section must contain linked list entries')
                heading, entries = True, 0
            elif (heading and re.match(r'^ {0,3}(?:[-+*]|\d+[.)])\s+', line)
                  and any(linked_paths(line, definitions=definitions))):
                entries += 1
        if not heading or not entries:
            error('body', 'index requires headings and linked list entries')
    else:
        if has_frontmatter:
            error('frontmatter', 'log has no concept frontmatter')
        dates, entries = [], 0
        for line in lines:
            heading = re.match(r'^ {0,3}##\s+(.+?)(?:\s+#+)?\s*$', line)
            if heading:
                if dates and not entries:
                    error('body', 'each log date needs list entries')
                entries = 0
                try:
                    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', heading[1]):
                        raise ValueError()
                    stamp = date.fromisoformat(heading[1])
                    if dates and stamp >= dates[-1]:
                        error('body', 'log dates must be distinct and newest first')
                    dates.append(stamp)
                except ValueError:
                    error('body', 'log date must be a real YYYY-MM-DD date')
            elif re.match(r'^ {0,3}[-+*]\s+\S', line) and dates:
                entries += 1
        if not dates or not entries:
            error('body', 'log requires date headings and list entries')
    return issues


def timestamp(value):
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str) and re.match(r'^\d{4}-\d{2}-\d{2}[Tt]', value):
        try:
            parsed = datetime.fromisoformat(value.replace('Z', '+00:00').replace('z', '+00:00'))
        except ValueError:
            return None
    else:
        return None
    return parsed if parsed.utcoffset() is not None else None


def prose(body, *, remove_escapes=True):
    text = '\n'.join(structure_lines(body))
    text = re.sub(r'<!--.*?(?:-->|\Z)', '', text, flags=re.S)
    # Matched code spans only; an unmatched backtick remains prose.
    text = re.sub(r'(`+)(?!`)(.+?)(?<!`)\1(?!`)', '', text, flags=re.S)
    return re.sub(r'\\[\\`*{}\[\]()#+.!_>~-]', '', text) if remove_escapes else text


def metadata_issues(path, data, body):
    issues = []

    def error(field, message):
        issues.append(Issue(path, field, message, 'authoring'))

    def string(value, field):
        if not nonempty(value):
            error(field, 'must be a nonempty string')

    def actor(value, field, source=False):
        pattern = r'(?:human:|process:)[^\s]+|[^\s/]+/[^\s/]+'
        # §5.1 and Appendix A also use team: source authors.
        if source:
            pattern += r'|team:[^\s]+'
        if not isinstance(value, str) or not re.fullmatch(pattern, value):
            error(field, 'must identify human:<id>, process:<id>, or producer/version'
                  + (' (team:<id> also accepted for a source)' if source else ''))

    def instant(value, field):
        parsed = timestamp(value)
        if parsed is None:
            error(field, 'must be an ISO 8601 datetime with an explicit UTC offset')
        return parsed

    def window(value, field):
        if not isinstance(value, dict):
            error(field, 'must be a mapping with from and to datetimes')
            return
        start, end = (instant(value.get(key), f'{field}.{key}') for key in ('from', 'to'))
        if start and end and start > end:
            error(field, 'from must not be after to')

    for field in ('title', 'description', 'resource'):
        if field in data:
            string(data[field], field)
    if 'tags' in data and (not isinstance(data['tags'], list)
                           or any(not nonempty(x) for x in data['tags'])):
        error('tags', 'must be a list of nonempty strings')
    if 'status' in data and data['status'] not in ('draft', 'stable', 'deprecated'):
        error('status', 'must be draft, stable, or deprecated')
    if 'stale_after' in data:
        instant(data['stale_after'], 'stale_after')
    if 'usage_window' in data:
        window(data['usage_window'], 'usage_window')
    if 'generated' in data:
        event = data['generated']
        if not isinstance(event, dict):
            error('generated', 'must be a mapping')
        else:
            actor(event.get('by'), 'generated.by')
            if 'at' in event:
                instant(event['at'], 'generated.at')
    if 'verified' in data:
        events = data['verified']
        events = [events] if isinstance(events, dict) else events
        if not isinstance(events, list):
            error('verified', 'must be a mapping or list of mappings')
        else:
            for i, event in enumerate(events):
                field = f'verified[{i}]'
                if not isinstance(event, dict):
                    error(field, 'must be a mapping')
                else:
                    actor(event.get('by'), field + '.by')
                    instant(event.get('at'), field + '.at')
    source_ids = set()
    sources = data.get('sources', [])
    if not isinstance(sources, list):
        error('sources', 'must be a list')
        sources = []
    for i, source in enumerate(sources):
        field = f'sources[{i}]'
        if not isinstance(source, dict):
            error(field, 'must be a mapping')
            continue
        string(source.get('resource'), field + '.resource')
        if 'id' in source:
            key = source['id']
            if not nonempty(key) or re.search(r'[\s\[\]]', key):
                error(field + '.id', 'must be a nonempty footnote label without whitespace or brackets')
            elif key in source_ids:
                error(field + '.id', 'duplicate source ID')
            else:
                source_ids.add(key)
        if 'title' in source:
            string(source['title'], field + '.title')
        if 'author' in source:
            actor(source['author'], field + '.author', source=True)
        if 'last_modified' in source:
            instant(source['last_modified'], field + '.last_modified')
        if 'usage_window' in source:
            window(source['usage_window'], field + '.usage_window')
        if 'usage_count' in source:
            count = source['usage_count']
            if type(count) is not int or count < 0:
                error(field + '.usage_count', 'must be a nonnegative integer')
            if 'usage_window' not in source and 'usage_window' not in data:
                error(field + '.usage_count', 'requires a source or shared usage_window')
    content = prose(body)
    definitions = re.findall(r'^ {0,3}\[\^([^]\s]+)\]:', content, re.M)
    refs = re.findall(r'\[\^([^]\s]+)\](?!:)', content)
    for key in set(definitions):
        if definitions.count(key) > 1:
            error('footnotes.' + key, 'duplicate footnote definition')
    for key in set(refs):
        if key not in definitions:
            error('footnotes.' + key, 'missing footnote definition')
        # Without sources, explanatory Markdown footnotes remain valid.
        elif sources and key not in source_ids:
            error('footnotes.' + key, 'attribution has no matching sources[].id')
    return issues


def state_issues(path, data, now, profile):
    issues = []
    deadline = timestamp(data.get('stale_after'))
    if deadline and now >= deadline:
        issues.append(Issue(path, 'stale_after', 'content is stale (now >= stale_after)',
                            'specification', 'warning'))
    events = data.get('verified', [])
    events = [events] if isinstance(events, dict) else events
    usable_events = [event for event in (events if isinstance(events, list) else []) if isinstance(event, dict)
                     and nonempty(event.get('by')) and timestamp(event.get('at'))]
    if not usable_events:
        issues.append(Issue(path, 'verified', 'unverified content; confirmation is not inferred',
                            'specification', 'warning'))
    generated = data.get('generated')
    changed = timestamp(generated.get('at')) if isinstance(generated, dict) else None
    if profile == 'authoring' and changed and isinstance(events, list):
        times = [timestamp(e.get('at')) for e in events if isinstance(e, dict)]
        if times and all(t and t < changed for t in times):
            issues.append(Issue(path, 'verified', 'recorded checks predate the content change',
                                'authoring', 'warning'))
    return issues


def local_target(value, path, bundle):
    """Return local target or None for external URLs and scope descriptors."""
    if not nonempty(value):
        return None
    parsed = urlsplit(value)
    if parsed.scheme.lower() in ('http', 'https'):
        if not parsed.hostname or re.search(r'\s', parsed.netloc):
            raise ValueError('HTTP(S) URL requires an authority without whitespace')
        # Accessing port validates its syntax without contacting the endpoint.
        _ = parsed.port
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    relative = unquote(parsed.path)
    return (bundle / relative.lstrip('/') if relative.startswith('/')
            else path.parent / relative)


def markdown_destination(text):
    if text.startswith('<'):
        end = text.find('>')
        return text[1:end] if end >= 0 else ''
    result, depth, escaped = [], 0, False
    for char in text:
        if escaped:
            result.append(char)
            escaped = False
            continue
        if char == '\\':
            escaped = True
            continue
        if char == ')' and depth == 0 or char.isspace() and depth == 0:
            break
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        result.append(char)
    return ''.join(result)


def bracket_label(text, start):
    """Read a Markdown label, respecting escaped and nested brackets."""
    depth, result, i = 1, [], start + 1
    while i < len(text):
        char = text[i]
        if char == '\\' and i + 1 < len(text):
            result.append(text[i + 1])
            i += 2
            continue
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            if depth == 0:
                return ''.join(result), i + 1
        result.append(char)
        i += 1
    return None, start + 1


def normalized_label(text):
    return ' '.join(text.split()).casefold()


def reference_definitions(content):
    definitions = {}
    lines = content.splitlines()
    for number, line in enumerate(lines):
        if line.startswith('    '):
            continue
        line = line.lstrip()
        if line.startswith('[') and not line.startswith('[^'):
            label, end = bracket_label(line, 0)
            if label is not None and line[end:end + 1] == ':':
                value = line[end + 1:].lstrip()
                if not value and number + 1 < len(lines):
                    value = lines[number + 1].lstrip()
                target = markdown_destination(value)
                if target:
                    definitions[normalized_label(label)] = target
    return definitions


def linked_paths(body, *, definitions=None):
    content = prose(body, remove_escapes=False)
    if definitions is None:
        definitions = reference_definitions(content)
    i = 0
    while i < len(content):
        if content[i] == '\\':
            i += 2
            continue
        if content[i] != '[' or (i and content[i - 1] == '!'):
            i += 1
            continue
        label, end = bracket_label(content, i)
        i = end
        if label is None or label.startswith('^'):
            continue
        if content[end:end + 1] == '(':
            target = markdown_destination(content[end + 1:].lstrip())
            if target:
                yield target
        elif content[end:end + 1] != ':':
            if content[end:end + 1] == '[':
                reference, i = bracket_label(content, end)
                label = reference or label
            key = normalized_label(label)
            if key in definitions:
                yield definitions[key]


def contract_issues(path, bundle, data, body):
    issues = []

    def error(field, message):
        issues.append(Issue(path, field, message, 'authoring'))

    def link(value, field, descriptor=False, require_file=False):
        if not nonempty(value):
            error(field, 'must be a nonempty path or URL')
            return
        if descriptor and re.search(r'\s', value) and not re.match(r'^(?:\.?\.?/|[A-Za-z][A-Za-z0-9+.-]*:)', value):
            return
        if descriptor and not ('/' in value or re.search(r'\.[a-zA-Z0-9]+(?:#.*)?$', value)):
            return
        try:
            target = local_target(value, path, bundle)
        except ValueError:
            error(field, 'malformed path or URL')
            return
        if target is not None:
            try:
                if not target.resolve().is_relative_to(bundle.resolve()):
                    error(field, f'reference leaves the Bundle: {value}')
                elif not target.exists():
                    error(field, f'local reference does not exist: {value}')
                elif require_file and not target.is_file():
                    error(field, 'computation must reference a regular file')
            except (ValueError, RuntimeError):
                error(field, 'invalid local path')

    for value in linked_paths(body):
        link(value, 'links')
    if 'resource' in data and nonempty(data['resource']):
        link(data['resource'], 'resource')
    sources = data.get('sources', [])
    if isinstance(sources, list):
        for i, source in enumerate(sources):
            if isinstance(source, dict) and nonempty(source.get('resource')):
                link(source['resource'], f'sources[{i}].resource', descriptor=True)
    is_computation = data.get('type') == 'Attested Computation'
    if is_computation or 'runtime' in data:
        if not nonempty(data.get('runtime')):
            error('runtime', 'Attested Computation requires a nonempty runtime')
    if 'parameters' in data:
        params = data['parameters']
        if not isinstance(params, list):
            error('parameters', 'must be a list of declarations')
        else:
            names = set()
            for i, param in enumerate(params):
                field = f'parameters[{i}]'
                if not isinstance(param, dict):
                    error(field, 'must contain name, type, required')
                    continue
                for key in ('name', 'type'):
                    if not nonempty(param.get(key)):
                        error(field + '.' + key, 'must be a nonempty string')
                name = param.get('name')
                if nonempty(name):
                    if name in names:
                        error(field + '.name', 'duplicate declared parameter')
                    names.add(name)
                if type(param.get('required')) is not bool:
                    error(field + '.required', 'must be a boolean')
    for field in ('executor', 'attester'):
        if field not in data:
            continue
        contract = data[field]
        if not isinstance(contract, dict):
            error(field, 'must be a mapping')
        else:
            link(contract.get('resource'), field + '.resource')
            if field == 'executor' and 'receipt' in contract:
                receipt = contract['receipt']
                if not isinstance(receipt, list) or any(not nonempty(x) for x in receipt):
                    error('executor.receipt', 'must be a list of field names, not runtime evidence')
    if 'computation' in data:
        link(data['computation'], 'computation', require_file=True)
    if is_computation:
        # Count real fences under the conventional heading, before its next peer.
        active, level, fence, count, has_content = False, 0, None, 0, False
        comment = False
        for line in body.splitlines():
            if not fence:
                visible = ''
                while line:
                    if comment:
                        end = line.find('-->')
                        if end < 0:
                            line = ''
                        else:
                            line, comment = line[end + 3:], False
                    else:
                        start = line.find('<!--')
                        if start < 0:
                            visible += line
                            break
                        visible += line[:start]
                        line, comment = line[start + 4:], True
                line = visible
            marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
            if fence:
                if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                    fence = None
                elif active and line.strip():
                    has_content = True
                continue
            if marker:
                fence = (marker[1][0], len(marker[1]))
                if active:
                    count += 1
                continue
            heading = re.match(r'^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+)?\s*$', line)
            if heading:
                if heading[2] == 'Computation':
                    active, level = True, len(heading[1])
                elif len(heading[1]) <= level:
                    active = False
        if 'computation' in data and count:
            error('computation', 'choose a file or an inline Computation fence, not both')
        elif 'computation' not in data and (count != 1 or (fence and active) or not has_content):
            error('computation', 'requires one closed, nonempty fenced code block under Computation')
    return issues


def validate_file(path, bundle, profile='conformance', *, now=None):
    path, bundle = Path(path), Path(bundle)
    if yaml is None:
        raise RuntimeError('PyYAML is required; use an existing environment with PyYAML installed')
    if profile not in ('conformance', 'authoring'):
        raise ValueError('unknown profile')
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeError:
        return [Issue(path, 'encoding', 'document must be UTF-8', 'specification')]
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    reserved = path.name in {'index.md', 'log.md'}
    if not match and reserved and not re.match(r'\A---(?:\r?\n|\Z)', text):
        return (reserved_issues(path, bundle, {}, text, False, profile)
                + (contract_issues(path, bundle, {}, text) if profile == 'authoring' else []))
    if not match:
        return [Issue(path, 'frontmatter', 'missing YAML frontmatter', 'specification')]
    try:
        data = yaml.load(match[1], Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError) as error:
        return [Issue(path, 'frontmatter', str(error), 'specification')]
    if not isinstance(data, dict):
        return [Issue(path, 'frontmatter', 'must be a mapping', 'specification')]
    if reserved:
        return (reserved_issues(path, bundle, data, text[match.end():], True, profile)
                + (contract_issues(path, bundle, {}, text[match.end():]) if profile == 'authoring' else []))
    issues = []
    if not nonempty(data.get('type')):
        issues.append(Issue(path, 'type', 'must be a nonempty string', 'specification'))
    if profile == 'authoring':
        for field in ('title', 'description'):
            if not nonempty(data.get(field)):
                issues.append(Issue(path, field, 'must be a nonempty string', 'authoring'))
        issues.extend(metadata_issues(path, data, text[match.end():]))
        issues.extend(contract_issues(path, bundle, data, text[match.end():]))
    issues.extend(state_issues(path, data, now or datetime.now(timezone.utc), profile))
    return issues


def selected_files(bundle, names):
    if not bundle.is_dir():
        raise ValueError('Bundle root must be an existing directory')
    if names:
        paths = []
        for name in names:
            path = Path(name)
            path = path if path.is_absolute() else bundle / path
            if not path.absolute().is_relative_to(bundle) or '..' in path.parts:
                raise ValueError(f'target must be inside the Bundle: {name}')
            relative = path.relative_to(bundle)
            if any((bundle.joinpath(*relative.parts[:i])).is_symlink()
                   for i in range(1, len(relative.parts) + 1)):
                raise ValueError(f'target must not traverse a symbolic link: {name}')
            if not path.is_file() or path.suffix != '.md':
                raise ValueError(f'target must be an existing Markdown file: {name}')
            paths.append(path)
        return sorted(set(paths))

    def walk_error(error):
        raise error

    paths = []
    for directory, directories, files in os.walk(bundle, followlinks=False, onerror=walk_error):
        directories[:] = sorted(d for d in directories if not (Path(directory) / d).is_symlink())
        paths.extend(Path(directory) / name for name in sorted(files)
                     if name.endswith('.md') and not (Path(directory) / name).is_symlink())
    return paths


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path, help='Knowledge Bundle root')
    parser.add_argument('files', nargs='*', help='Markdown files relative to Bundle; default: all')
    parser.add_argument('--profile', choices=('conformance', 'authoring'), default='conformance')
    args = parser.parse_intermixed_args(argv)
    if yaml is None:
        print('environment: PyYAML is required; no packages were installed', file=sys.stderr)
        return 2
    try:
        bundle = Path(os.path.abspath(args.bundle))
        now = datetime.now(timezone.utc)
        paths = selected_files(bundle, args.files)
        issues = [issue for path in paths
                  for issue in validate_file(path, bundle, args.profile, now=now)]
        for issue in issues:
            message = ' '.join(issue.message.splitlines())
            print(f'{issue.path.relative_to(bundle)}: {issue.field}: '
                  f'{issue.severity} [{issue.rule}]: {message}')
        return int(any(issue.severity == 'error' for issue in issues))
    except (OSError, ValueError, RuntimeError) as error:
        print(f'environment: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
