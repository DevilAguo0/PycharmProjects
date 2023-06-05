#!/usr/bin/env python3
# sync.py

import time


def count() -> object:
    print("One")
    time.sleep(1)
    print("Two")


def main() -> object:
    for _ in range(3):
        count()


main()
