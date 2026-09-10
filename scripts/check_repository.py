"""Check source metadata and Markdown with the same entry point locally and in CI."""
import json
from pathlib import Path
import re
import subprocess
import sys

import yaml


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_file(path: Path) -> list[str]:
    errors = []
    try:
        text = path.read_text(encoding='utf-8')
        if path.suffix in {'.yml', '.yaml', '.json'}:
            data = json.loads(text) if path.suffix == '.json' else yaml.safe_load(text)
            if path.name == 'evals.json':
                if not isinstance(data, dict) or data.get('skill_name') != path.parent.parent.name:
                    return ['evals must identify their owning skill']
                cases = data.get('evals')
                if not isinstance(cases, list) or not cases:
                    return ['evals must contain cases']
                ids = set()
                for case in cases:
                    if not isinstance(case, dict):
                        errors.append('each eval must be an object')
                        continue
                    number = case.get('id')
                    if type(number) is not int or number <= 0 or number in ids:
                        errors.append('eval id must be a unique positive integer')
                    else:
                        ids.add(number)
                    for field in ('prompt', 'expected_output'):
                        if not nonempty(case.get(field)):
                            errors.append(f'eval {field} must be a nonempty string')
                    files = case.get('files')
                    if not isinstance(files, list) or any(not nonempty(f) for f in files):
                        errors.append('eval files must be a list of paths')
            return errors
        if path.suffix != '.md':
            return []
        required = path.name == 'SKILL.md' or any(
            part in path.parts for part in ('docs', 'skills', '.apm'))
        if not required:
            return []
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
        if not match:
            return ['missing YAML frontmatter']
        data = yaml.safe_load(match[1])
        if not isinstance(data, dict):
            return ['frontmatter must be a mapping']
        fields = ('name', 'description') if path.name == 'SKILL.md' else ('type', 'title', 'description')
        for field in fields:
            if not nonempty(data.get(field)):
                errors.append(f'{field} must be a nonempty string')
        if path.name == 'SKILL.md':
            name = data.get('name')
            if (not isinstance(name, str) or len(name) > 64
                    or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)
                    or name != path.parent.name):
                errors.append('skill name must be valid and match its directory')
            if isinstance(data.get('description'), str) and len(data['description']) > 1024:
                errors.append('skill description exceeds 1024 characters')
    except (ValueError, yaml.YAMLError, OSError) as error:
        errors.append(str(error))
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    names = subprocess.check_output(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=root
    ).decode().split('\0')
    paths = [root / name for name in sorted(set(names)) if name]
    errors = [f'{path.relative_to(root)}: {error}' for path in paths
              if path.suffix in {'.md', '.json', '.yml', '.yaml'}
              for error in validate_file(path)]
    for error in errors:
        print(error, file=sys.stderr)
    result = subprocess.run(['rumdl', 'check', '--extend-enable', 'MD051,MD057',
                             *[str(p) for p in paths if p.suffix == '.md']], cwd=root)
    return int(bool(errors) or result.returncode != 0)


if __name__ == '__main__':
    sys.exit(main())
