#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convenience wrapper for running project directly from source tree."""
import sys

from orthofisher.orthofisher import main

if __name__ == "__main__":
    main(sys.argv[1:])