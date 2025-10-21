# Ask the user to write some items.
user_input = input("Write some items with a space: ")
# Make a list from the user's text.
my_list = user_input.split()

# Make a new empty list to hold the unique items.
unique_list = []

# Look at every item in the original list.
for item in my_list:
    # Check if the item is already in our new list.
    if item not in unique_list:
        # If it is not, add it to the new list.
        unique_list.append(item)

# Print the final list that has only the unique items.
print("The unique items are:", unique_list)
