__author__ = "Alexander Hübner"
__copyright__ = "Copyright 2022, Alexander Hübner"
__license__ = "MIT"

import os
import shutil

import pandas as pd
import pyfastx

metawrapdir = snakemake.params.get("metawrapdir", "")

if os.stat(snakemake.input[0]).st_size > 0:
    clusters = pd.read_csv(snakemake.input[0], sep=",")
    contig_lengths = {name: len(seq)
                    for name, seq in pyfastx.Fasta(snakemake.input[1], build_index=False)}
    clustered_contigs = set(clusters['contig_id'].tolist())

    for i in clusters['cluster_id']:
        contigs = set(clusters.loc[clusters['cluster_id'] == i, 'contig_id'].tolist())
        total_length = sum([contig_lengths[c] for c in contigs])
        if total_length >= 50000:
            with open(f"{metawrapdir}/bin.{i}.fa", "wt") as outfile:
                for name, seq in pyfastx.Fasta(snakemake.input[1], build_index=False):
                    if name in contigs:
                        outfile.write(f">{name}\n{seq}\n")
else:
    clustered_contigs = []

with open(f"{metawrapdir}/unbinned.fa", "wt") as outfile:
    for name, seq in pyfastx.Fasta(snakemake.input[1], build_index=False):
        if name not in clustered_contigs:
            outfile.write(f">{name}\n{seq}\n")

shutil.copy(snakemake.input[0],
            f"{metawrapdir}/{snakemake.wildcards.sample}-{snakemake.wildcards.assembler}.clustering.csv")
