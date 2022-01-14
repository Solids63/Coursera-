fname = 'testtxt.txt'
count = 0
fh = open(fname)
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    else:
        print(wds[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
