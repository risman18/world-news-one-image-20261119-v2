#!/usr/bin/env python3
"""THE WORLD TODAY — Thursday, 19 November 2026 (v2).

Stdlib only. Copies the pre-rendered entry.png (built at build time by
compose.py) to /output/entry.png. No network, no clock, no randomness —
two runs produce byte-identical output.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
