import os
from pathlib import Path

import pytest
from mock import patch

from orthofisher.orthofisher import execute

here = Path(__file__)


@pytest.mark.integration
class TestIntegration(object):
    def _run_execute(
        self,
        fasta_file_list,
        hmms_file_list,
        evalue=0.001,
        percent_bitscore=0.85,
        output_dir="orthofisher_output",
        cpu=2,
        seq_type="auto",
        resume=False,
        force=True,
        write_all_sequences=True,
        keep_hmmsearch_output=True,
    ):
        execute(
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
            keep_hmmsearch_output=keep_hmmsearch_output,
        )

    def _read_text(self, path):
        with open(path, "r") as handle:
            return handle.read()

    def _assert_common_outputs(
        self,
        output_dir,
        expected_dir,
        all_sequence_files,
        scog_files,
        expect_all_sequences=True,
        expect_hmmsearch_output=True,
    ):
        assert os.path.isdir(output_dir)
        assert os.path.isdir(f"{output_dir}/scog")
        assert os.path.isdir(f"{output_dir}/all_sequences") is expect_all_sequences
        assert os.path.isdir(f"{output_dir}/hmmsearch_output") is expect_hmmsearch_output

        assert self._read_text(f"{expected_dir}/long_summary.txt") == self._read_text(
            f"{output_dir}/long_summary.txt"
        )
        assert self._read_text(f"{expected_dir}/short_summary.txt") == self._read_text(
            f"{output_dir}/short_summary.txt"
        )

        for name in all_sequence_files:
            assert self._read_text(f"{expected_dir}/all_sequences/{name}") == self._read_text(
                f"{output_dir}/all_sequences/{name}"
            )

        for name in scog_files:
            assert self._read_text(f"{expected_dir}/scog/{name}") == self._read_text(
                f"{output_dir}/scog/{name}"
            )

    @patch("builtins.print")
    def test_integration(self, mocked_print):
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            output_dir="orthofisher_output",
            cpu=2,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir="orthofisher_output",
            expected_dir=f"{here.parent}/expected/default_params",
            all_sequence_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            scog_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    @patch("builtins.print")
    def test_integration_str_decode(self, mocked_print):
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/str_decode_fastas.txt",
            hmms_file_list=f"{here.parent.parent}/samples/str_decode_hmms.txt",
            output_dir="orthofisher_output",
            cpu=2,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir="orthofisher_output",
            expected_dir=f"{here.parent}/expected/default_str_decode_testing",
            all_sequence_files=[
                "42at3041.hmm.orthofisher",
                "45at3041.hmm.orthofisher",
                "52at3041.hmm.orthofisher",
            ],
            scog_files=[
                "42at3041.hmm.orthofisher",
                "45at3041.hmm.orthofisher",
                "52at3041.hmm.orthofisher",
            ],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    def test_integration_custom_evalue(self):
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            evalue=1e-25,
            output_dir="orthofisher_output",
            cpu=2,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir="orthofisher_output",
            expected_dir=f"{here.parent}/expected/custom_evalue_param",
            all_sequence_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            scog_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    def test_integration_custom_bitscore(self):
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            percent_bitscore=0.2,
            output_dir="orthofisher_output",
            cpu=2,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir="orthofisher_output",
            expected_dir=f"{here.parent}/expected/custom_bitscore_param",
            all_sequence_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            scog_files=["718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    @patch("builtins.print")
    def test_integration_custom_output_name(self, mocked_print):
        output_dir = "orthofisher_custom_output"
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            output_dir=output_dir,
            cpu=2,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir=output_dir,
            expected_dir=f"{here.parent}/expected/default_params",
            all_sequence_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            scog_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    @patch("builtins.print")
    def test_integration_custom_cpu(self, mocked_print):
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            output_dir="orthofisher_output",
            cpu=4,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir="orthofisher_output",
            expected_dir=f"{here.parent}/expected/default_params",
            all_sequence_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            scog_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    @patch("builtins.print")
    def test_integration_no_second_column_in_input(self, mocked_print):
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input_no_second_column.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            output_dir="orthofisher_output",
            cpu=2,
            force=True,
            write_all_sequences=True,
            keep_hmmsearch_output=True,
        )

        self._assert_common_outputs(
            output_dir="orthofisher_output",
            expected_dir=f"{here.parent}/expected/default_params_no_second_column_in_fasta_file_paths_file",
            all_sequence_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            scog_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=True,
            expect_hmmsearch_output=True,
        )

    @patch("builtins.print")
    def test_integration_slim_output(self, mocked_print):
        output_dir = "orthofisher_output_slim"
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmms.txt",
            output_dir=output_dir,
            cpu=2,
            force=True,
            write_all_sequences=False,
            keep_hmmsearch_output=False,
        )

        self._assert_common_outputs(
            output_dir=output_dir,
            expected_dir=f"{here.parent}/expected/default_params",
            all_sequence_files=[],
            scog_files=["1001705at2759.hmm.orthofisher", "718307-1.fa.mafft.hmm.orthofisher"],
            expect_all_sequences=False,
            expect_hmmsearch_output=False,
        )

    def test_integration_auto_mode_uses_nhmmer_for_nucleotide_hmms(self):
        output_dir = "orthofisher_output_nucl_auto"
        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input_nucl.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmm_nucl.txt",
            output_dir=output_dir,
            seq_type="auto",
            cpu=2,
            force=True,
            write_all_sequences=False,
            keep_hmmsearch_output=True,
        )

        hmm_out_dir = f"{output_dir}/hmmsearch_output"
        assert os.path.isdir(hmm_out_dir)

        out_files = [
            name for name in os.listdir(hmm_out_dir)
            if os.path.isfile(os.path.join(hmm_out_dir, name))
        ]
        assert len(out_files) > 0

        for out_file in out_files:
            out_path = os.path.join(hmm_out_dir, out_file)
            assert "# Program:         nhmmer" in self._read_text(out_path)

    def test_integration_resume_mode(self, tmp_path):
        output_resume = tmp_path / "resume_run"
        output_fresh = tmp_path / "fresh_run"
        hmms_subset = tmp_path / "hmms_subset.txt"
        hmms_subset.write_text(f"{here.parent.parent}/samples/bena.fa.mafft.hmm\n")

        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input_nucl.txt",
            hmms_file_list=str(hmms_subset),
            output_dir=str(output_resume),
            seq_type="auto",
            cpu=2,
            force=True,
            resume=False,
            write_all_sequences=False,
            keep_hmmsearch_output=False,
        )

        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input_nucl.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmm_nucl.txt",
            output_dir=str(output_resume),
            seq_type="auto",
            cpu=2,
            force=False,
            resume=True,
            write_all_sequences=False,
            keep_hmmsearch_output=False,
        )

        self._run_execute(
            fasta_file_list=f"{here.parent.parent}/samples/input_nucl.txt",
            hmms_file_list=f"{here.parent.parent}/samples/hmm_nucl.txt",
            output_dir=str(output_fresh),
            seq_type="auto",
            cpu=2,
            force=True,
            resume=False,
            write_all_sequences=False,
            keep_hmmsearch_output=False,
        )

        resume_short = self._read_text(f"{output_resume}/short_summary.txt")
        fresh_short = self._read_text(f"{output_fresh}/short_summary.txt")
        assert resume_short == fresh_short

        resume_long = self._read_text(f"{output_resume}/long_summary.txt").strip().splitlines()
        fresh_long = self._read_text(f"{output_fresh}/long_summary.txt").strip().splitlines()
        assert sorted(resume_long) == sorted(fresh_long)
