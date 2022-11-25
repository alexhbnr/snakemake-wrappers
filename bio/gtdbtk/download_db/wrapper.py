__author__ = "Alexander Hübner"
__license__ = "MIT"

import os

from snakemake.shell import shell

url = snakemake.params.get("url", "")
resourcedir = snakemake.params.get("resourcedir", "")
gtdbtk_dir = f"{resourcedir}/gtdbtk/gtdbtk_r207_v2"
tarball_fn = f"{resourcedir}/gtdbtk/{os.path.basename(url)}"

shell(
    "(wget -O {tarball_fn} {url} && "
    "tar -xvzf {tarball_fn} -C '{gtdbtk_dir}' --strip 1 > /dev/null && "
    "rm {tarball_fn} && "
    "conda env config vars set GTDBTK_DATA_PATH='{gtdbtk_dir}')"
)
