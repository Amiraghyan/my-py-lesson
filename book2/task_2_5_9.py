list1 = input("Write a numbers with a space:  ").split()

new_list = []

for el in list1:
    if el not in new_list:
        new_list.append(el)
        print(el, end = " ")