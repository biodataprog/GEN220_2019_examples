#!/usr/bin/env python3
import os
gffurl="https://fungidb.org/common/downloads/release-45/ScerevisiaeS288c/gff/data/FungiDB-45_ScerevisiaeS288c.gff"
in_file = os.path.basename(gffurl)

if not os.path.exists(in_file):
    os.system("curl -O "+gffurl)

from BCBio import GFF
limit_info = dict(
        gff_id = ["BK006934"],
        gff_type = ["CDS"],
        gff_source = ["EuPathDB"])

in_handle = open(in_file)
for rec in GFF.parse(in_handle, limit_info=limit_info):
    for feat in rec.features:
        print(feat)
        break
in_handle.close()

in_handle = open(in_file)
for rec in GFF.parse(in_handle):
    for feat in rec.features:
        print(feat)
        break
in_handle.close()

