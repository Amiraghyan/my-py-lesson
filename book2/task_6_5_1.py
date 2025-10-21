# This is the text we start with.
data_string = "Jan = January; Feb = February; Mar = March"

# First, remove all spaces from the text.
# It becomes "Jan=January;Feb=February;Mar=March"
no_spaces_string = data_string.replace(" ", "")

# Then, split the text into a list using the ';'.
# It becomes ['Jan=January', 'Feb=February', 'Mar=March']
string_pairs = no_spaces_string.split(";")

# Make a new empty dictionary for the result.
result_dict = {}

# Look at each pair string in the list (like "Jan=January").
for pair_string in string_pairs:
    # Find the position of the "=" sign.
    equal_sign_index = pair_string.index("=")

    # Get the key (the part before the "=").
    key = pair_string[:equal_sign_index]

    # Get the value (the part after the "=").
    value = pair_string[equal_sign_index + 1 :]

    # Add the key and value to our dictionary.
    result_dict[key] = value

# Print the final dictionary.
print("The final dictionary is:", result_dict)
