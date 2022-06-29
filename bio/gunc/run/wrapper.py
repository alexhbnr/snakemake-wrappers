__author__ = "Alexander Hübner"
__license__ = "MIT"

from glob import glob
import os
import sys

from snakemake.shell import shell


outdir = snakemake.params.get("outdir")
assert outdir is not None, "Please provide a location for result directory."
tmpdir = snakemake.params.get("tmpdir", f"{outdir}/tmp")
os.makedirs(tmpdir, exist_ok=True)

fadir = snakemake.params.get("fadir")
assert fadir is not None, "Please provide a location that contains the Fasta files of the MAGs."
assert len(glob(f"{fadir}/*.fa")) > 0, (f"The --input_dir {fadir} does not contain "
                                        "any files with the suffix .fa. Please provide "
                                        "a directory with FastA files with the suffix .fa.")

shell(
    "(gunc run "
    "    -r {snakemake.params.db_file} "
    "    --input_dir {fadir} "
    "    -t {snakemake.threads} "
    "    -o {outdir} "
    "    --temp_dir {tmpdir} "
    "    --detailed_output)"
)

os.rmdir(tmpdir)
