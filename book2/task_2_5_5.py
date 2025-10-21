# Ask the user to write numbers.
user_input = input("Write numbers with a space: ")
# Make a list of strings from the user's text.
my_list = user_input.split()

# Make a variable for the sum, start with 0.
total_sum = 0

# Look at every item in the list.
for item in my_list:
    # Change the item from text to a integer and add to total sum.
    total_sum += int(item)

# Print the final sum.
print("The total sum is:", total_sum)
