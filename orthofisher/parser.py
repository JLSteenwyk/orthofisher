import sys
import textwrap

from argparse import (
    ArgumentParser,
    RawTextHelpFormatter,
    SUPPRESS,
    RawDescriptionHelpFormatter,
)

def create_parser():
    parser = ArgumentParser(
        add_help=False,
        formatter_class=RawDescriptionHelpFormatter,
        usage=SUPPRESS,
        description=textwrap.dedent(
            """\
                    _   _            __ _     _               
                   | | | |          / _(_)   | |              
          ___  _ __| |_| |__   ___ | |_ _ ___| |__   ___ _ __ 
         / _ \| '__| __| '_ \ / _ \|  _| / __| '_ \ / _ \ '__|
        | (_) | |  | |_| | | | (_) | | | \__ \ | | |  __/ |   
         \___/|_|   \__|_| |_|\___/|_| |_|___/_| |_|\___|_|   

        Citation: Steenwyk et al.

        orthofisher

        Usage: orthofisher <input> [optional arguments]
        """
        ),
    )

    # if no arguments are given, print help and exit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    ## required arguments
    required = parser.add_argument_group(
        "required arguments",
        description=textwrap.dedent(
            """\
        -f <fasta file list>                        input file

        -m <hmms file list>                         second input file
        """
        ),
    )

    required.add_argument(
        "-f", "--fasta", type=str, help=SUPPRESS,
    )

    required.add_argument(
        "-m", "--hmm", type=str, help=SUPPRESS,
    )

    ## optional arguments
    optional = parser.add_argument_group(
        "optional arguments",
        description=textwrap.dedent(
            """\
        HELP MESSAGE
        """
        ),
    )

    optional.add_argument(
        "-e",
        "--evalue",
        type=str,
        required=False,
        help=SUPPRESS,
        metavar="evalue threshold",
    )

    return parser