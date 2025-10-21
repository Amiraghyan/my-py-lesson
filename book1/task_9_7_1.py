# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
number = int(user_input)

# Get the last two digits from the number.
# For example, 12345 becomes 45.
last_two_digits = number % 100

# From the last two digits, get the first one.
# For example, 45 becomes 4.
second_to_last_digit = last_two_digits // 10

# Print the final digit.
print("The second-to-last digit is:", second_to_last_digit)
