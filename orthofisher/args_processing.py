import os.path

from .exceptions import InputValidationError

def process_args(args) -> dict:
    """
    Process args from argparser and set defaults
    """
    fasta_file_list = args.fasta
    hmms_file_list = args.hmm

    if not os.path.isfile(fasta_file_list):
        raise InputValidationError("Fasta file list does not exist")

    if not os.path.isfile(hmms_file_list):
        raise InputValidationError("HMM file does not exist")

    
    # assign optional arguments
    evalue = args.evalue if args.evalue is not None else 0.001

    percent_bitscore = args.bitscore if args.bitscore is not None else 0.85
    
    output_dir = args.output_dir or "orthofisher_output"

    cpu = args.cpu if args.cpu is not None else 2
    seq_type = args.seq_type if args.seq_type is not None else "auto"
    resume = args.resume or False
    force = args.force or False
    verbose_output = args.verbose_output or False

    if evalue <= 0:
        raise InputValidationError("e-value must be greater than 0")

    if percent_bitscore < 0 or percent_bitscore > 1:
        raise InputValidationError("bitscore must range from 0 to 1")

    if cpu < 1:
        raise InputValidationError("cpu must be an integer greater than 0")
    if resume and force:
        raise InputValidationError("--resume and --force cannot be used together")

    write_all_sequences = verbose_output
    keep_hmmsearch_output = verbose_output

    return dict(
        fasta_file_list=fasta_file_list,
        hmms_file_list=hmms_file_list,
        evalue=evalue,
        percent_bitscore=percent_bitscore,
        output_dir=output_dir,
        cpu=cpu,
        seq_type=seq_type,
        resume=resume,
        force=force,
        write_all_sequences=write_all_sequences,
        keep_hmmsearch_output=keep_hmmsearch_output
    )
