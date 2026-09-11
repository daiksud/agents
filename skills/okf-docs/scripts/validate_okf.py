"""Read-only OKF v0.2 checks, independent of the hosting repository."""
from dataclasses import dataclass
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


def validate_file(path, bundle, profile='conformance', *, now=None):
    path, bundle = Path(path), Path(bundle)
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    if not match:
        return [Issue(path, 'frontmatter', 'missing YAML frontmatter', 'specification')]
    try:
        data = yaml.safe_load(match[1])
    except yaml.YAMLError as error:
        return [Issue(path, 'frontmatter', str(error), 'specification')]
    if not isinstance(data, dict):
        return [Issue(path, 'frontmatter', 'must be a mapping', 'specification')]
    issues = []
    if not nonempty(data.get('type')):
        issues.append(Issue(path, 'type', 'must be a nonempty string', 'specification'))
    if profile == 'authoring':
        for field in ('title', 'description'):
            if not nonempty(data.get(field)):
                issues.append(Issue(path, field, 'must be a nonempty string', 'authoring'))
    return issues
