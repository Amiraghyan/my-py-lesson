# Ask the user to write a number.
user_input = input("Write a number: ")

# Change the text to a whole number.
limit_number = int(user_input)

# the loop will go from 1 to number entered(include),
# for every iteration  multiplying by 7
for i in range(1, limit_number + 1):
    print(i * 7, end=" ")
