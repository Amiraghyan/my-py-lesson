my_text = input("Write a text :  ")
n = int(input("Write a index to delete: "))


new_text = my_text.replace(my_text[n], "")

print(new_text)