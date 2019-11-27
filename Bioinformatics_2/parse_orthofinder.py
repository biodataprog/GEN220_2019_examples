#!/usr/bin/env python3
import csv

orthogroups = "Orthogroups.csv"

groups = {}
with open(orthogroups,"r") as ortho, open("Orthogroups_counts.tab","w") as ogout:
    rdr = csv.reader(ortho,delimiter="\t")
    wrt = csv.writer(ogout,delimiter="\t")
    header = next(rdr)
    header[0] = "FAMILY"
    wrt.writerow(header)
    for row in rdr:
        name = row[0]
        # initialize a row 0s -with as many cols as we need
        # its -1 because the first col in the row is the name
        # of the ortholog group
        groups[name] = [0] * (len(row)-1)
        for i in range(1,len(row)):
            col = row[i]
            genes = col.split(", ")
            groups[name][i-1] = 0
            for gene in genes:
                if len(gene):
                    groups[name][i-1] += 1

    wrt = csv.writer(ogout,delimiter="\t")
    for group in groups:
        row = [group]
        row.extend(groups[group])
        wrt.writerow(row)
