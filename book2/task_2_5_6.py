# Ask the user to write numbers.
user_input = input("Write numbers with a space: ")
# Make a list of strings from the user's text.
my_list = user_input.split()

# Make a variable for the sum, start with 0.
total_sum = 0

# Look at every item in the list.
for item in my_list:
    # Change the item from text to a integer and add to total sum.
    total_sum += int(item)

# Count how many items are in the list.
number_count = len(my_list)

# Calculate the average by dividing the sum by the count.
average = total_sum / number_count

# Print the final sum.
print("The sum is:", total_sum)
# Print the final average.
print("The average is:", average)
