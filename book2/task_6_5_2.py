# The original dictionary mapping words to a list of their positions.
word_positions_dict = {"The": [0, 1], "best": [2, 3, 4]}

# This list will store the final combined lists.
combined_list = []

# Iterate through each key-value pair in the dictionary.
for word, positions in word_positions_dict.items():

    # Create a new, temporary empty list for each item.
    temp_list = []

    # Add the key (the word) to this temporary list.
    temp_list.append(word)

    # Add all the elements from the value list (the positions)
    temp_list.extend(positions)

    # Add the fully constructed temporary list to our final list.
    combined_list.append(temp_list)


# output

print("Original dictionary:", word_positions_dict)
print("Converted list of lists:", combined_list)
