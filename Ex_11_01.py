import re

test_file = open('regex_sum_1457348.txt')
count = 0
result = 0
number = list()
for line in test_file:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if y == []:
        continue
    for n in y:
        result = result + int(n)

print(result )
# for n in number:
#    n = int(n)
#    result = result + n
# print(count, result)
