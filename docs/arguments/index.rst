Arguments
=========

**orthofisher** provides researchers with flexibility to change parameters thereby allowing
for nuanced changes to pipeline that better fit their research question.

Further clarification about the usage of these parameters may be gained from checking out our tutorial.

|

^^^^^

Required
########
**-f, \-\-fasta**:
A two column tab delimited file that points to the location of fasta files that will be searched
using HMMs in the first column. Typically, these are protein fasta files from the entire genome/
transcriptome of an organism. The second column of the file specifies the identifier for the organism.

**-m, \-\-hmm**:
A single column file with the location of HMMs that you wish to identify or fish out of a given proteome.

|

Optional
########
**-e, \-\-evalue**:
Specify an e-value threshold to use when conducting sequence similarity searches (default: 0.001).
Format can be 1e-3 or 0.001.

**-b, \-\-bitscore**:
A fraction threshold to specify the bitscore threshold for sequences to be considered similar. More
specifically, if a hit has a bitscore less than the specified fraction, the gene will not be considered
sufficiently similar to be considered putatively orthologous. Value must range from 0 to 1 (default: 0.85).

**-c, \-\-cpu**:
Specify the number of parallel CPU workers to use for multithreading (default: 2). This argument is passed to HMMER.

**-o, \-\-output_dir**:
Name of the outputted directory with all results from the orthofisher run (default: orthofisher_output). Note, orthofisher will overwrite existing directories with the same name as specified by this argument.