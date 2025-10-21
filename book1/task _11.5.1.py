# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
user_number = int(user_input)

# Make a variable to hold the result, start with 1.
factorial_result = 1


# Keep looping as long as the number is bigger than 0.
while user_number > 0:
    # Multiply the result by the current number.
    factorial_result *= user_number
    # Make the number smaller by 1.
    user_number -= 1

# Print the final result.
print("The factorial is:", factorial_result)
