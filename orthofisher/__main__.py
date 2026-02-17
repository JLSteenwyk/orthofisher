"""Executable module entrypoint for `python -m orthofisher`."""

import sys

from .orthofisher import main


main(sys.argv[1:])
