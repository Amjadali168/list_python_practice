# Write a program that creates a list of strings and then finds the longest string in the list. Print the longest string.
list = ['one', 'two', 'seventy eight', 'debug']
max_string = max(list, key = len)
print("The longest string is: ", max_string)