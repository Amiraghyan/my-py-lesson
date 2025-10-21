# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
limit_number = int(user_input)

# Make a sum variable and counter, start with 0.
total_sum = 0
counter = 0

# Keep looping as long as the counter is not bigger than the limit.
while counter <= limit_number:
    # Check if the counter number is odd.
    if counter % 2 != 0:
        # If it is odd, add it to the sum.
        total_sum += counter
    # Add 1 to the counter for the next loop.
    counter += 1

# Print the final sum.
print("The sum of odd numbers is:", total_sum)
