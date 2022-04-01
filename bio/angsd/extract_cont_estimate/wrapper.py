__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import re

extract_nsnps = re.compile(r"( )+We have nSNP sites: ([0-9]+), with flanking: ([0-9]+)\n")
extract_estimates = re.compile(r"Method[0-9]: new_llh Version: MoM:(-*[0-9\.]+) SE\(MoM\):([0-9\.e\-\+]+) ML:(-*[0-9\.]+) SE\(ML\):([0-9\.e\-\+]+)")

with open(snakemake.input[0], "rt") as logfile:
    log = logfile.readlines()

with open(snakemake.output[0], "wt") as outfile:
    outfile.write("sample\tnSNPs\tnFlankingSites\tmethod1_ML\t"
                  "method1_ML_SE\tmethod2_ML\tmethod2_ML_SE\n")
    if log[-1].startswith("Method2"):  # successful estimation
        _, nsnps, nflanking = extract_nsnps.search(log[-7]).groups()
        method1 = [float(e) for e in extract_estimates.search(log[-3]).groups()]
        method2 = [float(e) for e in extract_estimates.search(log[-1]).groups()]
        outfile.write(f"{snakemake.params.get('sample', '')}\t{nsnps}\t{nflanking}\t"
                    f"{method1[2]}\t{method1[3]:.6f}\t"
                    f"{method2[2]}\t{method2[3]:.6f}\n")
    else:  # seg fault
        _, nsnps, nflanking = extract_nsnps.search(log[-3]).groups()
        outfile.write(f"{snakemake.params.get('sample', '')}\t{nsnps}\t{nflanking}\t"
                      "NA\tNA\tNA\tNA\n")
