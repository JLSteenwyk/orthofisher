Tutorial
========

**orthofisher** enables researchers to conduct high-throughput identification
of orthologous genes using Hidden Markov Models (HMM). This tutorial covers the
easy-to-implement workflow needed for using orthofisher.

|

^^^^^

1) Creating HMMs
################

Before using orthofisher, users will have to create (or curate) sets of HMMs of interest. 
HMMs can be curated from various sources including databases such as `Pfam database
<https://pfam.xfam.org/>`_. In this tutorial, we will go over creating your own HMMs.

First, we have to decide on genes of interest, download them, and align them. In this tutorial,
we will download protein sequences that are top hits in BLASTP searches
to the GAL1, GAL7, and GAL10 genes in *Saccharomyces cerevisiae*, which make up a very famous
metabolic gene cluster in fungi. To do so, I individually BLASTed the
`GAL1 <https://www.yeastgenome.org/locus/S000000224/protein>`_,
`GAL7 <https://www.yeastgenome.org/locus/S000000222/protein>`_, and
`GAL10 <https://www.yeastgenome.org/locus/S000000223/protein>`_ genes against NCBI's default database.
Next, I downloaded the aligned FASTA sequences for each gene, which can be downloaded here:

.. centered::
   Download GAL1/7/10 alignments:
   :download:`GAL alignments </data/gal_sequences.tar.gz>`

Unzip the directory and from within the new directory, and generate alignments for each set
of protein sequences. To do so, I will use `Clustal Omega <http://www.clustal.org/omega/>`_
alignment protocol, which is available via `EMBL-EBI <https://www.ebi.ac.uk/Tools/msa/clustalo/>`_.
However, other alignment software like `MAFFT <https://mafft.cbrc.jp/alignment/software/>`_ can be used.
Next, use the resulting alignments as input into the hmmbuild function from the HMMER suite
using the following commands:

.. code-block:: shell

   $ hmmbuild Gal1p.hmm Gal1p.aln.faa
   $ hmmbuild Gal7p.hmm Gal7p.aln.faa
   $ hmmbuild Gal10p.hmm Gal10p.aln.faa

|

2) Download the test data
#########################

For ease of use, this tutorial will rely on a small dataset, which can be downloaded using
the following link:

.. centered::
   Download test data:
   :download:`tutorial dataset </data/orthofisher_tutorial.tar.gz>`

Next, unzip the downloaded directory and change directory to the newly downloaded directory.

.. code-block:: shell

   $ cd path_to_unzipped_directory/orthofisher_tutorial

|

3) Run orthofisher
##################

Two arguments are required when using orthofisher. 

The first arument, -f/--fasta, points to a two column tab delimited file that specifies
the location of fasta files that will be searched using HMMs. Typically, these are protein
fasta files from the entire genome/transcriptome of an organism. Additionally, the second
column of the file specifies the identifier for the organism. This will be used when
representing sequences from a given proteome in a multi-fasta file. In this tutorial,
this is file **fasta_arg.txt**.

The second argument, -m is a file that points to the location of HMMs that you wish to 
identify or *fish out* of a given proteome. In this tutorial, this is file **hmms.txt**.

.. code-block:: shell

   $ orthofisher -m hmms.txt -f fasta_arg.txt

|

4) Examine output
#################

In the current working directory, a subdirectory will be made titled *orthofisher_output*.
Each subdirectory therein contains desirable output, which is briefly desired as:

1. all_sequences: multi-fasta file sequences of every hit identified during sequence similarity search.
2. hmmsearch_output: output files generated during hmmsearches
3. scog: a directory of single copy orthologous HMMs identified in the various fasta files

Also, two text files are made with helpful information that summarizes all the searches:

1. long_summary.txt: Hits identified during sequence similarity search per fasta file per HMM. 
HMMs are considered single-copy, multi-copy, or absent in a given fasta file.

