__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

outdir = snakemake.params.get("outdir", "")
workfiles = snakemake.params.get("workfiles", "")

shell(
    "(metawrap binning -o {outdir} "
    " -t {snakemake.threads}"
    " -a {snakemake.input[0]}"
    " --concoct"
    " --metabat2"
    " --maxbin2"
    " --universal"
    " {snakemake.input[1]} {snakemake.input[2]} {log} || touch {snakemake.output[0]})"
)
