from orthofisher.helper import (
    determine_search_tool,
    get_hmm_alphabet,
    parse_nhmmer_tblout,
)


def test_get_hmm_alphabet_reads_dna_hmm():
    hmm = "tests/samples/bena.fa.mafft.hmm"
    assert get_hmm_alphabet(hmm) == "DNA"


def test_determine_search_tool_auto_uses_nhmmer_for_dna_hmm():
    hmm = "tests/samples/bena.fa.mafft.hmm"
    assert determine_search_tool("auto", hmm) == "nhmmer"


def test_determine_search_tool_forced_protein_uses_hmmsearch():
    hmm = "tests/samples/bena.fa.mafft.hmm"
    assert determine_search_tool("protein", hmm) == "hmmsearch"


def test_determine_search_tool_forced_nucleotide_uses_nhmmer():
    hmm = "tests/samples/1001705at2759.hmm"
    assert determine_search_tool("nucleotide", hmm) == "nhmmer"


def test_parse_nhmmer_tblout_extracts_hits(tmp_path):
    tbl_path = tmp_path / "nhmmer.tbl"
    tbl_path.write_text(
        "# target name accession query name accession hmmfrom hmmto alifrom alito envfrom envto sqlen strand E-value score bias description of target\n"
        "targetA - modelA - 1 10 5 20 5 20 100 + 1e-20 75.5 0.0 desc\n"
        "targetB - modelA - 1 10 7 21 7 21 100 - 2e-05 40.1 0.1 desc\n"
    )

    hits = parse_nhmmer_tblout(str(tbl_path))
    assert len(hits) == 2
    assert hits[0].id == "targetA"
    assert hits[0]._id == "targetA"
    assert hits[0].evalue == 1e-20
    assert hits[0].bitscore == 75.5
