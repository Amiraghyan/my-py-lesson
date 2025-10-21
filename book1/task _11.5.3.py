# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
limit_number = int(user_input)

# Make a counter, start with 1.
counter = 1

# Keep looping as long as the counter is not bigger than the limit.
while counter <= limit_number:
    # Print the counter multiplied by 7.
    # end=" " prints a space instead of a new line.
    print(counter * 7, end=" ")
    # Add 1 to the counter.
    counter += 1
