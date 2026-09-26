"""Exercise gh skill installation in a temporary directory, never user scope."""
from pathlib import Path
import io
import subprocess
import tarfile
import tempfile

import yaml

# Keep the pre-rename package even when the healthy APM recovery baseline advances.
SKILL_MIGRATION_BASELINE = '6e09d5166a8f49aa3a71edc102446d92a59e939d'


def skill_content(path):
    _, header, body = path.read_text(encoding='utf-8').split('---', 2)
    metadata = yaml.safe_load(header)
    provenance = metadata.get('metadata', {})
    provenance.pop('local-path', None)
    if not provenance:
        metadata.pop('metadata', None)
    return metadata, body.lstrip('\n')


def validate_install(source, target, previous_source=None):
    errors = []
    skills = sorted((source / 'skills').glob('*/SKILL.md'))
    if not skills:
        return ['no source skills found']
    if previous_source is not None:
        previous_names = {p.parent.name for p in (previous_source / 'skills').glob('*/SKILL.md')}
        retired_names = previous_names - {p.parent.name for p in skills}
        for name in sorted(retired_names):
            if (target / name).exists():
                errors.append(f'retired package skill remains: {name}')
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


def verify_upgrade(source, root):
    """Exercise the documented retirement step only inside the smoke's temporary root."""
    previous, target, backup = root / 'previous-source', root / 'upgraded', root / 'retired-backup'
    baseline = SKILL_MIGRATION_BASELINE
    archive = subprocess.check_output(['git', 'archive', baseline], cwd=source)
    with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
        bundle.extractall(previous, filter='data')
    command = ['gh', 'skill', 'install', str(previous), '--from-local', '--all', '--dir', str(target)]
    subprocess.run(command, check=True, stdin=subprocess.DEVNULL)
    errors = validate_install(previous, target)
    if errors:
        raise RuntimeError('\n'.join(errors))

    def content(directory):
        return {p.relative_to(directory): p.read_bytes() for p in directory.rglob('*') if p.is_file()}

    previous_names = {p.parent.name for p in (previous / 'skills').glob('*/SKILL.md')}
    current_names = {p.parent.name for p in (source / 'skills').glob('*/SKILL.md')}
    retired_names = previous_names - current_names
    for name in ('bdd-tdd', 'task-workflow', 'okf-docs'):
        if name not in retired_names:
            raise RuntimeError(f'migration fixture does not retire {name}: {baseline}')
    retired = {name: content(target / name) for name in retired_names}
    unrelated = target / 'unrelated-fixture/SKILL.md'
    unrelated.parent.mkdir()
    unrelated.write_text('---\nname: unrelated-fixture\ndescription: Preserve other owners.\n---\n')
    unrelated_content = unrelated.read_bytes()
    command[3] = str(source)
    subprocess.run(command + ['--force'], check=True, stdin=subprocess.DEVNULL)
    errors = validate_install(source, target)
    if errors:
        raise RuntimeError('\n'.join(errors))
    backup.mkdir()
    moved = []
    for name, original in retired.items():
        installed = target / name
        if not installed.is_dir():
            raise RuntimeError(f'retired skill missing before backup: {name}')
        if content(installed) != original:
            raise RuntimeError(f'retired skill changed before backup: {name}')
        installed.rename(backup / name)
        if content(backup / name) != original:
            raise RuntimeError(f'retired skill backup differs: {name}')
        moved.append(name)
    errors = validate_install(source, target, previous_source=previous)
    if errors or unrelated.read_bytes() != unrelated_content:
        raise RuntimeError('\n'.join(errors) or 'unrelated skill changed')
    print(f'Upgrade from {baseline} verified; retired skills outside discovery: {sorted(moved)}',
          flush=True)


def main():
    source = Path(__file__).resolve().parents[1]
    subprocess.run(['gh', '--version'], check=True)
    with tempfile.TemporaryDirectory(prefix='agents-skills-') as directory:
        root = Path(directory)
        target = root / 'clean-installed'
        command = ['gh', 'skill', 'install', '.', '--from-local', '--dir', str(target)]
        listing = subprocess.run(command, cwd=source, check=True, stdin=subprocess.DEVNULL,
                                 capture_output=True, text=True)
        print(listing.stdout)
        command.append('--all')
        for extra in ([], ['--force']):
            subprocess.run(command + extra, cwd=source, check=True, stdin=subprocess.DEVNULL)
            errors = validate_install(source, target)
            if errors:
                raise SystemExit('\n'.join(errors))
            print('Installed source content verified', flush=True)
        verify_upgrade(source, root)


if __name__ == '__main__':
    main()
