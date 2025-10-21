# Ask the user to write some items.
user_input = input("Write some items with a space: ")
# Make a list from the user's text.
my_list = user_input.split()

# Ask for the element to check.
element_to_check = input("Write element to check: ")


# Look at every item in the list.
for item in my_list:
    # Check if the current item is the one we are looking for.
    if item == element_to_check:
        # Stop the loop because we found what we needed.
        print(True)
        break
# If still not found, it will print False.
else:
    print(False)
