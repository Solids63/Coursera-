import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if (b**2 - 4*a*c) >= 0:
    root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print(int(root1))
    print(int(root2))
else:
    print("Корней нет")

#  d = b * b - 4 * a * c

#  x1 = (-b + math.sqrt(d)) / (2 * a)
#  x2 = (-b - math.sqrt(d)) / (2 * a)