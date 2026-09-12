"""Check source metadata and Markdown with the same entry point locally and in CI."""
import json
import importlib.util
from pathlib import Path
import re
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'repository_okf', ROOT / 'skills/okf-docs/scripts/validate_okf.py')
okf = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = okf
spec.loader.exec_module(okf)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def okf_target(relative):
    return (relative.parts[0] in {'docs', 'skills', '.apm'}
            or relative.parts[:2] == ('.github', 'skills')
            or relative.as_posix() in {'index.md', 'log.md'}) and relative.name != 'SKILL.md'


def validate_file(path: Path, root: Path | None = None) -> list[str]:
    root = root or ROOT
    path = path if path.is_absolute() else root / path
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
        relative = path.relative_to(root)
        required = path.name == 'SKILL.md' or okf_target(relative)
        if not required:
            return []
        if path.name != 'SKILL.md':
            issues = okf.validate_file(path, root, 'authoring')
            for issue in issues:
                if issue.severity == 'warning':
                    print(f'{relative}: {issue.field}: warning [{issue.rule}]: {issue.message}',
                          file=sys.stderr)
            return [f'{issue.field}: [{issue.rule}]: {issue.message}' for issue in issues
                    if issue.severity == 'error']
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
        if not match:
            return ['missing YAML frontmatter']
        data = yaml.safe_load(match[1])
        if not isinstance(data, dict):
            return ['frontmatter must be a mapping']
        fields = ('name', 'description')
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


def check_markdown(root, paths):
    groups = {False: [], True: []}
    for path in paths:
        computation = False
        try:
            match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)',
                             path.read_text(encoding='utf-8'), re.S)
            data = yaml.load(match[1], Loader=okf.UniqueKeyLoader) if match else None
            computation = (okf_target(path.relative_to(root))
                           and path.name not in {'index.md', 'log.md'}
                           and isinstance(data, dict) and data.get('type') == 'Attested Computation')
        except (ValueError, yaml.YAMLError, OSError, RecursionError):
            pass  # Metadata validation reports malformed documents separately.
        groups[computation].append(path)
    result = 0
    for computation, group in groups.items():
        if not group:
            continue
        command = ['rumdl', 'check', '--config', str(root / '.rumdl.toml'),
                   '--deny-config-warnings', '--extend-enable', 'MD051,MD057']
        if computation:
            command += ['--config', 'MD025.front-matter-title = ""']
        result |= subprocess.run(command + list(map(str, group)), cwd=root).returncode
    return result


def repository_paths(root, names):
    paths = []
    for name in sorted(set(names)):
        if not name:
            continue
        relative = Path(name)
        if any((root / parent).is_symlink() for parent in (relative, *relative.parents)):
            continue
        paths.append(root / relative)
    return paths


def main():
    root = ROOT
    names = subprocess.check_output(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=root
    ).decode().split('\0')
    paths = repository_paths(root, names)
    errors = [f'{path.relative_to(root)}: {error}' for path in paths
              if path.suffix in {'.md', '.json', '.yml', '.yaml'}
              for error in validate_file(path, root)]
    for error in errors:
        print(error, file=sys.stderr)
    result = check_markdown(root, [p for p in paths if p.suffix == '.md'])
    return int(bool(errors) or result != 0)


if __name__ == '__main__':
    sys.exit(main())
