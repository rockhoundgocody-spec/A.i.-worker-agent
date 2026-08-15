#!/usr/bin/env python3
"""Validate the root catalog and each book summary's entry points."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "README.md"
CATALOG_LINK = re.compile(r"^\s*[*-]\s+\[[^]]+\]\(([^)]+/index\.md)\)\s*$")


def main() -> int:
    errors: list[str] = []
    targets: list[str] = []

    for line_number, line in enumerate(CATALOG.read_text(encoding="utf-8").splitlines(), 1):
        match = CATALOG_LINK.match(line)
        if not match:
            continue
        target = match.group(1)
        targets.append(target)
        if not (ROOT / target).is_file():
            errors.append(f"README.md:{line_number}: missing target: {target}")

    duplicates = sorted({target for target in targets if targets.count(target) > 1})
    for target in duplicates:
        errors.append(f"README.md: duplicate catalog target: {target}")

    summary_targets = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.glob("*/index.md")
        if path.is_file()
    }
    catalog_targets = set(targets)
    for target in sorted(summary_targets - catalog_targets):
        errors.append(f"README.md: summary is not listed: {target}")
    for target in sorted(catalog_targets - summary_targets):
        errors.append(f"README.md: target is not a summary: {target}")

    for target in sorted(summary_targets):
        readme = (ROOT / target).parent / "README.md"
        if not readme.is_symlink():
            errors.append(f"{readme.relative_to(ROOT)}: expected a symbolic link")
        elif readme.readlink() != Path("index.md"):
            errors.append(
                f"{readme.relative_to(ROOT)}: expected link to index.md, "
                f"found {readme.readlink()}"
            )

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Catalog validation passed for {len(summary_targets)} summaries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
