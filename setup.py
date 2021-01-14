from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

CLASSIFIERS = [
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
]

REQUIRES = [""]

setup(
    name="orthofisher",
    description="orthofisher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jacob L. Steenwyk",
    author_email="jlsteenwyk@gmail.com",
    url="https://github.com/JLSteenwyk/orthofisher.git",
    packages=["mipyp"],
    classifiers=CLASSIFIERS,
    entry_points={"console_scripts": ["mipyp = mipyp.mipyp:main"]},
    version="0.0.0",
    include_package_data=True,
    install_requires=REQUIRES,
)