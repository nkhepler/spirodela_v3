#used to appropriately reorder locus ID and counts from RNA-seq data that's been aligned to a transcriptome
#standard in from: samtools view input.bam | cut -f3 | sort | uniq -c | python count_reads.py > file.txt (last bit about python using this file now)

import fileinput
import sys

for line in fileinput.input():
	line = line.strip()
	line = line.split(" ")

	count = line[0]
	gene = line[1]

	print "%s\t%s" % (gene, count)

