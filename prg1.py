# Write a program that creates an empty list and then asks the user to input integers to add to the list. Print the final list.
list = []
n = int(input("Enter the number of elements: "))

for i in range(0, n):
    element = int(input("Enter an element: "))
    list.append(element)

print("List:", list)


