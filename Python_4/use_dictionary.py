#!/usr/bin/env python3
from Bio import SeqIO
infile="/bigdata/gen220/shared/data/vector"
handle = open(infile, "rU")
record_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
print(record_dict.keys)
handle.close()
print(record_dict["gi|1052556|emb|Z50149.1|"]) #use any record ID
