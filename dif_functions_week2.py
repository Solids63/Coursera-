def get_multiplier():
    def inner(a, b):
        return a * b
    return inner

multiplier = get_multiplier()
print(multiplier(10, 11))

print(multiplier.__name__)


def get_multiplier(number):
    def inner(a):
        return a * number
    return inner

multiplier_by_2 = get_multiplier(2)
print(multiplier_by_2(10))

def squarify(a):
    return a ** 2

#  print(list(map(squarify, range(5))))

#  Тот же алгоритм в чистом питоне
squared_list = []

for number in range(5):
    squared_list.append(squarify(number))
print(squared_list)

def is_positive(a):
    return a > 0

print(list(filter(is_positive, range(-4, 5))))

#  тоже на чистом питоне
positive_list = []

for number in range(-4, 5):
    if is_positive(number):
        positive_list.append(number)
print(positive_list)


print(list(map(lambda x: x ** 2, range(5))))

print(type(lambda x: x ** 2))

print(list(filter(lambda x: x > 0, range(-4, 5))))


def num_to_string(a):
    return list(map(str, a))


print(num_to_string(range(20)))


from functools import reduce
from functools import partial

def multiply(a, b):
    return a * b

print(reduce(multiply, [1,2, 3, 4, 5, 6]))

print(reduce(lambda x, y: x * y, range(1, 7)))

def greeter(person, greeting):
    return '{}, {}!'.format(person, greeting)

hier = partial(greeter, greeting = 'Hi')
helloer = partial(greeter, greeting = 'Hello')

print(hier('Bob'))
print(helloer('Sir'))

square_list = []
for number in range(10):
    square_list.append(number ** 2)
print(square_list)


