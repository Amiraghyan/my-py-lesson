# Ask user for number for rows.
rows_input = input("Write number of rows: ")
# Change text to number.
rows = int(rows_input)

# Ask user for number for columns.
cols_input = input("Write number of columns: ")
# Change text to number.
cols = int(cols_input)


# full box
# This loop is for rows.
for i in range(rows):
    # Print one line of stars.
    print("*" * cols)


# empty box
# This loop for rows.
for i in range(rows):
    # This loop for columns.
    for j in range(cols):
        # if it is first row or last row
        # or if it is first column or last column
        # then print star.
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        # if not, print space.
        else:
            print(" ", end="")
    # Finish row, go to new line.
    print()


# This code make a triangle
# This loop for rows.
for i in range(rows):
    # This loop print stars. More stars every time.
    for j in range(i + 1):
        print("*", end="")
    # New line for next row.
    print()


# This code make triangle. on the right side
# Loop for each row.
for i in range(rows):
    # This loop is for the spaces before stars.
    for j in range((rows - 1) - i):
        print(" ", end="")

    # This loop is for the stars.
    for k in range(i + 1):
        print("*", end="")

    # New line.
    print()


# This code make triangle. upside down
# Loop while i_row is not 0.
for i in range(rows, 0, -1):
    # j is for printing stars.
    for j in range(i):
        print("*", end="")
    # New line.
    print()


# This code make triangle. upside down . on the right
# Loop for rows.
for i in range(rows):
    # This loop for spaces.
    for j in range(i):
        print(" ", end="")

    # This loop for stars.
    for k in range(rows - i):
        print("*", end="")

    # New line.
    print()


# This is the triangle. in middle
# Loop for the rows.
for i in range(rows):
    # Loop for spaces to make triangle in middle.
    for j in range((rows - 1) - i):
        print(" ", end="")

    # Loop to print stars.
    # Every time print 2 more stars.
    for k in range(2 * i + 1):
        print("*", end="")

    # New line.
    print()
