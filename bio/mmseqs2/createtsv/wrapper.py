__author__ = "Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

prefix = snakemake.params.get("prefix", "")
extra = snakemake.params.get("extra", "")

assert os.stat(snakemake.input.contigs).st_size > 0, "Contig database seems to be empty."

shell(
    "(mmseqs createtsv "
    "{snakemake.input[0]} "
    "{snakemake.params.prefix} "
    "{snakemake.output[0]} "
    " --threads {snakemake.threads} "
    f"{extra})"
)
