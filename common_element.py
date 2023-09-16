# Write a program that creates two lists of integers and then finds the common elements between those two lists. Print the common elements.
# Take input from the user for the first list
input_str1 = input("Enter elements for the first list separated by spaces: ")
list1 = [int(x) for x in input_str1.split()]

# Take input from the user for the second list
input_str2 = input("Enter elements for the second list separated by spaces: ")
list2 = [int(x) for x in input_str2.split()]
# Create two lists of integers
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)

# Find the common elements using set intersection
common_elements = set1.intersection(set2)

# Convert the result back to a list (if needed)
common_elements_list = list(common_elements)

# Print the common elements
print("Common elements:", common_elements_list)
