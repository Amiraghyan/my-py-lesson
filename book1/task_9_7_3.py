# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
number = int(user_input)

# Get the first digit of the number.
first_digit = number // 100

# Get the last digit of the number.
last_digit = number % 10

# Check if the first and last digits are the same.
if first_digit == last_digit:
    # If they are the same, print True.
    print(True)
# If they are not the same.
else:
    # Print False.
    print(False)
