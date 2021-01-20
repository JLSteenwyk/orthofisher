Tutorial
========

**orthofisher** enables researchers to conduct high-throughput identification
of orthologous genes using Hidden Markov Models (HMM). This tutorial covers the
easy-to-implement workflow needed for using orthofisher.

|

^^^^^

1. Download the test data
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

^^^^^

2. Run orthofisher
##################

Two arguments are required when using orthofisher. 

The first arument, -f/--fasta, points to a two column file that points to the location 
of fasta files that will be searched using HMMs. Typically, these are protein fasta
files from the entire genome/transcriptome of an organism. Additionally, the second
column of the file specifies the identifier for the organism. This will be used when
representing sequences from a given proteome in a multi-fasta file. In this tutorial,
this is file **fasta_arg.txt**.

The second argument, -m is a file that points to the location of HMMs that you wish to 
identify or *fish out* of a given proteome. In this tutorial, this is file **hmms.txt**.

.. code-block:: shell

   $ orthofisher -m hmms.txt -f fasta_arg.txt

|

^^^^^

3. Examine output
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

   $ cat orthofisher_output/long_summary.txt
   GCF_010094145.1_Didex1_protein.faa      718307-1.fa.mafft.hmm single_copy      1       XP_033451061.1
   GCF_010094145.1_Didex1_protein.faa      1001705at2759.hmm     single_copy      1       XP_033445010.1
   GCA_011032825.1_Masph1_protein.faa      718307-1.fa.mafft.hmm single_copy      1       KAF2869753.1
   GCA_011032825.1_Masph1_protein.faa      1001705at2759.hmm     single_copy      1       KAF2868776.1
   no_copy.faa     718307-1.fa.mafft.hmm   absent  0       NA
   no_copy.faa     1001705at2759.hmm       absent  0       NA
   multi_copy.faa  718307-1.fa.mafft.hmm   multi-copy      2     Massariosphaeria_phaeospora
   multi_copy.faa  718307-1.fa.mafft.hmm   multi-copy      2     Didymella_exigua
   multi_copy.faa  1001705at2759.hmm       absent  0       NA

col. 1: Query proteome fasta file. |br|
col. 2: HMM file used during sequence similarity search. |br|
col. 3: The sequence represented by the HMM is considered single_copy, multi-copy, or absent in a query proteome. |br|
col. 4: Absolute copy number of hits from the sequence similarity search. |br|
col. 5: The fasta entry identifier of the gene identified. |br|

2. short_summary.txt: Summary of the absolute number and percentage of single-copy, multi-copy, or absent HMMs
per fasta file.

.. code-block:: shell

   $ cat orthofisher_output/short_summary.txt
   file_name       single-copy     multi-copy      absent  per_single-copy        per_multi-copy  per_absent
   GCF_010094145.1_Didex1_protein.faa      2       0       0     1.0      0.0     0.0
   GCA_011032825.1_Masph1_protein.faa      2       0       0     1.0      0.0     0.0
   no_copy.faa     0       0       2       0.0     0.0     1.0
   multi_copy.faa  0       1       1       0.0     0.5     0.5

col. 1: Query proteome fasta file. |br|
col. 2-4: Absolute number of sequences represented by HMMs that are present in single-copy, multi-copy, or absent. |br|
col. 5-7: Percetange of sequences represented by HMMs that are present in single-copy, multi-copy, or absent. |br|

.. |br| raw:: html

   <br />
                     