my_list = [(6,24,36),(120,12,6),(12,18,21)]
K = 6

filtered_list = []

for list_elem in my_list:
    for tuple_elem in list_elem:
        if tuple_elem%6 != 0:
            break
    else:
        filtered_list.append(list_elem)

print(filtered_list)