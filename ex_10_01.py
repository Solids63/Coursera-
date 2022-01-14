name = input("Enter file:")
if len(name) < 1:
    name = "testtxt.txt"
count = 0
di = dict()
mails = []
fh = open(name)
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    else:
        mails.append(wds)

pr_list = []
for w in mails:
    h = w[5].split(':')
    pr_list.append(h[0])

for hour in pr_list:
    di[hour] = di.get(hour, 0) + 1
for k, v in sorted(di.items()):
    print(k, v)
