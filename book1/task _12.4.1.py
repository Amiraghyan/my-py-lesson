# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
user_number = int(user_input)

# Make a variable to hold the result, start with 1.
factorial_result = 1

# Check that the number is positive
if user_number < 0:
    print("Factorial does not exist for negative numbers.")
# elif user_number == 0:
#    factorial_result = 1
else:
    # Calculate the factorial using a loop
    for i in range(1, user_number + 1):
        factorial_result *= i

# Print the final result.
print("The factorial is:", factorial_result)
