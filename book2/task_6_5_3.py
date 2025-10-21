# The original dictionaries.
first_dictionary = {"a": 1, "b": 2, "c": 3}
second_dictionary = {"d": 4, "e": 5, "a": 99}


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # Start by creating a copy of the first dictionary.
    merged_dict = dict1.copy()

    # loop through the second dictionary and add each key-value pair
    # to our new dictionary.
    # If a key already exists, its value will be updated.
    for key, value in dict2.items():
        merged_dict[key] = value

    # Return merged dictionary.
    return merged_dict


# Call the function with our two dictionaries.
final_dictionary = merge_dictionaries(first_dictionary, second_dictionary)

# Output
print("First dictionary:", first_dictionary)
print("Second dictionary:", second_dictionary)
print("Merged dictionary:", final_dictionary)
