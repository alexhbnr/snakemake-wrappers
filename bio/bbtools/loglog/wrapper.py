__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

java_opts = get_java_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

n = len(snakemake.input.fastq)
assert n == 1 or n == 2, "Either one FastQ file (single-end) or two FastQ files (paired-end) are allowed as input."

if n == 1:  # single-end
    fqs = f"in={snakemake.input.fastq[0]}"
else: # paired-end
    fqs = f"in={snakemake.input.fastq[0]} in2={snakemake.input.fastq[1]}"

shell(
    f"(loglog.sh {java_opts} {fqs} {extra} {log} 2> {snakemake.output[0]})"
)
