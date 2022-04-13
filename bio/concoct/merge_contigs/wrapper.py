__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

import os
from pathlib import Path

clustering = snakemake.params.get("clustering", "")

if os.path.isfile(clustering):

    shell(
        "(merge_cutup_clustering.py "
        " {clustering}"
        " > {snakemake.output[0]})"
    )

else:

    Path(snakemake.output[0]).touch()
