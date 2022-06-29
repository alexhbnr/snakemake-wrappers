__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

from snakemake.shell import shell

dbdir = snakemake.params.get("dbdir", "")

shell(
    "(echo {dbdir} |"
    " checkm data setRoot {dbdir})"
)
