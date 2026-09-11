"""Read-only OKF v0.2 checks, independent of the hosting repository."""
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
import re

import yaml


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
    """Ignore fenced/indented examples before recognizing document structure."""
    fence = None
    for line in body.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            yield ''
        elif marker and not (marker[1][0] == '`' and '`' in marker[2]):
            fence = (marker[1][0], len(marker[1]))
            yield ''
        elif line.startswith(('    ', '\t')):
            yield ''
        else:
            yield line


def reserved_issues(path, bundle, data, body, has_frontmatter):
    issues = []

    def error(field, message):
        issues.append(Issue(path, field, message, 'specification'))

    lines = list(structure_lines(body))
    if path.name == 'index.md':
        if has_frontmatter and (path.parent.resolve() != bundle.resolve()
                                or 'okf_version' not in data or 'type' in data):
            error('frontmatter', 'only a bundle-root index may declare okf_version; not a concept')
        heading, entries = False, 0
        for line in lines:
            if re.match(r'^ {0,3}#{1,6}\s+\S', line):
                if heading and entries == 0:
                    error('body', 'index section must contain linked list entries')
                heading, entries = True, 0
            elif re.match(r'^ {0,3}[-+*]\s+\[[^]]+\](?:\([^)]+\)|\[[^]]*\])', line) and heading:
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


def prose(body):
    text = '\n'.join(structure_lines(body))
    # Matched code spans only; an unmatched backtick remains prose.
    text = re.sub(r'(`+)(?!`)(.+?)(?<!`)\1(?!`)', '', text, flags=re.S)
    return re.sub(r'\\[\\`*{}\[\]()#+.!_>~-]', '', text)


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


def state_issues(path, data, now):
    issues = []
    deadline = timestamp(data.get('stale_after'))
    if deadline and now >= deadline:
        issues.append(Issue(path, 'stale_after', 'content is stale (now >= stale_after)',
                            'specification', 'warning'))
    events = data.get('verified', [])
    events = [events] if isinstance(events, dict) else events
    if not events:
        issues.append(Issue(path, 'verified', 'unverified content; confirmation is not inferred',
                            'specification', 'warning'))
    generated = data.get('generated')
    changed = timestamp(generated.get('at')) if isinstance(generated, dict) else None
    if changed and isinstance(events, list):
        times = [timestamp(e.get('at')) for e in events if isinstance(e, dict)]
        if times and all(t and t < changed for t in times):
            issues.append(Issue(path, 'verified', 'recorded checks predate the content change',
                                'authoring', 'warning'))
    return issues


def validate_file(path, bundle, profile='conformance', *, now=None):
    path, bundle = Path(path), Path(bundle)
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    reserved = path.name in {'index.md', 'log.md'}
    if not match and reserved and not text.startswith('---\n'):
        return reserved_issues(path, bundle, {}, text, False)
    if not match:
        return [Issue(path, 'frontmatter', 'missing YAML frontmatter', 'specification')]
    try:
        data = yaml.safe_load(match[1])
    except yaml.YAMLError as error:
        return [Issue(path, 'frontmatter', str(error), 'specification')]
    if not isinstance(data, dict):
        return [Issue(path, 'frontmatter', 'must be a mapping', 'specification')]
    if reserved:
        return reserved_issues(path, bundle, data, text[match.end():], True)
    issues = []
    if not nonempty(data.get('type')):
        issues.append(Issue(path, 'type', 'must be a nonempty string', 'specification'))
    if profile == 'authoring':
        for field in ('title', 'description'):
            if not nonempty(data.get(field)):
                issues.append(Issue(path, field, 'must be a nonempty string', 'authoring'))
        issues.extend(metadata_issues(path, data, text[match.end():]))
    issues.extend(state_issues(path, data, now or datetime.now(timezone.utc)))
    return issues
