#!/usr/bin/python

# test strings with the gene name in them
gene1 = "Atchr12gene6"
gene2 = "Atchr3gene4"

match_length = len("chr")
print("substring length is ",match_length)

start_cut = gene1.find("chr")  + match_length


end_cut   = gene1.find("gene")

chrom     = gene1[start_cut:end_cut]

print "the chrom for", gene1, "is", chrom

start_cut = gene2.find("chr") + match_length
end_cut   = gene2.find("gene")

chrom     = gene2[start_cut:end_cut]

print("the chrom for",gene2,"is",chrom)
