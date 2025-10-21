# Ask the user to write a number.
user_input = input("Write a number: ")

# Make a variable for the new reversed string
reversed_str = ""


for char in user_input:
    reversed_str = char + reversed_str

# # we can make it a number
# reversed_number = int(reversed_str)


# Print the final reversed number.
print("The reversed number is:", reversed_str)
