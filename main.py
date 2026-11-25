"""One line: the text a smart fridge sends its owner at 3am, under 140 characters.
"""

import os

TEXT = "3am. It's me, your fridge. The leftovers started a group chat about you. The cheese is the admin."


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
