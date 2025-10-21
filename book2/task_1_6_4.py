# Get the text from the user.
source_text = input("Write a text: ")

# replace argument (" ") to  ("").
text_without_spaces = source_text.replace(" ", "")


print(f"\nOriginal text: '{source_text}'")
print(f"Text without spaces: '{text_without_spaces}'")
