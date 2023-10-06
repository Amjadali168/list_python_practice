# Write a program that uses the map function to create a new list that contains the squares of each element in a user inputted list of integers.
def square(x):
    return x ** 2

input_str = input("Enter a list of integers separated by spaces: ")
input_list = list(map(int, input_str.split()))
squared_list = list(map(square, input_list))

print("Squares of the input list:", squared_list)
