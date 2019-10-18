#!/usr/bin/env python

filename="/bigdata/gen220/shared/simple/rice_random_exons.bed"
with open(filename,"r") as fh:
	exon_count = 0
	total_exon_length = 0
	for line in fh:
#		print(line)
		list = line.strip().split("\t")
#		print(list)
		start = int(list[1])
		end   = int(list[2])
		exonlen = end - start + 1
		exon_count += 1
		total_exon_length += exonlen
#		print(exonlen)
	print("There are",exon_count, "exons, and",total_exon_length,"coding bases")
