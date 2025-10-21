# Make an empty list to hold the ages.
ages_list = []

# Ask for an age 4 times.
for i in range(4):
    # Get the age from the user.
    user_input = input("Write an age: ")
    # Change the text to a number.
    age = int(user_input)
    # Add the age to our list.
    ages_list.append(age)

# Guess that the first age in the list is the smallest.
smallest_age = ages_list[0]

# Check every age in the list.
for age in ages_list:
    # If the current age is smaller than our smallest guess.
    if age < smallest_age:
        # Then this age is the new smallest.
        smallest_age = age

# Print the final smallest age.
print("The smallest age is:", smallest_age)
