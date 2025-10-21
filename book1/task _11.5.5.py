# Ask user for number for rows.
rows_input = input("Write number of rows: ")
# Change text to number.
rows = int(rows_input)

# Ask user for number for columns.
cols_input = input("Write number of columns: ")
# Change text to number.
cols = int(cols_input)


# full box
i = 0

# This loop is for rows.
while i < rows:
    # Print one line of stars.
    print("*" * cols)
    # Go to next row.
    i += 1


# empty box
i = 0

# This loop for rows.
while i < rows:
    # j is for counting columns.
    j = 0
    # This loop for columns.
    while j < cols:
        # if it is first row or last row
        # or if it is first column or last column
        # then print star.
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        # if not, print space.
        else:
            print(" ", end="")
        # Go to next column.
        j += 1
    # Finish row, go to new line.
    print()
    # Go to next row.
    i += 1


# This code make a triangle
i = 0

# This loop for rows.
while i < rows:
    # j is for counting stars in a row.
    j = 0
    # This loop print stars. More stars every time.
    while j <= i:
        print("*", end="")
        j += 1
    # New line for next row.
    print()
    # Go to next row.
    i += 1


# This code make triangle. on the right side
i = 0

# Loop for each row.
while i < rows:
    # This loop is for the spaces before stars.
    j = 0
    while j < (rows - 1) - i:
        print(" ", end="")
        j += 1

    # This loop is for the stars.
    k = 0
    while k < i + 1:
        print("*", end="")
        k += 1

    # New line.
    print()
    # Go to next row.
    i += 1


# This code make triangle. upside down
i = rows
# Loop while i_row is not 0.
while i > 0:
    # j is for printing stars.
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    # New line.
    print()
    # Make row number smaller.
    i -= 1


# This code make triangle. upside down . on the right
i = 0

# Loop for rows.
while i < rows:
    # This loop for spaces.
    j = 0
    while j < i:
        print(" ", end="")
        j += 1

    # This loop for stars.
    k = 0
    while k < rows - i:
        print("*", end="")
        k += 1

    # New line.
    print()
    # Go to next row.
    i += 1


# This is the big triangle. in middle
i = 0

# Loop for the rows.
while i < rows:
    # Loop for spaces to make triangle in middle.
    j = 0
    while j < (rows - 1) - i:
        print(" ", end="")
        j += 1

    # Loop to print stars.
    # Every time print 2 more stars.
    k = 0
    while k < 2 * i + 1:
        print("*", end="")
        k += 1

    # New line.
    print()
    # Go to next row.
    i += 1
