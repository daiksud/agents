"""Synchronize the review skill's runtime files for GitHub Copilot."""
import argparse
from pathlib import Path
import shutil


def synchronize(source, target, *, check=False):
    if not (source / 'SKILL.md').is_file():
        raise ValueError('source SKILL.md is missing')
    expected = {p.relative_to(source): p.read_bytes() for p in source.rglob('*')
                if p.is_file() and p.relative_to(source).parts[0] != 'evals'}
    actual = {p.relative_to(target): p.read_bytes() for p in target.rglob('*')
              if p.is_file()}
    if check:
        for path in sorted(expected.keys() | actual.keys()):
            if expected.get(path) != actual.get(path):
                print(f'review skill copy differs: {path}')
        return expected == actual
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for path, content in expected.items():
        destination = target / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='check without writing')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    return int(not synchronize(root / 'skills/code-review',
                               root / '.github/skills/code-review', check=args.check))


if __name__ == '__main__':
    raise SystemExit(main())
