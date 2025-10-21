# Ask the user to write a text.
my_text = input("Write a text: ")

# Ask for the start index and Change text to a number.
start_index = int(input("Write the start index: "))

# Ask for the stop index and Change text to a number.
stop_index = int(input("Write the stop index: "))

# Get the part of the text from start to stop.
new_text = my_text[start_index:stop_index]

# Print the new part of the text.
print("The new text is:", new_text)
