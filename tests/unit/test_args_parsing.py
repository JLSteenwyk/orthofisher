import pytest
from argparse import Namespace

from orthofisher.args_processing import process_args
from orthofisher.parser import create_parser

@pytest.fixture
def args():
    kwargs = dict(
        fasta="tests/samples/input.txt",
        hmm="tests/samples/hmms.txt",
        evalue=0.001,
        bitscore=0.85,
        output_dir="orthofisher_output",
        cpu=2
    )
    return Namespace(**kwargs)

class TestArgsProcessing(object):
    def test_process_args_fasta_file_dne(self, args):
        args.fasta = "some/file/that/doesnt/exist"
        with pytest.raises(SystemExit):
            process_args(args)

    def test_process_args_hmm_file_dne(self, args):
        args.hmm = "some/file/that/doesnt/exist"
        with pytest.raises(SystemExit):
            process_args(args)

    def test_process_args_default_evalue(self, args):
        args.evalue = None
        res = process_args(args)
        assert res["evalue"] == 0.001

    def test_process_args_custom_evalue(self, args):
        args.evalue = 1e-5
        res = process_args(args)
        assert res["evalue"] == 0.00001

    def test_process_args_default_bitscore(self, args):
        args.bitscore = None
        res = process_args(args)
        assert res["percent_bitscore"] == 0.85

    def test_process_args_custom_bitscore(self, args):
        args.bitscore = 0.5
        res = process_args(args)
        assert res["percent_bitscore"] == 0.5

    def test_process_args_custom_output(self, args):
        args.output_dir = "custom_out"
        res = process_args(args)
        assert res["output_dir"] == "custom_out"

    def test_process_args_custom_cpu(self, args):
        args.cpu = 4
        res = process_args(args)
        assert res["cpu"] == 4

    def test_process_args_expected_keywords(self, args):
        res = process_args(args)
        expected_keys = [
            "fasta_file_list",
            "hmms_file_list",
            "evalue",
            "percent_bitscore",
            "output_dir",
            "cpu"
        ]
        assert sorted(res.keys()) == sorted(expected_keys)

class TestParser(object):
    def test_create_parser(self, args):
        parser = create_parser()
        assert parser.add_help == False
        assert parser.conflict_handler == 'error'
        assert parser.prog == '__main__.py'

        
