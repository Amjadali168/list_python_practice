# Write a program that creates a list of integers and then finds the index of a specific element in the list. Print the index.
integer_list = [5, 10, 15, 20, 25]
element_to_find = 15

if element_to_find in integer_list:
    index = integer_list.index(element_to_find)
    print(f"The index of {element_to_find} is {index}")
else:
    print(f"{element_to_find} is not in the list")
