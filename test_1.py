def add_dict(a, b):
 if a in d:
        x = d.get(a)
        x.append(b)
    else:
        d[a] = [b]
        print(d)
    return d


d = {'a': [1], 'b': [2], 'c': [3]}


key = input("Введите ключ словаря: ")
val = input("Введите значение ключа: ")

add_dict(key, val)

key = input("Введите ключ словаря: ")
val = input("Введите значение ключа: ")
add_dict(key, val)

key = input("Введите ключ словаря: ")
val = input("Введите значение ключа: ")
add_dict(key, val)

key = input("Введите ключ словаря: ")
val = input("Введите значение ключа: ")
add_dict(key, val)

print(d)
