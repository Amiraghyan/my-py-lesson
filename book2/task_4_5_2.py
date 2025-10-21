# Make the setս.
first_set = {1, 2, 3}
second_set = {3, 4}

# Print the first set before we change it.
print("The first set at the start:", first_set)

# Remove items from the first set that are also in the second set.
first_set.difference_update(second_set)

# Another way to write this is:
# first_set -= second_set

# Print the first set after it was changed.
print("The first set at the end:", first_set)
