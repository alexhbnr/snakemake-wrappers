__author__ = "Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

dbdir = snakemake.params.get("dir")
assert dbdir is not None, "Please provide a location for installing the GUNC database."

os.makedirs(dbdir, exist_ok=True)
shell(
    "(gunc download_db {dbdir})"
)
