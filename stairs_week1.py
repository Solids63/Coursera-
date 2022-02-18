import sys

digit_string = sys.argv[1]

stairs = int(digit_string)

for i in range(stairs):
    stair = (stairs - (i + 1))*' ' + ((i + 1) * '#')
    print(stair)


#  import sys

#  num_steps = int(sys.argv[1])

#  for i in range(num_steps):
#    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")