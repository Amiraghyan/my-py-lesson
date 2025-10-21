# Ask the user to write a text.
my_text = input("Write a text: ")

# This will be our new text with unique letters.
new_text = ""
# This text will remember the letters we have already seen.
seen_letters = ""

# Look at each character in the user's text.
for char in my_text:
    # Get the lowercase version of the character.
    lower_char = char.lower()

    # Check if we have seen this lowercase character before.
    if lower_char not in seen_letters:
        # If we have not seen it, add the original character to our new text.
        new_text = new_text + char
        # And remember that we have now seen this lowercase character.
        seen_letters = seen_letters + lower_char

# Print the final text.
print("The new text is:", new_text)
