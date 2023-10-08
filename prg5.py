# Write a program that creates a list of strings and then removes all elements that contain a specific substring. Print the final list.
string_list = ["apple", "banana", "cherry", "date", "grape"]

# Specify the substring to remove
substring_to_remove = "ap"

# Remove strings containing the specified substring
filtered_list = [s for s in string_list if substring_to_remove not in s]
print("Original list:", string_list)
print("List after removing strings with substring:", filtered_list)
