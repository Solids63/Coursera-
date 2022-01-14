# Use the file name mbox-short.txt as the file name

def average(text):
    pos = text.find(':')
    number = text[pos+1:]
    val_str = number.lstrip()
    val_num = float(val_str)
    return val_num


fname = "testtxt.txt"
fh = open(fname)
count = 0
val = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        x = line.rstrip()
        val = average(x) + val
print(val/count)

