#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line deadline excuse to entry.txt.

Final line (revised from the draft): tightened to first person, kept the
recursive meeting joke, and sharpened the punch to "rescheduled for never".
"""
import os

LINE = "I scheduled a meeting about the missed deadline, missed that meeting too, so we rescheduled the deadline for never."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
