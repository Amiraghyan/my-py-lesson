def my_range(*args):
    # Argument Parsing
    num_args = len(args)
    start = 0
    step = 1

    if num_args == 1:
        stop = args[0]
    elif num_args == 2:
        start = args[0]
        stop = args[1]
    elif num_args == 3:
        start, stop, step = args
    else:
        # Raise a TypeError, which is more appropriate for wrong argument count.
        raise TypeError(f"my_range expected at most 3 arguments, got {num_args}")

    # Input Validation
    if step == 0:
        raise ValueError("my_range() arg 3 must not be zero")

    # Generation Logic
    current_value = start

    # For a positive step, we continue as long as the value is less than the stop.
    if step > 0:
        while current_value < stop:
            yield current_value
            current_value += step
    # For a negative step, we continue as long as the value is greater than the stop.
    else:  # step < 0
        while current_value > stop:
            yield current_value
            current_value += step


# Testing

print("--- Testing my_range(5) ---")
for element in my_range(5):
    print(element, end=" ")
print("\n")

print("--- Testing my_range(2, 8) ---")
for element in my_range(2, 8):
    print(element, end=" ")
print("\n")

print("--- Testing my_range(10, 1, -2) ---")
for element in my_range(10, 1, -2):
    print(element, end=" ")
print("\n")
