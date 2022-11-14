__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os
from pathlib import Path
import subprocess

from snakemake.shell import shell

outdir = snakemake.params.get("outdir", "")
min_completeness = snakemake.params.get("min_completeness", "")
max_contamination = snakemake.params.get("max_contamination", "")

os.makedirs(outdir, exist_ok=True)

try:
    shell(
        "(metawrap bin_refinement -o {outdir} "
        " -t {snakemake.threads}"
        " -c {min_completeness}"
        " -x {max_contamination}"
        " -A {snakemake.params.maxbin2}"
        " -B {snakemake.params.metabat2}"
        " -C {snakemake.params.concoct})"
    )
except subprocess.CalledProcessError:
    print("MetaWRAP was not able to find bins. Check the log files!")
    Path(f"{outdir}/metawrap_50_10_bins.stats").touch()

if not os.path.isdir(f"{outdir}/metawrap_50_10_bins"):
    os.makedirs(f"{outdir}/metawrap_50_10_bins")

Path(snakemake.output[0]).touch()
