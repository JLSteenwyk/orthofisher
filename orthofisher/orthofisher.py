#!/usr/bin/env python

import os
import sys
import tempfile
from pathlib import Path

from Bio import SearchIO, SeqIO
from tqdm import tqdm

from .args_processing import process_args
from .exceptions import OrthoFisherError
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
    cpu: int,
    force: bool = False,
    write_all_sequences: bool = False,
    keep_hmmsearch_output: bool = False
):

    # read input files
    fasta_file_list, hmms_file_list = read_input_files(fasta_file_list, hmms_file_list)

    # create directories that will be
    # populated with output files
    create_directories(output_dir, write_all_sequences, keep_hmmsearch_output, force)

    ## loop through fasta files
    for fasta in tqdm(fasta_file_list):
        # ortholog presence absence stats will hold
        # idx0: # single-copy orthologs
        # idx1: # multi-copy orthologs
        # idx2: # absent orthologs
        ortholog_presence_absence_stats = [0, 0, 0]
        record_dict = SeqIO.index(fasta[0], "fasta")
        fasta_name = Path(fasta[0]).name
        name = f"{fasta[1]} " if len(fasta) > 1 else ""

        try:
            ## loop through HMMs
            for hmm in hmms_file_list:
                hmm_name, \
                singlecopy_name, \
                all_name, \
                short_summary_name, \
                long_summary_name, \
                hmmsearch_out = set_names(hmm[0], fasta_name, output_dir)
                created_temp_hmmsearch = False
                if not keep_hmmsearch_output:
                    fd, temp_hmmsearch_out = tempfile.mkstemp(
                        prefix=f"{fasta_name}_{hmm_name}_",
                        suffix=".tbl",
                        dir=output_dir
                    )
                    os.close(fd)
                    hmmsearch_out = temp_hmmsearch_out
                    created_temp_hmmsearch = True
                try:
                    # execute hmmsearch
                    conduct_hmm_search(hmmsearch_out, hmm[0], fasta[0], evalue, cpu)

                    # identify single copy orthologs and write them to separate scog files
                    check_hmmsearch_output(hmmsearch_out)

                    with open(hmmsearch_out, 'r') as hmmsearch_handle:
                        have_written = 0
                        for qresult in SearchIO.parse(hmmsearch_handle, 'hmmer3-tab'):
                            matches = qresult.hits
                            top_score = matches[0].bitscore

                            # remove genes with bitscores less than specified value (-b arg)
                            # of the bitscore value as the top hit in the hmmsearch
                            hits = [hit for hit in matches if hit.bitscore >= (percent_bitscore * top_score)]
                            num_hits = len(hits)

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
                                    record_dict,
                                    write_all_sequences=write_all_sequences
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
                                    num_hits,
                                    write_all_sequences=write_all_sequences
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
                finally:
                    if created_temp_hmmsearch and os.path.exists(hmmsearch_out):
                        os.remove(hmmsearch_out)
        finally:
            record_dict.close()
        
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
    try:
        execute(**process_args(args))
    except OrthoFisherError as exc:
        print(str(exc))
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
