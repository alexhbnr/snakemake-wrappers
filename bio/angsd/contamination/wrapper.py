__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

hapmapfn = snakemake.params.get("hapmap", "")

shell(
    "(contamination "
    "    -a {snakemake.input[0]} "
    "    -h {hapmapfn} "
    "    -p {snakemake.threads} "
    "    |&tee {snakemake.output[0]})"
)
