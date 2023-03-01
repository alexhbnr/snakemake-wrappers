__author__ = "Alexander Hübner"
__license__ = "MIT"

import tempfile

from snakemake.shell import shell


ptmpdir = snakemake.params.get("tmpdir", None)
dbname = snakemake.params.get("db", "")
prefix = snakemake.params.get("prefix", "")
extra = snakemake.params.get("extra", "")

with tempfile.TemporaryDirectory(dir=ptmpdir) as tmpdir:
    shell(
        "(mmseqs databases "
        f"{dbname} {prefix} {tmpdir} "
        "--threads {snakemake.threads} "
        f" {extra})"
    )
