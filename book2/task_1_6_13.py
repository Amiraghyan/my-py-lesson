my_text = input("Write a text:  ")

reg_word = input("write a regex: ")


my_text += " "
new_text = ""
temp_word = ""

for char in my_text:

    if char != " ":
        temp_word += char
    elif char == " ":
        if reg_word.lower() in temp_word.lower():
            new_text += temp_word + " "
        temp_word = ""

print(new_text)