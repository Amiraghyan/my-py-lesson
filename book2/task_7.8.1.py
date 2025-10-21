def calculate_absolute_value(number):
    # Check if the number is less than zero.
    if number < 0:
        # If it is negative, flip its sign by multiplying by -1.
        return number * -1
    else:
        # If the number is zero or positive, return it unchanged.
        return number


# Define a number to test the function.
test_number = -6
absolute_result = calculate_absolute_value(test_number)
print(f"The absolute value of {test_number} is: {absolute_result}")

# Test with a positive number as well.
positive_test_number = 10
positive_absolute_result = calculate_absolute_value(positive_test_number)
print(f"The absolute value of {positive_test_number} is: {positive_absolute_result}")
