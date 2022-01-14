largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        cifra = int(num)
    except:
        print('Invalid input')

    if smallest is None:
        smallest = cifra
    elif cifra < smallest:
        smallest = cifra
    if largest is None:
        largest = cifra
    elif cifra > largest:
        largest = cifra


print('Maximum is', largest)
print('Minimum is', smallest)
