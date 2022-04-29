__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


import os
import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem

params_fastq = snakemake.params.get("fastq", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

mem = get_mem(snakemake, "MiB")
mem = "-m {0:.0f}M".format(mem / threads) if mem and threads else ""

shell(
    "(samtools fastq"
    " {params_fastq}"
    " -1 {snakemake.output[0]}"
    " -2 {snakemake.output[1]}"
    " -0 /dev/null"
    " -s /dev/null"
    " -F 0x900"
    " {snakemake.input[0]} "
    ") {log}"
)
