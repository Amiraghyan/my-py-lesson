my_list = input("Write a numbers with a space:  ").split()

# print(max(my_list))

max_number = int(my_list[0])
for num in my_list:

    num = int(num)
    
    if num > max_number:
        max_number = num

print(max_number)