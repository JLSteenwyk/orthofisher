import sys
import textwrap

from argparse import (
    ArgumentParser,
    RawTextHelpFormatter,
    SUPPRESS,
    RawDescriptionHelpFormatter,
)

from .version import __version__

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

        Version: {__version__}
        Citation: Steenwyk et al.

        orthofisher conducts high-throughput automated sequence similarity searches across proteomes and
        creates fasta files of all significant hits. 
        
        See full documentation including a tutorial usage at the online documentation:
        https://jlsteenwyk.com/orthofisher

        Usage: orthofisher -f <list_of_fasta_files.txt> -m <list_of_hmms.txt> [optional arguments]
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
        -f, --fasta <fasta file list> 
            input file

        -m, --hmm <hmms file list>
            second input file
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
        -e, --evalue <e-value threshold>
            e-value threshold used when conducting sequence similarity searches

        -b, --bitscore <fraction bitscore threshold>
            fraction of a bitscore to be considered similar to top hit


        -------------------------------------
        | Detailed explanation of arguments | 
        -------------------------------------
        -f, --fasta
            A two column tab delimited file that points to the location of fasta files that will be searched using HMMs in the first column. Typically, these are protein fasta files from the entire genome/transcriptome of an organism. The second column of the file specifies the identifier for the organism
        
        -m, --hmm
            A single column file with the location of HMMs that you wish to identify or fish out of a given proteome.

        -e, --evalue
            Specify an e-value threshold to use when conducting sequence similarity searches (default: 0.001). Format can be 1e-3 or 0.001.

        -b, --bitscore
            A fraction threshold to specify the bitscore threshold for sequences to be considered similar. More specifically, if a hit has a bitscore less than the specified fraction, the gene will not be considered sufficiently similar to be considered putatively orthologous. Value must range from 0 to 1 (default: 0.85).
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

    optional.add_argument(
        "-b",
        "--bitscore",
        type=float,
        required=False,
        help=SUPPRESS,
        metavar="bitscore threshold",
    )

    optional.add_argument(
        "-h", "--help", action="help", help=SUPPRESS,
    )

    optional.add_argument(
        "-v", "--version", action="version", version=f"orthofisher {__version__}", help=SUPPRESS,
    )

    return parser