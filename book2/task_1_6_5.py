# All possible digit characters.
DIGITS = "0123456789"

source_text = input("Write a text: ")

# First, handle the edge case of an empty string.
if not source_text:
    print("Error: The text is empty and has no last character.")
else:
    # Get the last character of the string using negative indexing.
    last_character = source_text[-1]

    # Check if the last character is present in our string of digits.
    if last_character in DIGITS:
        result = True
    else:
        result = False

    print(f"\nOriginal text: '{source_text}'")
    print(f"The last character is: '{last_character}'")
    print(f"Is the last character a digit? -> {result}")
