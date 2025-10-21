# Make the sets.
first_set = {1, 2, 3}
second_set = {3, 4}


# Get the common items using the .intersection() method.
intersection_set = first_set.intersection(second_set)

# Another way to write this is:
# intersection_set = first_set & second_set

# Print the original sets.
print("The first set is:", first_set)
print("The second set is:", second_set)

# Print the final set with only the common items.
print("The common items are:", intersection_set)
