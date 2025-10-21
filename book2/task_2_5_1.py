# Ask the user to write some items.
user_input = input("Write some items with a space: ")
# Make a list from the user's text.
my_list = user_input.split()

# Ask for the first index.
index1_input = input("Write the first index: ")
# Change the first index text to a number.
index1 = int(index1_input)

# Ask for the second index.
index2_input = input("Write the second index: ")
# Change the second index text to a number.
index2 = int(index2_input)

# --- Swap the items ---

# Save the item from the first index in a temporary variable.
temp_item = my_list[index1]

# Put the item from the second index into the first index's place.
my_list[index1] = my_list[index2]

# Put the saved item into the second index's place.
my_list[index2] = temp_item

# Print the list after the swap.
print("The new list is:", my_list)
