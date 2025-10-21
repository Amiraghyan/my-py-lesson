# User Input
source_text = input("Write a text to check if it's a palindrome: ")


# Convert the entire string to lowercase.
processed_text = source_text.lower()

# Reversing with a Slice
reversed_text = processed_text[::-1]

# Compare the processed text with its reversed version.
if processed_text == reversed_text:
    is_palindrome = True
else:
    is_palindrome = False


# Output
print(f"Original text: '{source_text}'")
print(f"Is it a palindrome? -> {is_palindrome}")
