square_list = []
for number in range(10):
    square_list.append(number ** 2)

print(square_list)

square_list = [number ** 2 for number in range(11)]
print(square_list)
num = [4, 6, 7, 9, 13]
print([number ** 2 for number in num])

even_list = []
for number in range(10):
    if number % 2 == 0:
        even_list.append(number)

print(even_list)
x = [4, 5, 6, 7, 8, 9, 10]
even_list = [num for num in x if num % 2 == 0]
print(even_list)

square_map = {number: number ** 2 for number in range(7)}
print(square_map)

reminder_set = {num % 10 for num in range(101)}
print(reminder_set)

print(type(number ** 2 for number in range(5)))

num_list = range(7)
squared_list = [x ** 2 for x in num_list]
print(list(zip(num_list, squared_list)))
