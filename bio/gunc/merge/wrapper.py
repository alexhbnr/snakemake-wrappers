__author__ = "Alexander Hübner"
__license__ = "MIT"

import shutil

from snakemake.shell import shell

dir = snakemake.params.get("dir")
assert dir is not None, "Please provide a location for result directory."

shell(
    "(gunc merge_checkm "
    "    -g {snakemake.input.gunc} "
    "    -c {snakemake.input.checkm} "
    "    -o {dir})"
)

shutil.move(f"{dir}/GUNC_checkM.merged.tsv",
            snakemake.output[0])
