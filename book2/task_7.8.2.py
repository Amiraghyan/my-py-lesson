def decimal_to_binary_string(decimal_number: int) -> str:
    # Input Validation
    if decimal_number < 0:
        return "Error: Function only accepts non-negative integers."

    # Handle the special case where the input is 0.
    if decimal_number == 0:
        return "0"

    # This variable will store the final binary string.
    binary_string = ""

    # The loop continues as long as there are digits left to process.
    while decimal_number > 0:
        # Get the remainder when divided by 2 (0 or 1).
        remainder = decimal_number % 2
        # Prepend the remainder to our result string.
        binary_string = str(remainder) + binary_string
        # Use integer division to prepare for the next iteration.
        decimal_number //= 2

    return binary_string


# Test the function.
original_number = 8
binary_representation = decimal_to_binary_string(original_number)
print(f"The binary representation of {original_number} is: '{binary_representation}'")

# Test with another number.
original_number = 42
binary_representation = decimal_to_binary_string(original_number)
print(f"The binary representation of {original_number} is: '{binary_representation}'")

# Test with an error case.
original_number = -5
error_message = decimal_to_binary_string(original_number)
print(f"Trying to convert {original_number}: {error_message}")
