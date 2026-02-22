.. _change_log:


Change log
==========

^^^^^

Major changes to orthofisher are summarized here.

**1.1.3**:

- Added ``--seq-type`` with ``protein``, ``nucleotide``, and ``auto`` modes.
- ``--seq-type auto`` now infers HMM alphabet and dispatches ``hmmsearch`` or ``nhmmer``.
- Added ``--resume`` checkpoint mode to continue interrupted runs in an existing output directory.
- Added tests covering nucleotide auto-dispatch and resume/checkpoint behavior.
- Updated usage/docs for nucleotide-query workflows and resumed execution.

**1.1.2**:

- Default output is now slim (``scog/``, ``long_summary.txt``, ``short_summary.txt``).
- Added ``--verbose-output`` to also write ``all_sequences/`` and retain ``hmmsearch_output/`` files.
- Added ``--force`` to explicitly overwrite an existing output directory.
- Updated Python support to 3.10-3.13 and dropped 3.9.
- ``long_summary.txt`` now includes per-hit ``evalue`` and ``bitscore`` columns.
- Improved CLI validation for ``--evalue``, ``--bitscore``, and ``--cpu``.
- Improved runtime error handling with clearer typed exceptions and centralized CLI error reporting.
- Refactored integration and entrypoint tests to reduce duplication and improve environment portability.

**1.0.0**: introduced -c, \-\-\cpu argument and -o, \-\-output_dir argument

**0.2.0**: compatible with python 3.9 and biopython 1.79

**0.0.8**: created -b, \-\-bitscore parameter
