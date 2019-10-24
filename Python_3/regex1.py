#!/usr/bin/env python
import re
m = re.search("((AB)+)C.{2}","BLAHABABABCDED")
if m:
    print("Group 0",m.group(0))
    print("Group 1",m.group(1))
    print("Group 2",m.group(2))
