#  def even_range(start, end):
#    current = start
#    while current < end:
#        yield current
#        current += 2


#  for number in even_range(2, 20):
#    print(number)

#  def list_generator(list_obj):
#    for item in list_obj:
#        yield item
#        print('After yielding {}'.format(item))

#  generator = list_generator([1, 2, 3, 4, 5, 6])

#  next(generator)
# next(generator)
#  next(generator)
#  next(generator)


#  def fibonacci(number):
#    a =b = 0, 1
#    for i in range(number):
#        yield a
#        a, b = b, a + b


#  for num in fibonacci(10):
#    print(num)

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value
    print(total, value)


generator = accumulator()