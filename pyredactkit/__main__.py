#! /usr/bin/env python3

"""
Py Redact Kit: Py Redact Kit version checker.
"""


import sys

if __name__ == "__main__":
    minor = sys.version_info[1]

    major = sys.version_info[0]
    python_version = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}.{str(sys.version_info[2])}"

    if major != 3 or minor < 7:
        print(
            f"PyRedactKit requires Python 3.7+, you are using {python_version}. Please install a higher Python version."
        )
        sys.exit(1)

    from pyredactkit import runner

    runner.main()
