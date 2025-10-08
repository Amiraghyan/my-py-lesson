my_text = input("Write a text :  ")

new_text = ""

for i in range(len(my_text)):
    if i%2 == 0:
        new_text += my_text[i]

print(new_text)