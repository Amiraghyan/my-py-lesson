# Make a function to count characters.
def count_characters(input_text):

    # A text with all the vowels.
    vowels = "AEIOUY"
    # A text with all the consonants.
    consonants = "BCDFGHJKLMNPQRSTVWXZ"

    # Make a counter for vowels, start with 0.
    vowel_count = 0
    # Make a counter for consonants, start with 0.
    consonant_count = 0
    # Make a counter for other symbols, start with 0.
    symbol_count = 0

    # Look at each character in the input text.
    for char in input_text:
        # Make the character uppercase to check it.
        upper_char = char.upper()

        # Check if the character is in our vowels text.
        if upper_char in vowels:
            # If yes, add 1 to the vowel counter.
            vowel_count += 1
        # If not, check if it is in our consonants text.
        elif upper_char in consonants:
            # If yes, add 1 to the consonant counter.
            consonant_count += 1
        # If it is not a vowel or a consonant.
        else:
            # Add 1 to the symbol counter.
            symbol_count += 1

    # Return a dictionary with all the counts.
    return {
        "vowels": vowel_count,
        "consonants": consonant_count,
        "symbols": symbol_count,
    }


# This is the text we will check.
my_text = "Hello! I'm study "
# Call the function to get the counts.
result_counts = count_characters(my_text)

# Print the final results.
print("Vowels found:", result_counts["vowels"])
print("Consonants found:", result_counts["consonants"])
print("Symbols found:", result_counts["symbols"])
