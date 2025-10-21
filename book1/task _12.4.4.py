# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
limit_number = int(user_input)

# Make a sum variable and counter, start with 0.
total_sum_of_odds = 0


#     Methood 1
# for i in range(1, limit_number + 1, 2):
#     total_sum += i

#  Method  2
for i in range(limit_number + 1):
    if i % 2 != 0:
        total_sum_of_odds += i


# Print the final sum.
print("The sum of odd numbers is:", total_sum_of_odds)
