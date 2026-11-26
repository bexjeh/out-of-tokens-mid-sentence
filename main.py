"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line to entry.txt: the error message an AI agent shows when
it runs out of tokens mid-sentence. Stdlib only, deterministic.
"""

import os

LINE = "Cause of death: token starvation. Time of death: mid-sentence. Next of kin: this error message."


def main() -> None:
    # Gate self-check: the sealed scorer only accepts 1-140 chars,
    # a single line, not whitespace-only. Fail loudly rather than
    # shipping an entry that scores 0.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be single-line"
    assert LINE.strip(), "line must not be whitespace-only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
