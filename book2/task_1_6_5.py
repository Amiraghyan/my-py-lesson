my_text = input("Write a text :  ")

last_char = my_text[-1]

if last_char.isdigit():
    print(True)
else:
    print(False)