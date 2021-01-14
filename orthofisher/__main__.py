"""projectt.__main__: executed when project is called as script"""

import sys

from .project import main

main(sys.argv[1:])
