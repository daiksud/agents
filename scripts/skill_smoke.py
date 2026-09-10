"""Exercise gh skill installation in a temporary directory, never user scope."""
from pathlib import Path
import subprocess
import tempfile

import yaml


def skill_content(path):
    _, header, body = path.read_text(encoding='utf-8').split('---', 2)
    metadata = yaml.safe_load(header)
    provenance = metadata.get('metadata', {})
    provenance.pop('local-path', None)
    if not provenance:
        metadata.pop('metadata', None)
    return metadata, body.lstrip('\n')


def validate_install(source, target):
    errors = []
    skills = sorted((source / 'skills').glob('*/SKILL.md'))
    if not skills:
        return ['no source skills found']
    for skill in skills:
        for original in sorted(skill.parent.rglob('*')):
            if not original.is_file():
                continue
            relative = original.relative_to(source / 'skills')
            installed = target / relative
            if not installed.is_file():
                errors.append(f'missing {relative}')
                continue
            try:
                equal = (skill_content(original) == skill_content(installed)
                         if original.name == 'SKILL.md'
                         else original.read_bytes() == installed.read_bytes())
                if not equal:
                    errors.append(f'content differs: {relative}')
            except (ValueError, yaml.YAMLError, AttributeError) as error:
                errors.append(f'invalid {relative}: {error}')
    return errors


def main():
    source = Path(__file__).resolve().parents[1]
    subprocess.run(['gh', '--version'], check=True)
    listing = subprocess.run(['gh', 'skill', 'install', '.', '--from-local'],
                             cwd=source, check=True, stdin=subprocess.DEVNULL,
                             capture_output=True, text=True)
    print(listing.stdout)
    with tempfile.TemporaryDirectory(prefix='agents-skills-') as directory:
        target = Path(directory)
        command = ['gh', 'skill', 'install', '.', '--from-local', '--all', '--dir', str(target)]
        for extra in ([], ['--force']):
            subprocess.run(command + extra, cwd=source, check=True)
            errors = validate_install(source, target)
            if errors:
                raise SystemExit('\n'.join(errors))
            print('Installed source content verified', flush=True)


if __name__ == '__main__':
    main()
