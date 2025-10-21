# Ask the user to write a number.
user_input = input("Enter a number: ")

# Change the text from the user into a whole number.
user_number = int(user_input)

# Make a copy of the number to check.
number_to_check = user_number

# Check if the number is negative (less than 0).
if number_to_check < 0:
    # If it is negative, make it positive.
    number_to_check = number_to_check * -1

# Get the last digit of the number.
last_digit = number_to_check % 10

# Check if the last digit can be divided by 3.
if last_digit % 3 == 0:
    # If yes, print this message.
    print("The last digit is divisible by 3.")
# If not.
else:
    # Print this other message.
    print("The last digit is not divisible by 3.")
