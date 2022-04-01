__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

outputprefix = snakemake.params.get("outputprefix", "")
bamfn = snakemake.params.get("bam", "")
region = snakemake.params.get("region", "")
minmq = snakemake.params.get("minmq", "")
minbq = snakemake.params.get("minbq", "")

shell(
    "(angsd "
    "    -i {bamfn} "
    "    -r {region} "
    "    -doCounts 1 "
    "    -iCounts 1 "
    "    -minMapQ {minmq} "
    "    -minQ {minbq} "
    "    -out {outputprefix})"
)
