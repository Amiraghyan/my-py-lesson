my_text = input("Write a text :  ")

helf_len = len(my_text)//2

if my_text[:helf_len] == my_text[-1:helf_len:-1]:
    print(True)
else:
    print(False)