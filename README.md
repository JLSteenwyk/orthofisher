<p align="center">
  <a href="https://github.com/jlsteenwyk/orthofisher">
    <img src="https://raw.githubusercontent.com/JLSteenwyk/orthofisher/master/docs/_static/img/orthofisher.jpg" alt="Logo" width="400">
  </a>
  <p align="center">
    <a href="https://jlsteenwyk.com/orthofisher/">Docs</a>
    ·
    <a href="https://github.com/jlsteenwyk/orthofisher/issues">Report Bug</a>
    ·
    <a href="https://github.com/jlsteenwyk/orthofisher/issues">Request Feature</a>
  </p>
    <p align="center">
        <a href="https://lbesson.mit-license.org/" alt="License">
            <img src="https://img.shields.io/badge/License-MIT-blue.svg">
        </a>
        <a href="https://pypi.org/project/orthofisher/" alt="PyPI - Python Version">
            <img src="https://img.shields.io/pypi/pyversions/orthofisher">
        </a>
        <a href="https://github.com/JLSteenwyk/orthofisher/actions" alt="Build">
            <img src="https://img.shields.io/github/workflow/status/jlsteenwyk/orthofisher/CI">
        </a>
        <a href="https://codecov.io/gh/jlsteenwyk/orthofisher" alt="Coverage">
          <img src="https://codecov.io/gh/JLSteenwyk/orthofisher/branch/main/graph/badge.svg?token=7LYMLHDL9D"/>
        </a>
        <a href="https://github.com/jlsteenwyk/orthofisher/graphs/contributors" alt="Contributors">
            <img src="https://img.shields.io/github/contributors/jlsteenwyk/orthofisher">
        </a>
        <a href="https://twitter.com/intent/follow?screen_name=jlsteenwyk" alt="Author Twitter">
            <img src="https://img.shields.io/twitter/follow/jlsteenwyk?style=social&logo=twitter"
                alt="follow on Twitter">
        </a>
    </p>
</p>

Orthofisher conducts automated and high-throughout identification of a predetermined set of orthologs, which can be used for phylgenomics, gene family 
copy number determination and more!

---

<br/>

## Quick Start

To ensure users are able to install orthofisher using a workflow they are familiar with, orthofisher is available for download from GitHub, PyPi, and the Anaconda cloud. However, before installing orthofisher, please first install [HMMER3](http://hmmer.org/documentation.html).

<br/>

### 1) Prerequisite
Before installing orthofisher, please first install HMMER3 and add the HMMER to your .bashrc path. For example, my .bashrc has the following:

```shell
export PATH=$PATH:/home/steenwj/SOFTWARE/hmmer-3.1b2-linux-intel-x86_64/binaries
```

<br/>

### 2) Install orthofisher

**If you are having trouble installing orthofisher, please contact the lead developer, Jacob L. Steenwyk, via [email](https://jlsteenwyk.com/contact.html) or [twitter](https://twitter.com/jlsteenwyk) to get help.**

To install from source, we strongly recommend using a virtual environment. To do so, use the following commands:
```shell
# download
git clone https://github.com/JLSteenwyk/orthofisher.git
cd orthofisher/
# create virtual environment
python -m venv .venv
# activate virtual environment
source .venv/bin/activate
# install
make install
```
To deactivate your virtual environment, use the following command:
```shell
# deactivate virtual environment
deactivate
```
**Note, the virtual environment must be activated to use *orthofisher*.**