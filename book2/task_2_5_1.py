my_list = input("Write a numbers with a space:  ").split()

index1 = int(input("1 - Write index: "))
index2 = int(input("2 - Write index: "))

temp_index = my_list[index1]

my_list[index1] = my_list[index2]
my_list[index2] = temp_index

print(my_list)