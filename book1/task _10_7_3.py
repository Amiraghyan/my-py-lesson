# Ask the user to write a number.
user_input = input("Enter a number: ")

# Change the text from the user into a whole number.
user_number = int(user_input)

# Check the remainder when the number is divided by 7.
if user_number % 7 == 0:
    # If the remainder is 0, the number is divisible by 7.
    print(f"The number {user_number} is divisible by 7.")
# If the remainder is not 0.
else:
    # The number is not divisible by 7.
    print(f"The number {user_number} is not divisible by 7.")
