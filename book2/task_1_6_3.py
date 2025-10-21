# Ask the user to write a text.
user_text = input("Write a text: ")

# Ask the user for an index to delete.
user_index_str = input("Write a index to delete: ")


# Change the index text to a number.
index_to_delete = int(user_index_str)

# Get the part of the text before the index.
first_part = user_text[:index_to_delete]

# Get the part of the text after the index.
second_part = user_text[index_to_delete + 1 :]

# Join the two parts together to make the new text.
new_text = first_part + second_part

# Print the new text.
print("The new text is:", new_text)
