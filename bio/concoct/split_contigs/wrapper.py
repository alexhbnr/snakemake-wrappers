__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

shell(
    "(cut_up_fasta.py "
    " {snakemake.input[0]}"
    " -c 10000"
    " --merge_last"
    " -b {snakemake.output[1]}"
    " -o 0"
    " > {snakemake.output[0]})"
)
