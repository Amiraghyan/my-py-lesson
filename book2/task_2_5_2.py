# Ask the user to write numbers.
user_input = input("Write numbers with a space: ")
# Make a list of strings from the user's text.
my_list = user_input.split()

# Change the first item in the list to a number.
# Let's guess that this is the biggest number for now.
max_number = int(my_list[0])

# Look at every item in the list.
for item in my_list:
    # Change the item from text to a number.
    number = int(item)

    # Check if this number is bigger than our biggest number.
    if number > max_number:
        # If it is bigger, it becomes the new biggest number.
        max_number = number

# Print the final biggest number.
print("The biggest number is:", max_number)
