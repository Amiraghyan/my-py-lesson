my_list = input("Write a numbers with a space:  ").split()

check_elm = input("Write element: ")

for elm in my_list:
    if elm == check_elm:
        print(True)
        break
else:
    print(False)