# Ask the user for the usage amount.
user_input = input("Enter your usage amount: ")

# Change the text to a whole number.
usage_amount = int(user_input)

# Check if the usage is less than 0.
if usage_amount < 0:
    # If it is, print an error message.
    print("Error: Usage cannot be negative.")
# If not, check if usage is 100 or less.
elif usage_amount <= 100:
    # The price is 0.
    price = 0
    # Print the price.
    print(price)
# If not, check if usage is 200 or less.
elif usage_amount <= 200:
    # Calculate the price for this case.
    price = 200 * (usage_amount - 100)
    # Print the price.
    print(price)
# If usage is more than 200.
else:
    # Calculate the price for the last case.
    price = 220 * (usage_amount - 200) + 200 * 100
    # Print the price.
    print(price)
