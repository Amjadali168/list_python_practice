# Write a program that creates a list of integers and then removes all duplicates from the list. Print the final list.
# Create a list of integers with duplicates
integer_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Remove duplicates by converting the list to a set and back to a list
unique_list = list(set(integer_list))

# Print the final list without duplicates
print("Original list:", integer_list)
print("List after removing duplicates:", unique_list)
