my_text = input("Write a text :  ")

new_string = ""

for char in my_text:
    if char.lower() not in new_string.lower():
        new_string += char

print(new_string)