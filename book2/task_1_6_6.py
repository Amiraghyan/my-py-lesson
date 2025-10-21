# ALL  VOWELS
VOWELS = "aeiou"

# User Input
source_text = input("Write a text: ").lower()

# Assume that no vowels have been found yet.
vowel_found = False

# Loop through each character of the user's text.
for character in source_text:
    # Check if the character is one of the vowels.
    if character in VOWELS:
        # If we find even one vowel, we set our flag to True
        # and immediately stop searching.
        vowel_found = True
        break

# Output
print(f"\nText: '{source_text}'")
print(f"Does the text contain any vowels? -> {vowel_found}")
