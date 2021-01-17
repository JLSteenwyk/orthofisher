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

    def test_process_args_expected_keywords(self, args):
        res = process_args(args)
        expected_keys = [
            "fasta_file_list",
            "hmms_file_list",
            "evalue",
        ]
        assert sorted(res.keys()) == sorted(expected_keys)

class TestParser(object):
    def test_create_parser(self, args):
        parser = create_parser()
        assert parser.add_help == False
        assert parser.conflict_handler == 'error'
        assert parser.prog == '__main__.py'

        
