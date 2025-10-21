# ------   HELPED   ------

# ask user for how many row
row = int(input("Write number of rows: "))

# this is big list for all of triangle
pascal_triangle = []

# this for is for make every row
for i in range(row):
    # this list is for the row i make now
    current_row = []

    # this for is for make numbers in the row
    for j in range(i + 1):
        # if it is first number or last number in row
        if j == 0 or j == i:
            # then number is 1
            current_row.append(1)
        else:
            # if not first or last number
            # i get the row that is before, the one up
            previous_row = pascal_triangle[i - 1]
            # the new number is sum of two numbers from the up row
            new_value = previous_row[j - 1] + previous_row[j]
            # i add my new number to the row i make now
            current_row.append(new_value)

    # i add the row i finished to my big triangle list
    pascal_triangle.append(current_row)

# this part is for print the triangle to look good
for i in range(row):
    # this for is for the spaces before the numbers
    for k in range(row - i - 1):
        # print one space and no new line
        print(" ", end="")

    # get the row from my big list that i want to print
    row_to_print = pascal_triangle[i]

    # for every number in this row
    for number in row_to_print:
        # print the number and a space, no new line
        print(number, end=" ")

    # after printing all numbers in row, go to new line for next row
    print()
