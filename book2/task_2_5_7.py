list1 = input("Write a numbers with a space:  ").split()

for el in list1:
    el = int(el)
    if el%2 == 0:
        print(el, end = ", ")


# print()