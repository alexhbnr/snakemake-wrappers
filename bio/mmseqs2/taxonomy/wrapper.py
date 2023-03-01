__author__ = "Alexander Hübner"
__license__ = "MIT"

import os
import tempfile

from snakemake.shell import shell

ptmpdir = snakemake.params.get("tmpdir", None)
prefix = snakemake.params.get("prefix", "")
extra = snakemake.params.get("extra", "")

assert os.stat(snakemake.input.contigs).st_size > 0, "Contig database seems to be empty."

with tempfile.TemporaryDirectory(dir=ptmpdir) as tmpdir:
    shell(
        "(mmseqs taxonomy "
        "{snakemake.input[0]} "
        "{snakemake.input[1]} "
        "{snakemake.params.prefix} "
        f"{tmpdir} "
        " --threads {snakemake.threads} "
        f"{extra})"
    )
