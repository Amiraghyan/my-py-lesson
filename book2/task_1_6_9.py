# Ask the user to write a text.
user_text = input("Write a text: ")

# Make a counter for lowercase letters, start with 0.
lower_count = 0
# Make a counter for uppercase letters, start with 0.
upper_count = 0
# Make a counter for digits, start with 0.
digit_count = 0

# Look at each character in the user's text.
for char in user_text:
    # Check if the character is a digit (like '1', '2').
    if char.isdigit():
        # If it is a digit, add 1 to the digit counter.
        digit_count += 1
    # If not, check if the character is an uppercase letter.
    elif char.isupper():
        # If it is uppercase, add 1 to the uppercase counter.
        upper_count += 1
    # If not, check if the character is a lowercase letter.
    elif char.islower():
        # If it is lowercase, add 1 to the lowercase counter.
        lower_count += 1

# Print the final counts
print("Lowercase letters:", lower_count)
print("Uppercase letters:", upper_count)
print("Digits:", digit_count)
