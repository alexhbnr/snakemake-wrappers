__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

shell(
    "(concoct_coverage_table.py "
    " {snakemake.input[0]}"
    " {snakemake.input[1]}"
    " > {snakemake.output[0]})"
)
