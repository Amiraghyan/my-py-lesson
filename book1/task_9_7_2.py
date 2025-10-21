# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
user_number = int(user_input)

# Make a variable for the new reversed number, start with 0.
reversed_number = 0


# slicing
# reversed_number = user_number[::-1]

# Keep looping as long as the number is bigger than 0.
while user_number > 0:
    # Get the last digit of the number.
    last_digit = user_number % 10
    # Add the last digit to the end of our new number.
    reversed_number = (reversed_number * 10) + last_digit
    # Remove the last digit from the user's number.
    user_number //= 10

# Print the final reversed number.
print("The reversed number is:", reversed_number)
