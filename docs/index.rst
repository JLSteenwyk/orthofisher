.. image:: /_static/img/orthofisher.jpg
   :width: 55%
   :align: center
   :target: https://jlsteenwyk.com/orthofisher

^^^^^

Introduction
------------

Automated and high-throughout identification of a predetermined set of putative orthologous genes can be
a helpful task for phylogenomics/phylogenetics, gene family copy number determination, etc. 

To facilitate these analyses, **orthofisher** conducts automated HMMsearches among a set of proteomes using
a predetermined set of orthologs. Sequence similarity searches classify results as multi-copy, single-copy,
or absent in a given proteome. For the purposes of phylogenomics/phylogenetics, multi-fasta files are generated
for all sequences as well as those that are single-copy; for gene family copy number determination, easily
parsed output files contain absolute copy number of hits from the sequence similarity search.

If you found orthofisher useful, please cite orthofisher: a broadly applicable tool for automated gene
identification and retrieval. Steenwyk & Rokas 2021, G3: Genes | Genomes | Genetics. doi:
`10.1093/g3journal/jkab250 <https://jlsteenwyk.com/publication_pdfs/2021_Steenwyk_and_Rokas_G3.pdf>`_.

^^^^

.. toctree::
	:maxdepth: 4

	about/index
	arguments/index
	install/index
	tutorial/index
	other_software/index
	frequently_asked_questions/index

^^^^

