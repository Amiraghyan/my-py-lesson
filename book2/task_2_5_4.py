# Ask the user to write some items.
user_input = input("Write some items with a space: ")
# Make a list from the user's text.
original_list = user_input.split()

# Make a new, empty list.
copied_list = []

# Look at every item in the original list.
for item in original_list:
    # Add the item to the new list.
    copied_list.append(item)

# Check the lists
print("Do the lists have the same items (==)?", original_list == copied_list)
print("Are the lists the same object (is)?", original_list is copied_list)
