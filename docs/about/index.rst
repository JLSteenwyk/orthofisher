About
=====

**orthofisher** extracts and determines the copy number of a predetermined set of orthologs, which
can be used for the identification of single copy orthologous genes or estimation of gene family copy number.

|

^^^^^

Performance Assessment
----------------------
Using 1,530 sequence similarity searches across six model eukaryotic proteomes, the performance of orthofisher
was compared to results obtained from BUSCO. Examination of precision and recall revealed near perfect performance.
More specifically, orthofisher had a **recall of 1.0 and precision of 0.99**. Precision is less
than 1.0 because priors of expected sequence length and sequence similarity scores--which are not implemented
in orthofisher--resulted in more missing genes in the BUSCO pipeline than the orthofisher pipeline.

|

^^^^^

The Developers
--------------

orthofisher is developed and maintained by `Jacob L. Steenwyk <https://jlsteenwyk.github.io/>`_.

|

|JLSteenwyk|

|GoogleScholarSteenwyk| |GitHubSteenwyk| |TwitterSteenwyk| 

`Jacob L. Steenwyk <https://jlsteenwyk.github.io/>`_ is a Howard Hughes Medical Institute
Gilliam fellow in the `Antonis Rokas Laboratory <https://as.vanderbilt.edu/rokaslab/>`_ at
`Vanderbilt University <https://www.vanderbilt.edu/>`_. His research foci include understanding 
the parameters that influence genome stability, the genomics of microbial domestication, and 
the evolution of pathogenicity. Beyond research, Steenwyk aims to make education more accessible 
through diverse avenues of community engagement. Find out more information at his 
`personal website <http://jlsteenwyk.github.io/>`_.

.. |JLSteenwyk| image:: ../_static/img/Steenwyk.jpg 
   :width: 35%

.. |GoogleScholarSteenwyk| image:: ../_static/img/GoogleScholar.png
   :target: https://scholar.google.com/citations?user=VXV2j6gAAAAJ&hl=en
   :width: 4.5%

.. |TwitterSteenwyk| image:: ../_static/img/Twitter.png
   :target: https://twitter.com/jlsteenwyk
   :width: 4.5%

.. |GitHubSteenwyk| image:: ../_static/img/Github.png
   :target: https://github.com/JLSteenwyk
   :width: 4.5%

