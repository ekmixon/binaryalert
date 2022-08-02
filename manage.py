#!/usr/bin/env python3
"""Command-line tool for easily managing BinaryAlert."""
import argparse
import os
import sys

from cli import __version__
from cli.manager import Manager


def main() -> None:
    """Main command dispatcher."""
    if sys.version_info.major != 3 or sys.version_info.minor not in {6, 7}:
        print(
            f'ERROR: Python 3.6/7 is required, found Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'
        )

        exit(1)

    manager = Manager()

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'command', choices=sorted(manager.commands), help=manager.help, metavar='command')
    parser.add_argument(
        '--version', action='version', version=f'BinaryAlert v{__version__}'
    )

    args = parser.parse_args()

    os.environ['TF_IN_AUTOMATION'] = '1'
    manager.run(args.command)


if __name__ == '__main__':
    main()
