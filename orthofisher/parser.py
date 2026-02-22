import sys
import textwrap

from argparse import (
    ArgumentParser,
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
            fr"""\
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

        -c, --cpu <cpu workers for multithreading>
            CPU workers for multithreading

        -o, --output_dir <output directory name>
            name of the outputted directory

        --seq-type <protein|nucleotide|auto>
            choose search mode explicitly or infer from HMM alphabet

        --resume
            resume a previous run in the output directory using checkpoint state

        --force
            overwrite an existing output directory

        --verbose-output
            write larger/raw outputs including all_sequences and retained hmmsearch output files


        -------------------------------------
        | Detailed explanation of arguments | 
        -------------------------------------
        -f, --fasta
            A one or two column tab delimited file that points to the location of fasta files that will be searched using HMMs in the first column.
            Typically, these are protein fasta files from the entire genome/transcriptome of an organism. The second column of the file specifies
            the identifier for the organism. If there is no second column, the gene identifier will be used.
        
        -m, --hmm
            A single column file with the location of HMMs that you wish to identify or fish out of a given proteome.

        -e, --evalue
            Specify an e-value threshold to use when conducting sequence similarity searches (default: 0.001). Format can be 1e-3 or 0.001.

        -b, --bitscore
            A fraction threshold to specify the bitscore threshold for sequences to be considered similar. More specifically, if a hit has a
            bitscore less than the specified fraction, the gene will not be considered sufficiently similar to be considered putatively orthologous.
            Value must range from 0 to 1 (default: 0.85).

        -c, --cpu
            Specify the number of parallel CPU workers to use for multithreading (default: 2). This argument is passed to HMMER.

        -o, --output_dir
            Name of the outputted directory with all results from the orthofisher run (default: orthofisher_output).

        --seq-type
            Search mode. Use protein to force hmmsearch, nucleotide to force nhmmer,
            or auto to infer from the HMM ALPH header per model (default: auto).

        --resume
            Resume an existing run in the specified output directory. Completed FASTA/HMM
            pairs from the checkpoint are skipped and remaining pairs are processed.

        --force
            Overwrite an existing output directory. If omitted and the directory exists, orthofisher exits with an error.

        --verbose-output
            By default orthofisher writes slim outputs (scog, long_summary.txt, short_summary.txt).
            Use this flag to also write all_sequences and retain raw hmmsearch tabular output files.
        """
        ),
    )

    optional.add_argument(
        "-e",
        "--evalue",
        type=float,
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
        "-c",
        "--cpu",
        type=int,
        required=False,
        help=SUPPRESS,
        metavar="cpu workers",
    )

    optional.add_argument(
        "-o",
        "--output_dir",
        type=str,
        required=False,
        help=SUPPRESS,
        metavar="output dir",
    )

    optional.add_argument(
        "--seq-type",
        type=str,
        choices=["protein", "nucleotide", "auto"],
        required=False,
        help=SUPPRESS,
        metavar="sequence type",
    )

    optional.add_argument(
        "--resume",
        action="store_true",
        required=False,
        help=SUPPRESS,
    )

    optional.add_argument(
        "--force",
        action="store_true",
        required=False,
        help=SUPPRESS,
    )

    optional.add_argument(
        "--verbose-output",
        action="store_true",
        required=False,
        help=SUPPRESS,
    )

    optional.add_argument(
        "-h", "--help", action="help", help=SUPPRESS,
    )

    optional.add_argument(
        "-v", "--version", action="version", version=f"orthofisher {__version__}", help=SUPPRESS,
    )

    return parser
