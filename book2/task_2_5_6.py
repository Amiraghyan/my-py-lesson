list1 = input("Write a numbers with a space:  ").split()

sum_list = 0
num_elem = 0

for el in list1:
    sum_list += int(el)
    num_elem +=1


# int(sum_list/num_elem)
print(sum_list, sum_list/num_elem)