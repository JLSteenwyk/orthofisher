import os
import pytest
from pathlib import Path

from mock import patch, call

from orthofisher.orthofisher import execute

here = Path(__file__)


@pytest.mark.integration
class TestIntegration(object):
    @patch("builtins.print")
    def test_integration(self, mocked_print):
        """
        test integration
        """

        fasta_file_list = f"{here.parent.parent}/samples/input.txt"
        hmms_file_list = f"{here.parent.parent}/samples/hmms.txt"
        kwargs = dict(
            fasta_file_list=fasta_file_list,
            hmms_file_list=hmms_file_list,
            evalue=0.001,
        )
        execute(**kwargs)
        
        # read in expected files
        long_summary_expected = f"{here.parent}/expected/default_params/long_summary.txt"
        short_summary_expected = f"{here.parent}/expected/default_params/short_summary.txt"
        orthofisher_1001705at2759_expected = f"{here.parent}/expected/default_params/all_sequences/1001705at2759.hmm.orthofisher"
        orthofisher_718307_expected = f"{here.parent}/expected/default_params/all_sequences/718307-1.fa.mafft.hmm.orthofisher"
        scog_1001705at2759_expected = f"{here.parent}/expected/default_params/scog/1001705at2759.hmm.orthofisher"
        scog_718307_expected = f"{here.parent}/expected/default_params/scog/718307-1.fa.mafft.hmm.orthofisher"

        with open(long_summary_expected, "r") as expected:
            expected_long_summary_content = expected.read()
        with open(short_summary_expected, "r") as expected:
            expected_short_summary_content = expected.read()
        with open(orthofisher_1001705at2759_expected, "r") as expected:
            orthofisher_1001705at2759_expected_content = expected.read()
        with open(orthofisher_718307_expected, "r") as expected:
            orthofisher_718307_expected_content = expected.read()
        with open(scog_1001705at2759_expected, "r") as expected:
            scog_1001705at2759_expected_content = expected.read()
        with open(scog_718307_expected, "r") as expected:
            scog_718307_expected_content = expected.read()


        long_summary_created = f"orthofisher_output/long_summary.txt"
        short_summary_created = f"orthofisher_output/short_summary.txt"
        orthofisher_1001705at2759_created = f"orthofisher_output/all_sequences/1001705at2759.hmm.orthofisher"
        orthofisher_718307_created = f"orthofisher_output/all_sequences/718307-1.fa.mafft.hmm.orthofisher"
        scog_1001705at2759_created = f"orthofisher_output/scog/1001705at2759.hmm.orthofisher"
        scog_718307_created = f"orthofisher_output/scog/718307-1.fa.mafft.hmm.orthofisher"

        with open(long_summary_created, "r") as out_file:
            output_long_summary_content = out_file.read()
        with open(short_summary_created, "r") as out_file:
            output_short_summary_content = out_file.read()
        with open(orthofisher_1001705at2759_created, "r") as out_file:
            orthofisher_1001705at2759_created_content = out_file.read()
        with open(orthofisher_718307_created, "r") as out_file:
            orthofisher_718307_created_content = out_file.read()
        with open(scog_1001705at2759_created, "r") as expected:
            scog_1001705at2759_created_content = expected.read()
        with open(scog_718307_created, "r") as expected:
            scog_718307_created_content = expected.read()


        assert os.path.isdir('orthofisher_output')
        assert os.path.isdir('orthofisher_output/all_sequences')
        assert os.path.isdir('orthofisher_output/hmmsearch_output')
        assert os.path.isdir('orthofisher_output/scog')
        assert expected_long_summary_content == output_long_summary_content
        assert expected_short_summary_content == output_short_summary_content
        assert orthofisher_1001705at2759_expected_content == orthofisher_1001705at2759_created_content
        assert orthofisher_718307_expected_content == orthofisher_718307_created_content
        assert scog_1001705at2759_expected_content == scog_1001705at2759_created_content
        assert scog_718307_expected_content == scog_718307_created_content

    def test_integration_custom_evalue(self):
        """
        test integration
        """

        fasta_file_list = f"{here.parent.parent}/samples/input.txt"
        hmms_file_list = f"{here.parent.parent}/samples/hmms.txt"
        evalue = '1e-25'
        kwargs = dict(
            fasta_file_list=fasta_file_list,
            hmms_file_list=hmms_file_list,
            evalue=evalue,
        )
        execute(**kwargs)
        
        # read in expected files
        long_summary_expected = f"{here.parent}/expected/custom_evalue_param/long_summary.txt"
        short_summary_expected = f"{here.parent}/expected/custom_evalue_param/short_summary.txt"
        orthofisher_1001705at2759_expected = f"{here.parent}/expected/custom_evalue_param/all_sequences/1001705at2759.hmm.orthofisher"
        orthofisher_718307_expected = f"{here.parent}/expected/custom_evalue_param/all_sequences/718307-1.fa.mafft.hmm.orthofisher"
        scog_1001705at2759_expected = f"{here.parent}/expected/custom_evalue_param/scog/1001705at2759.hmm.orthofisher"
        scog_718307_expected = f"{here.parent}/expected/custom_evalue_param/scog/718307-1.fa.mafft.hmm.orthofisher"

        with open(long_summary_expected, "r") as expected:
            expected_long_summary_content = expected.read()
        with open(short_summary_expected, "r") as expected:
            expected_short_summary_content = expected.read()
        with open(orthofisher_1001705at2759_expected, "r") as expected:
            orthofisher_1001705at2759_expected_content = expected.read()
        with open(orthofisher_718307_expected, "r") as expected:
            orthofisher_718307_expected_content = expected.read()
        with open(scog_1001705at2759_expected, "r") as expected:
            scog_1001705at2759_expected_content = expected.read()
        with open(scog_718307_expected, "r") as expected:
            scog_718307_expected_content = expected.read()


        long_summary_created = f"orthofisher_output/long_summary.txt"
        short_summary_created = f"orthofisher_output/short_summary.txt"
        orthofisher_1001705at2759_created = f"orthofisher_output/all_sequences/1001705at2759.hmm.orthofisher"
        orthofisher_718307_created = f"orthofisher_output/all_sequences/718307-1.fa.mafft.hmm.orthofisher"
        scog_1001705at2759_created = f"orthofisher_output/scog/1001705at2759.hmm.orthofisher"
        scog_718307_created = f"orthofisher_output/scog/718307-1.fa.mafft.hmm.orthofisher"

        with open(long_summary_created, "r") as out_file:
            output_long_summary_content = out_file.read()
        with open(short_summary_created, "r") as out_file:
            output_short_summary_content = out_file.read()
        with open(orthofisher_1001705at2759_created, "r") as out_file:
            orthofisher_1001705at2759_created_content = out_file.read()
        with open(orthofisher_718307_created, "r") as out_file:
            orthofisher_718307_created_content = out_file.read()
        with open(scog_1001705at2759_created, "r") as expected:
            scog_1001705at2759_created_content = expected.read()
        with open(scog_718307_created, "r") as expected:
            scog_718307_created_content = expected.read()


        assert os.path.isdir('orthofisher_output')
        assert os.path.isdir('orthofisher_output/all_sequences')
        assert os.path.isdir('orthofisher_output/hmmsearch_output')
        assert os.path.isdir('orthofisher_output/scog')
        assert expected_long_summary_content == output_long_summary_content
        assert expected_short_summary_content == output_short_summary_content
        assert orthofisher_1001705at2759_expected_content == orthofisher_1001705at2759_created_content
        assert orthofisher_718307_expected_content == orthofisher_718307_created_content
        assert scog_1001705at2759_expected_content == scog_1001705at2759_created_content
        assert scog_718307_expected_content == scog_718307_created_content