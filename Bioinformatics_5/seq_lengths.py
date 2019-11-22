#!/usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.Seq import Seq
# seqfile
if len(sys.argv) != 2:
     print("argument should be\n","sequence_length.py FILE.fasta")
     exit()
filename = sys.argv[1]
print("%s\t%s"%("Name","Length"))
for seq_record in SeqIO.parse( filename , "fasta"):
    print("%s\t%d"%(seq_record.id,len(seq_record)))
