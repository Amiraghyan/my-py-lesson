# User Input
my_text = input("Write a text: ")
reg_word = input("Write a pattern: ")


# We split the text into words to check each one individually.
words = my_text.split()

# This string will store the matching words.
new_text = ""

# Remove the '*' from the pattern to get the part we need to check.
# For example, if reg_word is "*book", clean_word becomes "book".
clean_word = reg_word.replace("*", "")

# Loop through each word in the user's text.
for word in words:
    # Check where the '*' is in the original pattern and apply the correct logic.
    if reg_word.startswith("*"):
        # If pattern is like "*book", check if the word ends with "book".
        if word.lower().endswith(clean_word.lower()):
            new_text += word + " "
    elif reg_word.endswith("*"):
        # If pattern is like "book*", check if the word starts with "book".
        if word.lower().startswith(clean_word.lower()):
            new_text += word + " "
    else:
        # If there is no '*', check for an exact match.
        if word.lower() == clean_word.lower():
            new_text += word + " "

# Output
print(new_text.strip())
