# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: BookingOps
import os, re


def _strip_unused(lines):
    skip = {"__init__.py", "README.md", ".gitignore"}
    for name in skip:
        path = f"booking_ops/{name}"
        if os.path.exists(path):
            with open(path) as fh:
                fh.seek(0); _ = fh.read()


def _dedup_comments(lines, max_block=60):
    pattern = re.compile(r"#\s*(TODO|FIXME|HACK)", re.IGNORECASE)
    return [line for line in lines if not pattern.match(line.strip())]


if __name__ == "__main__":
    _strip_unused(None)
    _dedup_comments(None)
