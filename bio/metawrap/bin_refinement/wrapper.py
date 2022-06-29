__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

outdir = snakemake.params.get("outdir", "")
min_completeness = snakemake.params.get("min_completeness", "")
max_contamination = snakemake.params.get("max_contamination", "")

os.makedirs(outdir, exist_ok=True)

shell(
    "(metawrap bin_refinement -o {outdir} "
    " -t {snakemake.threads}"
    " -c {min_completeness}"
    " -x {max_contamination}"
    " -A {snakemake.params.maxbin2}"
    " -B {snakemake.params.metabat2}"
    " -C {snakemake.params.concoct}) || touch {snakemake.output[0]}"
)
