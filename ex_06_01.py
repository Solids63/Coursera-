text = open('newtest.txt')
val = 0
for line in text:
    pos = line.find(':')
    print(pos)
    number = line[pos + 1:]
    print(number)
    val_str = number.lstrip()
    val_num = float(val_str)
    val = val + val_num
print('Resuming: ', val / 27)

