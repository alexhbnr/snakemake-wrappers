__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

minlength = snakemake.params.get("minlength", "")
markerset = snakemake.params.get("markerset", "")
outprefix = snakemake.params.get("outprefix", "")

shell(
    "(run_MaxBin.pl "
    " -contig {snakemake.input[0]}"
    " -abund {snakemake.input[1]}"
    " -out {outprefix}"
    " -markerset {markerset}"
    " -min_contig_length {minlength}"
    " -thread {snakemake.threads}"
    " -verbose)"
)
