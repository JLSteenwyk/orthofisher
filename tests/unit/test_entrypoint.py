import pytest
import subprocess
import sys


class TestEntrypoint(object):
    def _run(self, args):
        return subprocess.run(
            [sys.executable, "-m", "orthofisher", *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

    @pytest.mark.slow
    def test_help(self):
        res = self._run(["--help"])
        assert res.returncode == 0

    @pytest.mark.slow
    def test_no_args(self):
        res = self._run([])
        assert res.returncode == 0

    @pytest.mark.slow
    def test_run(self):
        res = self._run(["-m", "tests/samples/hmms.txt", "-f", "tests/samples/input.txt", "--verbose-output", "--force"])
        assert res.returncode == 0

    @pytest.mark.slow
    def test_hmm_list_input_error(self):
        res = self._run(["-m", "/file/doesnt/exist", "-f", "tests/samples/input.txt"])
        assert res.returncode != 0
        assert "HMM file does not exist" in res.stdout

    @pytest.mark.slow
    def test_fasta_list_input_error(self):
        res = self._run(["-f", "/file/doesnt/exist", "-m", "tests/samples/hmms.txt"])
        assert res.returncode != 0
        assert "Fasta file list does not exist" in res.stdout
    
    @pytest.mark.slow
    def test_evalue_input_error(self):
        res = self._run(["-f", "tests/samples/input.txt", "-m", "tests/samples/hmms.txt", "-e", "error"])
        assert res.returncode != 0

    @pytest.mark.slow
    def test_bitscore_input_error(self):
        res = self._run(["-f", "tests/samples/input.txt", "-m", "tests/samples/hmms.txt", "-b", "error"])
        assert res.returncode != 0

    @pytest.mark.slow
    def test_cpu_input_error(self):
        res = self._run(["-f", "tests/samples/input.txt", "-m", "tests/samples/hmms.txt", "-c", "asdf"])
        assert res.returncode != 0
