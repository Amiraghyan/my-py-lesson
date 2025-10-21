# Define a constant for the maximum realistic age to make the code clearer.
MAX_REALISTIC_AGE = 120

# Ask the user to write their age.
user_input = input("Enter your age: ")

# Change the text from the user into a whole number.
user_age = int(user_input)


# If the age is realistic age
if user_age < 1 or user_age > MAX_REALISTIC_AGE:
    # If it is, print that the age is not real.
    print("This is not a real age.")
# Check if the age is 18 to MAX_REALISTIC_AGE.
elif user_age >= 18:
    # If it is, print that they can vote.
    print("You can vote.")
# If none of the above are true (meaning age is between 1 and 17).
else:
    # Print that they cannot vote yet.
    print("You cannot vote yet.")
