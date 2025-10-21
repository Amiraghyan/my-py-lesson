# Ask the user to write a number for a day.
user_input = input("Write a number for a day (1-7): ")

# Change the text to a whole number.
day_number = int(user_input)

# Check the number the user wrote.
match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        # Print an error message.
        print("Not a valid day.")
