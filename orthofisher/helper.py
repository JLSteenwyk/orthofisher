import os
import os.path
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .exceptions import HMMSearchError, OutputDirectoryExistsError

def read_input_files(
    fasta_file_list: str,
    hmms_file_list: str
):
    """
    read input files from user args
    """

    ## read input files
    with open(fasta_file_list, "r") as fasta_handle:
        fasta_file_list = [i.strip('\n').split('\t') for i in fasta_handle]
    with open(hmms_file_list, "r") as hmms_handle:
        hmms_file_list = [i.strip('\n').split('\t') for i in hmms_handle]

    return fasta_file_list, hmms_file_list

def create_directories(
    output_dir,
    write_all_sequences=True,
    keep_hmmsearch_output=True,
    force=False
):
    """
    create directories for outputting files
    """

    ## create output directories
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        if not force:
            raise OutputDirectoryExistsError(
                f"{output_dir} already exists. Use --force to overwrite."
            )
        shutil.rmtree(output_dir)
        os.mkdir(output_dir)
    os.mkdir(f'{output_dir}/scog')
    if keep_hmmsearch_output:
        os.mkdir(f'{output_dir}/hmmsearch_output')
    if write_all_sequences:
        os.mkdir(f'{output_dir}/all_sequences')

def conduct_hmm_search(
    hmmsearch_out: str,
    hmm: str,
    fasta: str,
    evalue: float,
    cpu: int,
    search_tool: str = "hmmsearch"
):
    """
    execute hmm search using subprocess
    """
    # execute hmmsearch
    try:
        subprocess.run(
            [
                search_tool, '--noali',
                '--notextw', '-E', str(evalue),
                '--cpu', str(cpu),
                '--tblout', hmmsearch_out,
                hmm, fasta
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        err = exc.stderr.strip() if exc.stderr else "hmmsearch failed without stderr output."
        raise HMMSearchError(f"{search_tool} failed: {err}")


def determine_search_tool(
    seq_type: str,
    hmm_path: str
) -> str:
    """
    Resolve which HMMER search binary to use for this model.
    """
    if seq_type == "protein":
        return "hmmsearch"
    if seq_type == "nucleotide":
        return "nhmmer"

    hmm_alphabet = get_hmm_alphabet(hmm_path)
    if hmm_alphabet in {"DNA", "RNA"}:
        return "nhmmer"
    return "hmmsearch"


def get_hmm_alphabet(
    hmm_path: str
):
    """
    Read HMM header and return alphabet if present (e.g., AMINO, DNA, RNA).
    """
    with open(hmm_path, "r") as handle:
        for line in handle:
            if line.startswith("ALPH"):
                parts = line.strip().split()
                if len(parts) >= 2:
                    return parts[1].upper()
                return None
            if line.startswith("HMM "):
                break
    return None


@dataclass
class ParsedHit:
    """
    Minimal hit object used to unify parsing across hmmsearch and nhmmer tbl outputs.
    """
    id: str
    bitscore: float
    evalue: float

    @property
    def _id(self):
        return self.id


def parse_nhmmer_tblout(
    tblout_path: str
):
    """
    Parse nhmmer --tblout lines into ParsedHit records.
    """
    hits = []
    with open(tblout_path, "r") as handle:
        for line in handle:
            if not line.strip() or line.startswith("#"):
                continue
            cols = line.strip().split(None, 15)
            if len(cols) < 15:
                continue

            target_name = cols[0]
            try:
                evalue = float(cols[12])
                bitscore = float(cols[13])
            except ValueError:
                continue

            hits.append(ParsedHit(id=target_name, bitscore=bitscore, evalue=evalue))

    return hits

def check_hmmsearch_output(
    hmmsearch_out: str
):
    
    if not os.path.isfile(hmmsearch_out):
        raise HMMSearchError("HMM search failed. Check e-value is an appropriate number.")

def set_names(
    hmm: str,
    fasta_name: str,
    output_dir: str
):
    """
    set names for output files
    """
    hmm_name = Path(hmm).name
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
    record_dict,
    write_all_sequences=True
):
    """
    writes single copy entry to two output fasta files
    and to a long-form log file
    """
    entry_name = ''.join([fasta + hits[0]._id + '|' + str(hits[0].evalue) + '|' + str(hits[0].bitscore)])
    record_entry = record_dict[hits[0].id]
    sequence = _format_sequence_lines(record_entry.seq)

    # write single copy orthologous gene file
    with open(singlecopy_name, 'a') as f:
        f.write(">" + entry_name + '\n' + sequence + '\n')

    # write to all gene file
    if write_all_sequences:
        with open(all_name, 'a') as f:
            f.write(">" + entry_name + '\n' + sequence + '\n')

    # write to long log file
    with open(long_summary_name, 'a') as f:
        f.write(
            '\t'.join(
                [
                    fasta_name,
                    hmm_name,
                    'single-copy',
                    str(1),
                    hits[0]._id,
                    str(hits[0].evalue),
                    str(hits[0].bitscore),
                ]
            ) + '\n'
        )

def handle_multi_copy_writing(
    fasta: str,
    all_name: str,
    long_summary_name: str,
    fasta_name: str,
    hmm_name: str,
    hits,
    record_dict,
    num_hits: int,
    write_all_sequences=True
):
    """
    writes single copy entry to two output fasta files
    and to a long-form log file
    """
    with open(long_summary_name, 'a') as long_out:
        if write_all_sequences:
            with open(all_name, 'a') as all_out:
                for idx in range(num_hits):
                    entry_name = ''.join([fasta + hits[idx]._id + '|' + str(hits[idx].evalue) + '|' + str(hits[idx].bitscore)])
                    record_entry = record_dict[hits[idx].id]
                    sequence = _format_sequence_lines(record_entry.seq)

                    # write to all gene file
                    all_out.write(">" + entry_name + '\n' + sequence + '\n')

                    # write to long log file
                    long_out.write(
                        '\t'.join(
                            [
                                fasta_name,
                                hmm_name,
                                'multi-copy',
                                str(num_hits),
                                hits[idx]._id,
                                str(hits[idx].evalue),
                                str(hits[idx].bitscore),
                            ]
                        ) + '\n'
                    )
        else:
            for idx in range(num_hits):
                long_out.write(
                    '\t'.join(
                        [
                            fasta_name,
                            hmm_name,
                            'multi-copy',
                            str(num_hits),
                            hits[idx]._id,
                            str(hits[idx].evalue),
                            str(hits[idx].bitscore),
                        ]
                    ) + '\n'
                )

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
        f.write('\t'.join([fasta_name, hmm_name, 'absent', str(0), 'NA', 'NA', 'NA']) + '\n')

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
    total = sum(ortholog_presence_absence_stats)
    ortholog_presence_absence_per = [round(val/total, 2) for val in ortholog_presence_absence_stats]

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

def _format_sequence_lines(seq, width=60):
    seq_str = str(seq)
    return '\n'.join(seq_str[i:i+width] for i in range(0, len(seq_str), width))
