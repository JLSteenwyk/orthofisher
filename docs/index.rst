.. image:: ../_static/img/mipypro_logo_no_text.jpg
   :width: 55%
   :align: center
   :target: https://jlsteenwyk.com/mipypro

^^^^^

Recent analyses indicate that ~28% of available computational tools fail to install due to
implementation errors |Mangul|_. To address this issue, **Mi**\nimum **Py**\thon **P**\roject
(MiPyP, pronounced 'my pipe') provides a scaffold for researchers to build long-lasting bioinformatic
tools using a python code base. 

Specifically, MiPyP comes complete with the foundation to build command line tools for the UNIX shell
environment by providing a 'hello world' example, construct Sphinx-based documentation that can be linked
to a researcher's GitHub page, and comes with instructions to upload the project to PyPi. 


If you found MiPyPro useful, please cite *MiPyPro*. bioRxiv. doi: |doiLink|_.

.. _Mangul: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000333
.. |Mangul| replace:: (Mangul *et al.*, 2019) 


Quick Start
-----------
**1) Installation**

To install from source, we strongly recommend using a virtual environment. To do so, use the following commands:

.. code-block:: shell
	# download
	git clone https://github.com/JLSteenwyk/mipypro.git
	cd PhyKIT/
	# create virtual environment
	python -m venv .venv
	# activate virtual environment
	source .venv/bin/activate
	# install
	make install

To deactivate your virtual environment, use the following command:

.. code-block:: shell
	# deactivate virtual environment
	deactivate


^^^^

.. toctree::
	:maxdepth: 4

	about/index
	tutorial/index

^^^^

