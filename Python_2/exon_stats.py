#!/usr/bin/env python

filename="/bigdata/gen220/shared/simple/rice_random_exons.bed"
with open(filename,"r") as fh:
	for line in fh:
#		print(line)
		list = line.strip().split("\t")
#		print(list)
		start = int(list[1])
		end   = int(list[2])
		exonlen = end - start + 1
		print(exonlen)
#		break
