fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    lst = line + lst
lst.sort()
newlist = list()
for i in lst:
    if i not in newlist:
        newlist.append(i)
print(newlist)
