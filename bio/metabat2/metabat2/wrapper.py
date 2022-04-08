__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

minlength = snakemake.params.get("minlength", "")
outprefix = snakemake.params.get("outprefix", "")

shell(
    "(metabat2 "
    " -i {snakemake.input[0]}"
    " -o {outprefix}"
    " -a {snakemake.input[1]}"
    " --minContig {minlength}"
    " --minClsSize 100000"
    " -t {snakemake.threads}"
    " --unbinned"
    " --verbose)"
)
