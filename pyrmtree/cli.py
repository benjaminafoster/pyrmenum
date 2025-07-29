"""This module provides the Pyrmenum CLI."""

import argparse
import pathlib
import sys

from . import __version__
from .pyrmtree import DirectoryTree

def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(root_dir)
    tree.generate()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="pyrmenum",
        description=" Pyrmenum (pronounced 'perm-enum'), a filesystem permissions enumerator",
        epilog="Thanks for using Pyrmenum!",
    )
    parser.version = f"Pyrmenum v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Scan a directory tree starting at this ROOT_DIR",
    )
    return parser.parse_args()