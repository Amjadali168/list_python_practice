# Write a program that creates a list of strings and then removes all whitespace characters from each string in the list. Print the final list.
string_list = ["Hello, World!", "This is a test", "   Remove spaces   ", "  Another   "]
cleaned_list = [s.replace(" ", "") for s in string_list]

print(cleaned_list)
