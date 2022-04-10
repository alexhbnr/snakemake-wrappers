__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"


from snakemake.shell import shell

minlength = snakemake.params.get("minlength", "")
outprefix = snakemake.params.get("outprefix", "")

shell(
    "(concoct "
    " -l {minlength}"
    " --coverage_file {snakemake.input[1]}"
    " --composition_file {snakemake.input[0]}"
    " -b {outprefix})"
)
