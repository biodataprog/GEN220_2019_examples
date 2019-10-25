#!/usr/bin/env python3
from urllib.request import urlopen
from io import TextIOWrapper
from Bio import SeqIO
url="https://www.uniprot.org/uniprot/P10127.fasta"
handle = TextIOWrapper(urlopen(url))

sequences = SeqIO.parse(handle, "fasta")
for seq in sequences:
	print("seq is ",seq.id, " ", seq.seq)
