# Write a program that creates a list of strings and then sorts the list alphabetically. Print the sorted list.
list_alpha = []

n = int(input("Enter the number of alphabets: "))

for i in range(n):
    alpha = input("Enter an alphabet: ")
    list_alpha.append(alpha)

sorted_list = sorted(list_alpha)

print("Sorted list:", sorted_list)

