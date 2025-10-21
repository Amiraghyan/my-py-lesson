# Import the 'dis' library. 'dis' helps us see the secret
# instructions that Python runs for our code.
import dis


# Make a simple function.
def my_function():
    # Inside the function, make a variable named 'my_age' and give it the value 30.
    my_age = 30
    return my_age


# --- Run the code ---

# Use the 'dis.dis()' function to look inside 'my_function'.
# It will show us the step-by-step instructions (bytecode) for that function.
print("--- Python's secret instructions for my_function ---")
dis.dis(my_function)
