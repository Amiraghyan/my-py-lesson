# Get the original text from the user.
source_text = input("Write a text: ")

# Slicing with a Step
# even_index_chars_text = source_text[::2]

# Make an empty text for the result.
even_index_chars_text = ""

# Loop through all the index numbers of the text.
for i in range(len(source_text)):
    # Check if the index number is even.
    if i % 2 == 0:
        # If the index is even, get the character at that index.
        char = source_text[i]
        # Add that character to our new text.
        even_index_chars_text += char

# Output
print(f"Original text: '{source_text}'")
print(f"Text with only even-indexed characters: '{even_index_chars_text}'")
