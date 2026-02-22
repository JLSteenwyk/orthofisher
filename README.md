<p align="center">
  <a href="https://github.com/jlsteenwyk/orthofisher">
    <img src="https://raw.githubusercontent.com/JLSteenwyk/orthofisher/master/docs/_static/img/orthofisher_full_logo.png" alt="Logo" width="400">
  </a>
  <p align="center">
    <a href="https://jlsteenwyk.com/orthofisher/">Docs</a>
    ·
    <a href="https://github.com/jlsteenwyk/orthofisher/issues">Report Bug</a>
    ·
    <a href="https://github.com/jlsteenwyk/orthofisher/issues">Request Feature</a>
  </p>
    <p align="center">
        <a href="https://github.com/JLSteenwyk/orthofisher/actions" alt="Build">
            <img src="https://img.shields.io/github/actions/workflow/status/JLSteenwyk/orthofisher/ci.yml?branch=main">
        </a>
        <a href="https://codecov.io/gh/jlsteenwyk/orthofisher" alt="Coverage">
          <img src="https://codecov.io/gh/JLSteenwyk/orthofisher/branch/main/graph/badge.svg?token=7LYMLHDL9D"/>
        </a>
        <a href="https://github.com/jlsteenwyk/orthofisher/graphs/contributors" alt="Contributors">
            <img src="https://img.shields.io/github/contributors/jlsteenwyk/orthofisher">
        </a>
        <a href="https://bsky.app/profile/jlsteenwyk.bsky.social" target="_blank" rel="noopener noreferrer">
          <img src="https://img.shields.io/badge/Bluesky-0285FF?logo=bluesky&logoColor=fff">
        </a>
        <br />
        <a href="https://pepy.tech/badge/orthofisher">
          <img src="https://static.pepy.tech/personalized-badge/orthofisher?period=total&units=international_system&left_color=grey&right_color=blue&left_text=PyPi%20Downloads">
        </a>
        <a href="https://lbesson.mit-license.org/" alt="License">
            <img src="https://img.shields.io/badge/License-MIT-blue.svg">
        </a>
        <a href="https://pypi.org/project/orthofisher/" alt="PyPI - Python Version">
            <img src="https://img.shields.io/pypi/pyversions/orthofisher">
        </a>
        <a href="https://academic.oup.com/g3journal/article/11/9/jkab250/6321954">
          <img src="https://zenodo.org/badge/DOI/10.1093/g3journal/jkab250.svg">
        </a>
    </p>
</p>

<br />

Orthofisher conducts automated and high-throughout identification of a predetermined set of orthologs, which can be used for phylgenomics, gene family copy number determination and more!<br /><br />

If you found orthofisher useful, please cite *orthofisher: a broadly applicable tool for automated gene identification and retrieval*. Steenwyk & Rokas 2021, G3 Genes|Genomes|Genetics. doi: [10.1093/g3journal/jkab250](https://academic.oup.com/g3journal/advance-article/doi/10.1093/g3journal/jkab250/6321954?login=true).
<br /><br />

---

<br />

## Guide
[Quick Start](#quick-start)<br />
[Performance Assessment](#performance-assessment)<br />
[FAQ](#faq)

<br />

---

<br/>

## Quick Start

For detailed instructions on usage and a tutorial, please see the [online documentation](https://jlsteenwyk.com/orthofisher/).

<br/>

### 1) Prerequisite
Before installing orthofisher, please first install [HMMER3](http://hmmer.org/documentation.html) and add the HMMER to your .bashrc path. For example, my .bashrc has the following:

```shell
export PATH=$PATH:/home/steenwj/SOFTWARE/hmmer-3.1b2-linux-intel-x86_64/binaries
```

<br/>

### 2) Install orthofisher

Supported Python versions: **3.10, 3.11, 3.12, and 3.13**.

**If you are having trouble installing orthofisher, please contact the lead developer, Jacob L. Steenwyk, via [email](https://jlsteenwyk.com/contact.html) or [twitter](https://twitter.com/jlsteenwyk) to get help.**

<br/>

To install via *anaconda*, execute the follwoing command:
``` shell
conda install -c jlsteenwyk orthofisher
```
Visit here for more information: https://anaconda.org/jlsteenwyk/orthofisher

<br/>

To install via *pip*, execute the follwoing command:
```shell
pip install orthofisher
```

<br />

To install from source, execute the follwoing command:
```shell
# download
git clone https://github.com/JLSteenwyk/orthofisher.git
# change dir
cd orthofisher/
# install
make install
```

<br/>

If you run into software dependency issues, install orthofisher in a virtual environment. To do so, create your virtual environment with the following command: 
```shell
# create virtual environment
python -m venv .venv
# activate virtual environment
source .venv/bin/activate
```

Next, install the software using your preferred method above. Thereafter, you will be able to use orthofisher.

To deactivate your virtual environment, use the following command:
```shell
# deactivate virtual environment
deactivate
```
**Note, the virtual environment must be activated to use *orthofisher*.**

<br />

### 3) Run orthofisher

```shell
orthofisher -m hmms.txt -f fasta_arg.txt
```

To query nucleotide sequences with nucleotide HMMs, use:

```shell
orthofisher -m hmm_nucl.txt -f fasta_nucl.txt --seq-type nucleotide
```

The default `--seq-type auto` mode infers the tool per HMM from the `ALPH` header:
- `ALPH DNA` / `ALPH RNA` -> `nhmmer`
- other alphabets (for example amino-acid models) -> `hmmsearch`

By default, orthofisher now writes a **slim output**:

- `scog/`
- `long_summary.txt`
- `short_summary.txt`

To additionally write larger raw outputs (`all_sequences/` and `hmmsearch_output/`), use:

```shell
orthofisher -m hmms.txt -f fasta_arg.txt --verbose-output
```

If your output directory already exists, orthofisher will stop with an error.
To overwrite the existing output directory, add:

```shell
orthofisher -m hmms.txt -f fasta_arg.txt --force
```

You can combine both flags:

```shell
orthofisher -m hmms.txt -f fasta_arg.txt --verbose-output --force
```

To continue an interrupted run in an existing output directory, use:

```shell
orthofisher -m hmms.txt -f fasta_arg.txt -o orthofisher_output --resume
```

`--resume` reuses checkpoint state, skips completed FASTA/HMM pairs, and rewrites
`short_summary.txt` from the resumed totals.

<br />

---

<br />

## Performance Assessment
Using 1,530 sequence similarity searches across six model eukaryotic proteomes, the performance of orthofisher was compared to results obtained from BUSCO. Examination of precision and recall revealed near perfect performance. More specifically, orthofisher had a <strong>recall of 1.0 and precision of 0.99</strong>. Precision is less than 1.0 because priors of expected sequence length and sequence similarity scores--which are not implemented in orthofisher--resulted in more missing genes in the BUSCO pipeline than the orthofisher pipeline.

<br />

---

<br />

## FAQ

<br />

<strong>I am having trouble installing orthofisher, what should I do?</strong>

Please install orthofisher using a virtual environment as described in the installation instructions. If you are still running into issues after installing in a virtual environment, please contact Jacob L. Steenwyk via [email](https://jlsteenwyk.com/contact.html) or [twitter](https://twitter.com/jlsteenwyk).

<br />

---

<br />

### orthofisher is developed and maintained by [Jacob Steenwyk](https://jlsteenwyk.github.io/)
