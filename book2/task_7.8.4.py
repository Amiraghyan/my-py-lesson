# Make a function that calculates from a text.
def calculate(expression_text):
    # Split the text into a list of parts.
    parts = expression_text.split()

    # Get the first number from the list.
    opernad_one = int(parts[0])
    # Get the operator from the list.
    operator = parts[1]
    # Get the second number from the list.
    opernad_two = int(parts[2])

    # Check which operator was used.
    match operator:
        # If the operator is "+".
        case "+":
            return opernad_one + opernad_two
        # If the operator is "-".
        case "-":
            return opernad_one - opernad_two
        # If the operator is "*".
        case "*":
            return opernad_one * opernad_two
        # If the operator is "/".
        case "/":
            return opernad_one / opernad_two
        # If the operator is "**".
        case "**":
            return opernad_one**opernad_two
        # If the operator is "//".
        case "//":
            return opernad_one // opernad_two
        case _:
            print(f"Error: Unknown operator '{operator}'.")
            return None


# This is the text we want to calculate.
my_expression = "3 * 3"
# Call the function to get the result.
result = calculate(my_expression)

# Print the final result.
print("The result is:", result)
