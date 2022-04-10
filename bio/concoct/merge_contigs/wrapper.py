__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

clustering = snakemake.params.get("clustering", "")

shell(
    "(merge_cutup_clustering.py "
    " {clustering}"
    " > {snakemake.output[0]})"
)