.. code-block:: shell

   $ cat orthofisher_output/long_summary.txt Clavispora_lusitaniae_P5.faa    Gal10p.hmm      single-copy     1       QFZ46524.1
   Clavispora_lusitaniae_P5.faa    Gal1p.hmm       single-copy     1       QFZ46523.1
   Clavispora_lusitaniae_P5.faa    Gal7p.hmm       single-copy     1       QFZ46527.1
   Kluyveromyces_lactis_NRRL_Y-1140.faa    Gal10p.hmm      single-copy     1       XP_455462.1
   Kluyveromyces_lactis_NRRL_Y-1140.faa    Gal1p.hmm       single-copy     1       XP_455461.1
   Kluyveromyces_lactis_NRRL_Y-1140.faa    Gal7p.hmm       single-copy     1       XP_455463.1
   Saccharomyces_cerevisiae_S288C.faa      Gal10p.hmm      single-copy     1       NP_009575.1
   Saccharomyces_cerevisiae_S288C.faa      Gal1p.hmm       multi-copy      2       NP_009576.1
   Saccharomyces_cerevisiae_S288C.faa      Gal1p.hmm       multi-copy      2       NP_010292.1
   Saccharomyces_cerevisiae_S288C.faa      Gal7p.hmm       single-copy     1       NP_009574.1
   Yarrowia_lipolytica_DSM3286.faa Gal10p.hmm      single-copy     1       QNP99911.1
   Yarrowia_lipolytica_DSM3286.faa Gal1p.hmm       single-copy     1       QNP96229.1
   Yarrowia_lipolytica_DSM3286.faa Gal7p.hmm       single-copy     1       QNP99718.1

col. 1: Query proteome fasta file. |br|
col. 2: HMM file used during sequence similarity search. |br|
col. 3: The sequence represented by the HMM is considered single_copy, multi-copy, or absent in a query proteome. |br|
col. 4: Absolute copy number of hits from the sequence similarity search. |br|
col. 5: The fasta entry identifier of the gene identified. |br|

2. short_summary.txt: Summary of the absolute number and percentage of single-copy, multi-copy, or absent HMMs
per fasta file.

.. code-block:: shell

   $ cat orthofisher_output/short_summary.txt
   file_name       single-copy     multi-copy      absent  per_single-copy per_multi-copy  per_absent
   Clavispora_lusitaniae_P5.faa    3       0       0       1.0     0.0     0.0
   Kluyveromyces_lactis_NRRL_Y-1140.faa    3       0       0       1.0     0.0     0.0
   Saccharomyces_cerevisiae_S288C.faa      2       1       0       0.67    0.33    0.0
   Yarrowia_lipolytica_DSM3286.faa 3       0       0       1.0     0.0     0.0

col. 1: Query proteome fasta file. |br|
col. 2-4: Absolute number of sequences represented by HMMs that are present in single-copy, multi-copy, or absent. |br|
col. 5-7: Percetange of sequences represented by HMMs that are present in single-copy, multi-copy, or absent. |br|

.. |br| raw:: html

   <br />

|

5) Estimating gene family copy number
#####################################

In the original paper describing orthofisher, we note that orthofisher can also be used to estimate gene family
copy number using a zinc finger, C2H2 type, (Pfam: PF00096) as an example. Following that, we will now estimate
PF00096 domain copy number among the same set of proteomes.

To do so, first download the PF00096 HMM from `EMBL-EBI <http://pfam.xfam.org/family/zf-C2H2#tabview=tab6>`_, which is also available here:

.. centered::
   Download Zinc Finger, C2H2 type, HMM:
   :download:`PF00096.hmm </data/PF00096.hmm>`

Next, follow the step described above to run orthofisher using PF00096.hmm. Of note, we recommend lowering the bitscore threshold
to a less stringent value. The default bitscore threshold is 85% of the best hit, which follows the `BUSCO <https://busco.ezlab.org/>`_ pipeline.
However, depending on the research question, lowering the threshold may be reasonable. For example, try running orthofisher using the -b parameter 
set to 0.85 and 0.2. Using a threshold of 0.2, Clavispora_lusitaniae_P5.faa has 27 copies, Kluyveromyces_lactis_NRRL_Y-1140.faa has 23 copies,
Saccharomyces_cerevisiae_S288C.faa has 31 copies, and Yarrowia_lipolytica_DSM3286.faa has 28 copes of PF00096 whereas the same species have 1, 1, 1, and 3
copies respectively. 

We provide an additional level of user-flexibility by having a e-value threshold that can be used during HMM-based sequence similarity search. To change the 
e-value threshold from the default value of 1e-3, use the -e parameter.

