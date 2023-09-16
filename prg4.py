# Write a program that creates a list of integers and then finds the maximum value in the list. Print the maximum value.
list = []
n = int(input("Enter the number of elements: "))

for i in range(0, n):
    element = int(input("Enter an element: "))
    list.append(element)

max_num = max(list)
print("List:", list)
print("Maximum number:", max_num)