import csv

datafile = 'species.csv'

genera = {}
with open(datafile,"r") as fh:
    reader = csv.reader(fh,delimiter=",")
    header = next(reader) # take the first line off
    for row in reader:
        key = row[1]
        if key == "": # skip an entry that is empty
            continue
        if key in genera:
            genera[key] += 1
        else:
            genera[key] = 1
for genus in genera:
    print(genus,genera[genus])
