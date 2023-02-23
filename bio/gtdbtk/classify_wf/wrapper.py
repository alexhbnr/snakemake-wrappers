__author__ = "Alexander Hübner"
__license__ = "MIT"

from pathlib import Path
import os

from snakemake.shell import shell

fadir = snakemake.params.get("fadir", "")
outdir = snakemake.params.get("outdir", "")
dbdir = snakemake.params.get("dbdir", "")

shell(
    "(GTDBTK_DATA_PATH={dbdir} "
    "gtdbtk classify_wf --cpu {snakemake.threads} "
    "--mash_db {dbdir}/mash_db "
    "--extension fa --genome_dir {fadir} --out_dir {outdir})"
)

if not os.path.isfile(snakemake.output[0]):
    print("WARNING: no MAGs from the kingdom bacterium found!")
    Path(snakemake.output[0]).touch()
