# Ask the user to write some items.
user_input = input("Write some items with a space: ")
# Make a list from the user's text.
my_list = user_input.split()

# Make a new empty list to hold the results.
combinations_list = []

# First loop for the first item's position.
for i in range(len(my_list)):
    # Second loop for the second item's position.
    # Start from i + 1 to not use the same item again.
    for j in range(i + 1, len(my_list)):
        # Third loop for the third item's position.
        # Start from j + 1 to not use the same item again.
        for k in range(j + 1, len(my_list)):
            # Make a small list with the three items from these positions.
            combination = [my_list[i], my_list[j], my_list[k]]
            # Add this small list to our big list of results.
            combinations_list.append(combination)

# Print the final list of all combinations.
print("All combinations of 3 are:", combinations_list)
