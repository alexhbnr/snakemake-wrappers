__author__ = "Alexander Hübner"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

shell(
    "(mmseqs createdb "
    " {snakemake.input[0]} "
    " {snakemake.output[0]} "
    "{extra})"
)
