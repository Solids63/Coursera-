import sys

digit_string = sys.argv[1]
n = 0
for i in digit_string:
    n = n + int(i)
print(n)

#  Решение от МФТИ
#  import sys


#  print(sum([int(x) for x in sys.argv[1]]))