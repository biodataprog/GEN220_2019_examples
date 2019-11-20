#!/usr/bin/env python3
import re
from Bio import SeqIO

protein_file = "E_coli_K12.pep"
blast_file   = "Ecoli-vs-Senterica.BLASTP.tab"
seqlengths = {}

# teh BLAST headers
# http://www.pangloss.com/wiki/Blast


# this function returns just the accession number from a long
# sequence name like gi|1234|ref|YP_1234.1|
def clean_name(id):
    split_name = id
    if re.search(r'\|',id):
        split_name = id.split("|")
    return split_name[3]

with open(protein_file, "rU") as handle:
    for record in SeqIO.parse(handle, "fasta"):
#        print(record.id)
        seqlengths[record.id]  = len(record)
        # REMEMBER we could get the sequence in this record
        # like this:
        # record[22:712]
#        print(record.id,len(record))
#        break

print("there are %d sequences stored"%(len(seqlengths)))

print("\t".join(["QUERY","SUBJECT","PERCENT_ALIGNED","PERCENT_ID"]))
with open(blast_file,"r") as blast:
    for line in blast:
        row = line.strip().split("\t")
        qname           = row[0] # query name is in slot 0
        hname           = row[1] # hit/subject name
        percent_id      = row[2] # percent ID col
        query_aln_start = row[6] # query start align is in 6
        query_aln_end   = row[7] # ""        in slot 7
        query_aln_len = int(row[7]) - int(row[6]) + 1
        frac_query_aln = query_aln_len / seqlengths[qname]

#        print(row[0],row[10])
#        print(row)
        print("\t".join([clean_name(qname),clean_name(hname),
                         "%.2f"%(frac_query_aln * 100),
                         percent_id ]))
