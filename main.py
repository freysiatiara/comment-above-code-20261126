"""Write the one-line entry for The Comment Above the Code to the output file.

The entry is a single comment line (no trailing newline) written UTF-8 to
/entry.txt by default, or to the path resolved from ENTRY_OUTPUT,
OUTPUT_DIR, or MAKEFUN_OUTPUT_DIR.
"""

import os

LINE = "# This function only works because the bug in billing cancels the bug in auth; fix either and both break."


def resolve_output_path():
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit("entry.txt does not match LINE after write")


if __name__ == "__main__":
    main()
