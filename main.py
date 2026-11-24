"""make.fun entry: Say What Actually Broke (u-po-pu-say-what-actually-broke-a2c153b5).

Writes one single-line error message to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line names the real failure (one missing semicolon took prod down)
and the punchline: the fix was seconds, the postmortem was hours.
"""

import os

LINE = (
    "Prod died on one missing semicolon. "
    "Fix: 4 seconds. "
    "Postmortem: 4 hours, three meetings, and a new rule nobody will read."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
