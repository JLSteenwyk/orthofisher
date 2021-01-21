Install
=======

^^^^^

1) Prerequisite
############

Before installing orthofisher, please first install `HMMER3 <http://hmmer.org/download.html>`_ and 
add HMMER to your *.bashrc* path. For example, my *.bashrc* has the following:

.. code-block:: shell

   export PATH=$PATH:/home/steenwj/SOFTWARE/hmmer-3.1b2-linux-intel-x86_64/binaries


|

2) Install orthofisher
######

If you are having trouble installing orthofisher, please contact the lead developer, `Jacob L. 
Steenwyk <https://jlsteenwyk.com>`_ , via `email <https://jlsteenwyk.com/contact.html>`_ or `twitter <https://twitter.com/jlsteenwyk>`_
to get help.

|

To install via *anaconda*, execute the follwoing command:

.. code-block:: shell

   conda install -c jlsteenwyk orthofisher

Visit here for more information: https://anaconda.org/jlsteenwyk/clipkit

|

To install via *pip*, execute the follwoing command:

.. code-block:: shell

   pip install orthofisher


|

To install from source, execute the follwoing command:

.. code-block:: shell

   # download
   git clone https://github.com/JLSteenwyk/orthofisher.git
   # change dir
   cd orthofisher/
   # install
   make install


|

If you run into software dependency issues, install orthofisher in a virtual environment.
To do so, create your virtual environment with the following command: 

.. code-block:: shell

   # create virtual environment
   python -m venv .venv
   # activate virtual environment
   source .venv/bin/activate


Next, install the software using your preferred method above. Thereafter, you will be able to use orthofisher.

To deactivate your virtual environment, use the following command:

.. code-block:: shell

   # deactivate virtual environment
   deactivate

**Note, if you install via a virtual environment, the environment must be activated to use orthofisher.**