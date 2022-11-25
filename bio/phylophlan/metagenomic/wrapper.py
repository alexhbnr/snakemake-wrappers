__author__ = "Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

dbdir = snakemake.params.get("dbdir")
fadir = snakemake.params.get("fadir")
prefix = snakemake.params.get("prefix")
db = snakemake.params.get("db")
os.makedirs(dbdir, exist_ok=True)

shell(
    "(phylophlan_metagenomic -i {fadir} "
    " --input_extension *.fa "
    " -o {prefix} "
    " --nproc {snakemake.threads} "
    " -n 10 --verbose "
    " --database {db} --database_folder {dbdir})"
)

os.rename(f"{prefix}.tsv", snakemake.output[0])
