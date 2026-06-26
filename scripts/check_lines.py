#!/usr/bin/env python3
from pathlib import Path
import sys

MAX_LINES = 200
SKIP_DIRS = {
    ".git",
    ".omx",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "target",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def count_lines(path: Path) -> int | None:
    data = path.read_bytes()
    if b"\0" in data:
        return None
    return len(data.splitlines())


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[tuple[str, int]] = []

    for path in sorted(root.rglob("*")):
        if not path.is_file() or should_skip(path.relative_to(root)):
            continue
        lines = count_lines(path)
        if lines is not None and lines > MAX_LINES:
            failures.append((str(path.relative_to(root)), lines))

    if failures:
        for rel, lines in failures:
            print(f"{rel}: {lines} lines > {MAX_LINES}")
        return 1

    print(f"line limit ok: all checked files <= {MAX_LINES} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
