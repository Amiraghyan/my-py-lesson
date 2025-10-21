# This is our list with lists inside.
my_list = [[1, 2], [1, 2], [3, 4, 5]]

# Make a new empty LIST to hold the unique lists.
unique_list = []

# Look at every small list in our big list.
for item in my_list:
    # Check if the small list is already in our new list.
    if item not in unique_list:
        # If it is not, add it to the new list. This is easy to read.
        unique_list.append(item)

# change the list into a tuple.
result_tuple = tuple(unique_list)

# Print tuple.
print("The final tuple is:", result_tuple)
