import os
import pytest
import subprocess


class TestEntrypoint(object):
    @pytest.mark.slow
    def test_help(self):
        cmd = "orthofisher --help"
        exit_status = os.system(cmd)
        assert exit_status == 0

    @pytest.mark.slow
    def test_no_args(self):
        cmd = "orthofisher"
        exit_status = os.system(cmd)
        assert exit_status == 0

    @pytest.mark.slow
    def test_run(self):
        cmd = "orthofisher -m tests/samples/hmms.txt -f tests/samples/input.txt"
        exit_status = os.system(cmd)
        assert exit_status == 0

    @pytest.mark.slow
    def test_hmm_list_input_error(self):
        cmd = "orthofisher -m /file/doesnt/exist -f tests/samples/input.txt"
        response = subprocess.check_output([cmd], stderr=subprocess.STDOUT, shell=True)
        assert response == b"HMM file does not exist\n"

    @pytest.mark.slow
    def test_fasta_list_input_error(self):
        cmd = "orthofisher -f /file/doesnt/exist -m tests/samples/hmms.txt"
        response = subprocess.check_output([cmd], stderr=subprocess.STDOUT, shell=True)
        assert response == b"Fasta file list does not exist\n"
    
    @pytest.mark.slow
    def test_evalue_input_error(self):
        cmd = "orthofisher -f tests/samples/input.txt -m tests/samples/hmms.txt -e error"
        exit_status = os.system(cmd)
        assert exit_status == 0

    @pytest.mark.slow
    def test_bitscore_input_error(self):
        cmd = "orthofisher -f tests/samples/input.txt -m tests/samples/hmms.txt -b error"
        exit_status = os.system(cmd)
        assert exit_status == 512