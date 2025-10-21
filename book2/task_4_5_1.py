# Make the first set.
first_set = {1, 2, 3}
# Make the second set.
second_set = {3, 4}

# --- First Action: Update the first set ---

# Add all items from the second set into the first set.
# This changes the first_set.
first_set.update(second_set)

# Print the first set after it was changed.
print("First set after update:", first_set)


# # Make a new set by joining the two sets.
# new_set = first_set | second_set

# # Print the new set. The result will be the same.
# print("The new set is:", new_set)
