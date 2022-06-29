__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

outdir = snakemake.params.get("outdir", "")
url = snakemake.params.get("url", "")
tarball = os.path.basename(url)

shell(
    "(cd {outdir} && "
    "  wget {url} && "
    "  tar xvf {tarball})"
)
