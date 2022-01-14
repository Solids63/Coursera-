name = input("Enter file:")
if len(name) < 1:
    name = "testtxt.txt"
count = 0
di = {}
mails = []
fh = open(name)
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    else:
        mails.append(wds[1])
        count += 1

big = -1
label = None
for w in mails:
    di[w] = di.get(w, 0) + 1

for k, v in di.items():
    if v > big:
        big = v
        label = k
print(label, big)
