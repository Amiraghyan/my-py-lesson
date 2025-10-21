# Get the main text from the user.
source_text = input("Write a text: ")
# Get the substring that we need to search for.
substring_to_find = input("Write the word/substring to count: ")

# how many times a substring appears in the main string.
occurrence_count = source_text.count(substring_to_find)


# Output
print("\n--- Results ---")
print(f"In the text '{source_text}',")
print(f"the substring '{substring_to_find}' appears {occurrence_count} times.")
