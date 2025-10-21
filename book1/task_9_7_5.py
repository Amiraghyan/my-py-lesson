# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
user_number = int(user_input)

# Make an empty text for the binary number.
binary_text = ""

# Check if the number is 0.
if user_number == 0:
    # If it is 0, the binary is "0".
    binary_text = "0"
# If the number is not 0.
else:
    # Keep looping as long as the number is bigger than 0.
    while user_number > 0:
        # Get the remainder when divided by 2.
        remainder = user_number % 2
        # Add the remainder to the beginning of our text.
        binary_text = str(remainder) + binary_text
        # Divide the number by 2 for the next loop.
        user_number //= 2

# Print the final binary text.
print("The binary is:", binary_text)
