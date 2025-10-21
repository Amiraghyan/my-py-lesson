# Make a function that reverses a number.
def reverse_number(number):

    # Make a variable for the new reversed number, start with 0.
    reversed_number = 0

    # Keep looping as long as the number is bigger than 0.
    while number > 0:
        # Get the last digit of the number.
        last_digit = number % 10
        # Add the last digit to the end of our new number.
        reversed_number = (reversed_number * 10) + last_digit
        # Remove the last digit from the number.
        number //= 10

    # Return the final reversed number.
    return reversed_number


# This is the number we want to reverse.
my_number = 15478965
# Call the function to get the reversed number.
result = reverse_number(my_number)

# Print the final result.
print("The reversed number is:", result)
