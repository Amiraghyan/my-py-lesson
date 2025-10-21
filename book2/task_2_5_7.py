# Ask the user to write numbers.
user_input = input("Write numbers with a space: ")
# Make a list of strings from the user's text.
my_list = user_input.split()

# Make a new empty list to hold the even numbers.
even_numbers_list = []

# Look at every item in the list
for item in my_list:

    # Change the item from text to a number
    number = int(item)

    # Check if the number is even.
    if number % 2 == 0:
        even_numbers_list.append(number)


# Print even numbers.
print("The even numbers are:", even_numbers_list)
