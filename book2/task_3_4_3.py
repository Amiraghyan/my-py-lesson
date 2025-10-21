# The list of tuples to be filtered.
list_of_tuples = [(6, 24, 36), (120, 12, 6), (12, 18, 21)]
# The number to check for divisibility.
DIVISOR = 6

# Make a new empty list for the results.
filtered_list = []

# Look at each tuple in the big list.
for current_tuple in list_of_tuples:
    # Look at each number inside the current tuple.
    for number in current_tuple:
        # Check if the number cannot be divided by K.
        if number % DIVISOR != 0:
            break
    else:
        # Add it to our result list.
        filtered_list.append(current_tuple)

# Print the final list.
print("The good tuples are:", filtered_list)
