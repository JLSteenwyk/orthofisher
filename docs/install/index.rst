Install
=======

^^^^^

To ensure users are able to install orthofisher using a workflow they are familiar with, orthofisher
is available for download from GitHub, PyPi, and the Anaconda cloud. However, before installing orthofisher,
please first install `HMMER3 <http://hmmer.org/download.html>`_

1) Prerequisite
############

Before installing orthofisher, please first install `HMMER3 <http://hmmer.org/download.html>`_ and 
add the HMMER to your *.bashrc* path. For example, my *.bashrc* has the following:

.. code-block:: shell

   export PATH=$PATH:/home/steenwj/SOFTWARE/hmmer-3.1b2-linux-intel-x86_64/binaries


|

2a) GitHub
######

To install *orthofisher*, execute the following commands:

.. code-block:: shell

   $ git clone https://github.com/JLSteenwyk/orthofisher.git
   $ cd orthofisher
   $ make install

If you run into permission errors when executing make install, create a virtual environment for your installation:

.. code-block:: shell
   $ git clone https://github.com/JLSteenwyk/orthofisher.git
   $ cd orthofisher/
   $ python -m venv .venv
   $ source .venv/bin/activate
   $ make install

Note, the virtual environment must be activated to use clipkit.

|

*Coming soon*: Installion via PyPi and conda.