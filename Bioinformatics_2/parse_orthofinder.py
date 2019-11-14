#!/usr/bin/env python3

orthogroups = "Orthogroups.csv"

groups = {}
with open(orthogroups,"r") as ortho:
    firstline = next(ortho)
    header = firstline.strip().split("\t")
    print(header)
    for line in ortho:
        row = line.strip().split("\t")
        name = row[0]
        for i in range(1,len(row)):
            col = row[i]
            genes = col.split(", ")
#            print(genes)
            if name in groups:
                groups[name][i] = str(len(genes))
            else:
                groups[name] = [0,0,0,0]
                groups[name][i] = str(len(genes))

for group in groups:
    print(group, "\t".join(groups[group][1:4]))
