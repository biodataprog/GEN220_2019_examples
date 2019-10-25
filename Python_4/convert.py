#!/usr/bin/env python3
from Bio import SeqIO

input_handle = open("cor6_6.gbk", "rt")
output_handle = open("cor6_6.fasta", "w")

sequences = SeqIO.parse(input_handle, "genbank")
count = SeqIO.write(sequences, output_handle, "fasta")

output_handle.close()
input_handle.close()
