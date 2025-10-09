list1 = input("Write a numbers with a space:  ").split()

sum_list = 0


for el in list1:
    sum_list += int(el)

print(sum_list)