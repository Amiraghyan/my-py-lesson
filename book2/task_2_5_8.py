# Ask the user to write numbers.
user_input = input("Write numbers with a space: ")
# Make a list of strings from the user's text.
my_list = user_input.split()

# Make a new empty list to hold the positive numbers.
positive_numbers_list = []

# Look at every item in the list.
for item in my_list:
    # Change the item from text to a number.
    number = int(item)

    # Check if the number is positive (bigger than 0).
    if number > 0:
        # If it is positive, add it to our new list.
        positive_numbers_list.append(number)

# Print the final list of positive numbers.
print("The positive numbers are:", positive_numbers_list)


# new_list = [elm for elm in list1 if elm > 0]
# print(new_list)
