__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

from snakemake.shell import shell

minlength = snakemake.params.get("minlength", "")
outprefix = snakemake.params.get("outprefix", "")

with open(snakemake.input[1], "rt") as depthfile:
    for i, line in enumerate(depthfile):
        if i > 1:
            break
        else:
            pass

if i > 1:

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

else:

    shell(
        "(gunzip -c {snakemake.input[0]} "
        "  > {snakemake.output[0]})"
    )
