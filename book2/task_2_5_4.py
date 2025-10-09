list1 = input("Write a numbers with a space:  ").split()

list2 = []

for el in list1:
    list2.append(el)

print(list1 == list2)
print(list1 is list2)
