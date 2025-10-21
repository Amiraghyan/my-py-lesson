# This is the secret code we are looking for.
secret_code_text = "4581"
# Change the text code to a number.
secret_code_number = int(secret_code_text)

# Loop through all numbers from 0 to 9999.
# The step is 2, so it will check 0, 2, 4, 6, ...
for current_code in range(0, 10000, 2):
    # Print the code we are checking now.
    # :04 makes the number have 4 digits, like 0002.
    print(f"I am checking the code: {current_code:04}")

    # Check if the current code is the same as the secret code.
    if current_code == secret_code_number:
        # If we found it, print a message.
        print("I found the code! The code is", current_code)
        # Stop the loop because we are done.
        break
