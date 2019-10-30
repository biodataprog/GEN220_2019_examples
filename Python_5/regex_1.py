#!/usr/bin/env python3
import re

pat = re.compile(r'>([^\|]+)\|([^\|]+)\|gi\|(\d+)\s+GENE=(\S+)\s+DESC=\"([^\"]+)\"')
with open("sequences.fas","r") as fh:
    for line in fh:
        if line.startswith(">"):
            m = pat.match(line)
            print(line.strip())
            if m:
                species=m.group(1)
                acc    =m.group(2)
                gi     =m.group(3)
                gene   =m.group(4)
                Desc   =m.group(5)
                print("species   = ",species)
                print("accession = ",acc)
                print("gi.       = ",gi)
                print("Gene name = ",gene)
                print("Desc is.  = '{}'".format(Desc))
