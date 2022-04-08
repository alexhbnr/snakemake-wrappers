__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

minlength = snakemake.params.get("minlength", "")

shell(
    "(jgi_summarize_bam_contig_depths "
    " --outputDepth {snakemake.output[0]}"
    " --minContigDepth 1"
    " --minContigLength {minlength}"
    " {snakemake.input[0]})"
)
