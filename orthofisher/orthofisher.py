#!/usr/bin/env python

import os
import os.path
import re
import subprocess
import sys

from Bio import SearchIO, SeqIO
import numpy as np
from tqdm import tqdm

from .args_processing import process_args
from .parser import create_parser
from .helper import (
    create_directories, read_input_files, 
    conduct_hmm_search, set_names,
    handle_single_copy_writing, handle_multi_copy_writing,
    handle_absent_writing, handle_percent_present_summary,
    check_hmmsearch_output
    )

def execute(
    fasta_file_list: str,
    hmms_file_list: str,
    evalue: float,
    percent_bitscore: float,
    output_dir: str,
    cpu: int
):

    # read input files
    fasta_file_list, hmms_file_list = read_input_files(fasta_file_list, hmms_file_list)

    # create directories that will be
    # populated with output files
    create_directories(output_dir)

    # create empty object for checking 
    # hmmsearches with no hits
    exhausted = object()

    ## loop through fasta files
    for fasta in tqdm(fasta_file_list):
        # ortholog presence absence stats will hold
        # idx0: # single-copy orthologs
        # idx1: # multi-copy orthologs
        # idx2: # absent orthologs
        ortholog_presence_absence_stats = [0, 0, 0]
        record_dict = SeqIO.to_dict(SeqIO.parse(fasta[0], "fasta"))
        fasta_name = re.sub(r'^.*/', '', fasta[0])

        ## loop through HMMs
        for hmm in hmms_file_list:
            hmm_name, \
            singlecopy_name, \
            all_name, \
            short_summary_name, \
            long_summary_name, \
            hmmsearch_out = set_names(hmm[0], fasta_name, output_dir)
            
            # execute hmmsearch
            conduct_hmm_search(hmmsearch_out, hmm[0], fasta[0], evalue, cpu)

            # identify single copy orthologs and write them to separate scog files
            check_hmmsearch_output(hmmsearch_out)

            with open(hmmsearch_out, 'r') as hmmsearch_out:
                have_written = 0
                for qresult in SearchIO.parse(hmmsearch_out, 'hmmer3-tab'):
                    matches = qresult.hits
                    top_score = matches[0].bitscore
                    hits = []

                    # remove genes with bitscores less than specified value (-b arg)
                    # of the bitscore value as the top hit in the hmmsearch
                    for hit in matches:
                        if hit.bitscore >= (percent_bitscore*top_score):
                            hits.append(hit)
                    
                    num_hits = len(hits)

                    # if there is no second column provided,
                    # create a placeholder name that is an empty string
                    try:
                        name = fasta[1] + " "
                    except IndexError:
                        name = ""

                    # if single copy
                    if num_hits == 1:
                        # write to single copy orthologous gene file
                        # write to all gene file
                        # write to long log file
                        handle_single_copy_writing(
                            singlecopy_name,
                            name,
                            all_name,
                            long_summary_name,
                            fasta_name,
                            hmm_name,
                            hits,
                            record_dict
                        )

                        # add to counter
                        ortholog_presence_absence_stats[0]+=1
                        have_written+=1

                    # if multi-copy
                    elif num_hits > 1:
                        handle_multi_copy_writing(
                            name,
                            all_name,
                            long_summary_name,
                            fasta_name,
                            hmm_name,
                            hits,
                            record_dict,
                            num_hits
                        )
                        
                        # add to counter
                        ortholog_presence_absence_stats[1]+=1
                        have_written+=1
                    
                # if absent
                if have_written == 0:
                    handle_absent_writing(
                        long_summary_name,
                        fasta_name,
                        hmm_name
                    )

                    # add to counter
                    ortholog_presence_absence_stats[2]+=1
        
        handle_percent_present_summary(
            ortholog_presence_absence_stats,
            fasta_name,
            short_summary_name
        )

def main(argv=None):
    """
    Function that parses and collects arguments              
    """
    # parse and assign arguments
    parser = create_parser()
    args = parser.parse_args()

    # pass to master execute function
    execute(**process_args(args))

if __name__ == "__main__":
    main(sys.argv[1:])
