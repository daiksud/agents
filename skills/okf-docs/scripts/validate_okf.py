"""Read-only OKF v0.2 checks, independent of the hosting repository."""
from dataclasses import dataclass
from datetime import date
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
    return issues
