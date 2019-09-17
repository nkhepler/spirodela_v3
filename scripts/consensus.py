'''
Creates consensus sequence for individual blast loci captured using retrive.py.
Default settings: residue is considered consensus if appears in 30% (0.3) of sequences.
'''

import os
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align import AlignInfo
from Bio import AlignIO


### file names ###
file = '/Users/nathanhepler/Desktop/spipo manuscript/spipo_v3/scaffolds/SWLF01000119c'
out = '/Users/nathanhepler/Desktop/spipo manuscript/spipo_v3/scaffolds/alignments/SWLF01000119c'
filename = '/Users/nathanhepler/Desktop/spipo manuscript/spipo_v3/scaffolds/consensus/Consensus_SWLF01000119c.txt'
seqName = '>SWLF01000119c'


### setting path and aligning sequences ###
clustalw_exe = r"/Users/nathanhepler/Desktop/arabi manuscript/protein/clustalw-2.1/clustalw2"
clustalw_cline = ClustalwCommandline(clustalw_exe,
                                     infile=f"{file}.txt",
                                     outfile = f'{out}.aln')
assert os.path.isfile(clustalw_exe), "Clustal W exectuable missing"
stdout, stderr = clustalw_cline()

align_fasta = AlignIO.convert(f"{out}.aln", "clustal", f"{out}.fasta", "fasta")
alignment = AlignIO.read(f'{out}.fasta', 'fasta')


### creating consensus. ###
### default paramters: residue is consensus if appears in 0.3 proportion of seqs ###
summary_align = AlignInfo.SummaryInfo(alignment)
consensus = summary_align.dumb_consensus(0.2)


### output ###
with open(filename, 'w') as new:
    new.write(f'{seqName}\n{str(consensus)}')


