my_text = input("Write a text :  ")

lower = 0
upper = 0
digit = 0

for char in my_text:
    if char.isdigit():
        digit += 1
    elif char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print(lower,upper,digit, sep = ", ")