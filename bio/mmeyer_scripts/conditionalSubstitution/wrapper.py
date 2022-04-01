__author__ = "Alexander Hübner, Matthias Meyer"
__copyright__ = "Copyright 2022, Alexander Hübner, Matthias Meyer"
__license__ = "MIT"

import os

import pandas as pd

# Parse and merge the damageprofiler results requiring a conditional substitution
for fn in snakemake.input.cond_subst:
    if "3p" in os.path.basename(os.path.dirname(fn)):
        freq_3p = pd.read_csv(f"{os.path.dirname(fn)}/5p_freq_misincorporations.txt", sep="\t",
                              skiprows=3, usecols=[0, 1])
        freq_3p['Pos'] += 1
        freq_3p = pd.pivot_table(freq_3p.iloc[:1,:], columns=['Pos'], values=['C>T'])
    elif "5p" in os.path.basename(os.path.dirname(fn)):
        freq_5p = pd.read_csv(fn, sep="\t", skiprows=3, usecols=[0, 1])
        freq_5p['Pos'] += 1
        freq_5p['Pos'] *= (-1)
        freq_5p = pd.pivot_table(freq_5p.iloc[-1:,:], columns=['Pos'], values=['C>T'])

freq = pd.concat([freq_3p, freq_5p], axis=1)
freq.columns = ["condSubst_5p", "condSubst_3p"]

# Parse the damageprofiler results without requiring a conditional substitution
freq_5p_wo = pd.read_csv(f"{os.path.dirname(snakemake.input.wo_cond_subst)}/5p_freq_misincorporations.txt", sep="\t",
                         skiprows=3, usecols=[0, 1])
freq_5p_wo['Pos'] = (freq_5p_wo['Pos'] + 1) * (-1)
freq_3p_wo = pd.read_csv(f"{os.path.dirname(snakemake.input.wo_cond_subst)}/3p_freq_misincorporations.txt", sep="\t",
                         skiprows=3, usecols=[0, 1])
freq_3p_wo['Pos'] += 1
freq_wo = pd.concat([pd.pivot_table(freq_3p_wo.iloc[-1:,:], columns=['Pos'], values=['C>T']),
                     pd.pivot_table(freq_5p_wo.iloc[:1,:], columns=['Pos'], values=['C>T'])], axis=1) 
freq_wo.columns = ["all_3p", "all_5p"]

cont_estimate = pd.concat([freq, freq_wo], axis=1)
cont_estimate['cont_3p'] = 1 - cont_estimate['all_3p'] / cont_estimate['condSubst_3p']
cont_estimate['cont_5p'] = 1 - cont_estimate['all_5p'] / cont_estimate['condSubst_5p']
cont_estimate['mean_cont'] = cont_estimate[['cont_3p', 'cont_5p']].mean(axis=1)
cont_estimate['sample'] = snakemake.wildcards.sample
cont_estimate[['sample', 'all_5p', 'condSubst_5p', 'cont_5p',
               'all_3p', 'condSubst_3p', 'cont_3p', 'mean_cont']] \
    .to_csv(snakemake.output[0], sep="\t", index=False)
