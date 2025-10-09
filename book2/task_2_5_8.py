list1 = input("Write a numbers with a space:  ").split()

for el in list1:
    el = int(el)
    if el > 0:
        print(el, end = ", ")

# new_list = [elm for elm in list1 if elm > 0]
# print(new_list)