my_text = input("Write a text :  ").lower()

vowels = "aeiou"

for i in range(len(vowels)):
    if vowels[i] in my_text:
        print(False)
        break