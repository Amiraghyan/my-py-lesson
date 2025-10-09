# ՕԳՆԵԼ ԵՆ

list1 = input("Write a numbers with a space:  ").split()
# list1 = ['ա', 'բ', 'գ', 'դ', 'ե', 'զ']

new_list = []

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        for k in range(j + 1, len(list1)):
            list2 = [list1[i], list1[j], list1[k]]
            new_list.append(list2)
    
print(new_list)


