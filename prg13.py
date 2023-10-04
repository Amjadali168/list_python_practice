# Write a program that creates a list of strings and then reverses the order of the strings in the list. Print the reversed list.

string_list = ["apple", "banana", "cherry", "date", "fig"]

reversed_list = string_list[::-1]

print("Reversed List:")
for item in reversed_list:
    print(item)
