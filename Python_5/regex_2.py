#!/usr/bin/env python3
import re
text=[ "ABC\t10..30",
       "ABC   30..40"]
for r in text:
    m = re.match(r'(\S+)\s+(\S+)',r)
    if m:
        print("\t".join([m.group(1),m.group(2)]))
