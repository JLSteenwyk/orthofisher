import os
import os.path
import re
import shutil
import subprocess
import sys

def read_input_files(
    fasta_file_list: str,
    hmms_file_list: str
):
    """
    read input files from user args
    """

    ## read input files
    fasta_file_list = [i.strip('\n').split('\t') for i in open(fasta_file_list)]
    hmms_file_list = [i.strip('\n').split('\t') for i in open(hmms_file_list)]

    return fasta_file_list, hmms_file_list

def create_directories(output_dir):
    """
    create directories for outputting files
    """

    ## create output directories
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        print(f"WARNING: {output_dir} output exists. Overwriting directory now...")
        shutil.rmtree(output_dir)
        os.mkdir(output_dir)
    os.mkdir(f'{output_dir}/scog')
    os.mkdir(f'{output_dir}/hmmsearch_output')
    os.mkdir(f'{output_dir}/all_sequences')

def conduct_hmm_search(
    hmmsearch_out: str,
    hmm: str,
    fasta: str,
    evalue: float,
    cpu: int
):
    """
    execute hmm search using subprocess
    """
    # execute hmmsearch
    subprocess.call(
        [
            'hmmsearch', '--noali', 
            '--notextw', '-E', str(evalue),
            '--cpu', str(cpu),
            '--tblout', hmmsearch_out, 
            hmm, fasta
        ], stdout=subprocess.DEVNULL
    )

def check_hmmsearch_output(
    hmmsearch_out: str
):
    
    if not os.path.isfile(hmmsearch_out):
        print("HMM search failed. Check e-value is an appropriate number.")
        sys.exit()

def set_names(
    hmm: str,
    fasta_name: str,
    output_dir: str
):
    """
    set names for output files
    """
    hmm_name = re.sub(r'^.*/', '', hmm)
    singlecopy_name = f'{output_dir}/scog/{hmm_name}.orthofisher'
    all_name = f'{output_dir}/all_sequences/{hmm_name}.orthofisher'
    long_summary_name = f'{output_dir}/long_summary.txt'
    short_summary_name = f'{output_dir}/short_summary.txt'
    hmmsearch_out = f'{output_dir}/hmmsearch_output/{fasta_name}_{hmm_name}'

    return hmm_name, singlecopy_name, all_name, short_summary_name, long_summary_name, hmmsearch_out

def handle_single_copy_writing(
    singlecopy_name: str,
    fasta: str,
    all_name: str,
    long_summary_name: str,
    fasta_name: str,
    hmm_name: str,
    hits,
    record_dict
):
    """
    writes single copy entry to two output fasta files
    and to a long-form log file
    """

    entry_name = ''.join([fasta + ' ' + hits[0]._id + '|' + str(hits[0].evalue) + '|' + str(hits[0].bitscore)])
    record_entry = record_dict[hits[0].id]

    # write single copy orthologous gene file
    with open(singlecopy_name, 'a') as f:
        f.write(">" + entry_name + '\n')
        sequence = [record_entry.seq[i:i+60] for i in range(0, len(record_entry.seq), 60)]
        for seq in sequence:
            if type(seq._data) is str:
                f.write(seq._data + '\n')
            else:
                f.write(seq._data.decode("utf-8") + '\n')

    # write to all gene file
    with open(all_name, 'a') as f:
        f.write(">" + entry_name + '\n')
        sequence = [record_entry.seq[i:i+60] for i in range(0, len(record_entry.seq), 60)]
        for seq in sequence:
            if type(seq._data) is str:
                f.write(seq._data + '\n')
            else:
                f.write(seq._data.decode("utf-8") + '\n')

    # write to long log file
    with open(long_summary_name, 'a') as f:
        f.write('\t'.join([fasta_name, hmm_name, 'single-copy', str(1), hits[0]._id]) + '\n')

def handle_multi_copy_writing(
    fasta: str,
    all_name: str,
    long_summary_name: str,
    fasta_name: str,
    hmm_name: str,
    hits,
    record_dict,
    num_hits: int
):
    """
    writes single copy entry to two output fasta files
    and to a long-form log file
    """

    hit_ids = []
    for idx in range(num_hits):
        hit_ids.append(hits[0]._id)

        entry_name = ''.join([fasta + ' ' + hits[idx]._id + '|' + str(hits[idx].evalue) + '|' + str(hits[idx].bitscore)])
        record_entry = record_dict[hits[idx].id]

        # write to all gene file
        with open(all_name, 'a') as f:
            f.write(">" + entry_name + '\n')
            sequence = [record_entry.seq[i:i+60] for i in range(0, len(record_entry.seq), 60)]
            for seq in sequence:
                if type(seq._data) is str:
                    f.write(seq._data + '\n')
                else:
                    f.write(seq._data.decode("utf-8") + '\n')

        # write to long log file
        with open(long_summary_name, 'a') as f:
            f.write('\t'.join([fasta_name, hmm_name, 'multi-copy', str(num_hits), hits[idx]._id]) + '\n')

def handle_absent_writing(
    long_summary_name: str,
    fasta_name: str,
    hmm_name: str
):
    """
    logs if hmm is absent in the genome
    """
    # write to long log file
    with open(long_summary_name, 'a') as f:
        f.write('\t'.join([fasta_name, hmm_name, 'absent', str(0), 'NA']) + '\n')

def handle_percent_present_summary(
    ortholog_presence_absence_stats: list,
    fasta_name: str,
    short_summary_name: str
):
    """
    write log of percent present single-copy, multi-copy, or absent
    """

    header = [
        'file_name', 'single-copy', 'multi-copy', 'absent',
        'per_single-copy', 'per_multi-copy', 'per_absent'
    ]
    ortholog_presence_absence_per = []

    for val in ortholog_presence_absence_stats:
        ortholog_presence_absence_per.append(round(val/sum(ortholog_presence_absence_stats), 2))

    ortholog_presence_absence_stats = [str(i) for i in ortholog_presence_absence_stats]
    ortholog_presence_absence_per = [str(i) for i in ortholog_presence_absence_per] 

    if os.path.isfile(short_summary_name):
        with open(short_summary_name, 'a') as f:
            f.write(
                '\t'.join(
                    [fasta_name,
                    '\t'.join(ortholog_presence_absence_stats),
                    '\t'.join(ortholog_presence_absence_per)
                    ]
                ) + '\n'
            )
    else:
        with open(short_summary_name, 'a') as f:
            f.write('\t'.join(header) + '\n')

            f.write(
                '\t'.join(
                    [fasta_name,
                    '\t'.join(ortholog_presence_absence_stats),
                    '\t'.join(ortholog_presence_absence_per)
                    ]
                ) + '\n'
            )
