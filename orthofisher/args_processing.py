import logging
import os.path
import sys

logger = logging.getLogger(__name__)

def process_args(args) -> dict:
    """
    Process args from argparser and set defaults
    """
    fasta_file_list = args.fasta
    hmms_file_list = args.hmm

    if not os.path.isfile(fasta_file_list):
        logger.warning("Fasta file list does not exist")
        sys.exit()

    if not os.path.isfile(hmms_file_list):
        logger.warning("HMM file does not exist")
        sys.exit()
    # assign optional arguments
    evalue = args.evalue or 0.001

    return dict(
        fasta_file_list=fasta_file_list,
        hmms_file_list=hmms_file_list,
        evalue=evalue
    )