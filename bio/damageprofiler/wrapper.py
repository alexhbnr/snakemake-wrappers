__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

outdir = snakemake.params.get("dir", "")
reffasta = snakemake.params.get("reffasta", "")
title = snakemake.params.get("title", "")

shell(
    "(damageprofiler "
    "    -Xmx10g "
    "    -i {snakemake.input[0]} "
    "    -o {outdir} "
    "    -r {reffasta} "
    "    -title {title})"
)
