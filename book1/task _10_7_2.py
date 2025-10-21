# Ask the user to write a number.
user_input = input("Enter a number: ")

# Change the text from the user into a whole number.
user_number = int(user_input)

# Check the remainder when the number is divided by 2.
if user_number % 2 == 0:
    # If the remainder is 0, the number is even.
    print("The number is even.")
# If the remainder is not 0.
else:
    # The number is odd.
    print("The number is odd.")
