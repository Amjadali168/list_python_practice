# Write a program that creates a list of integers and then asks the user to input an integer to check if it exists in the list. Print a message indicating whether the integer is in the list or not.
list = [1,2,3,4,5,6,7,8]
user_input = int(input("Enter the number you want to check: "))
if user_input in list:
    print("this number present in list", user_input)
else :
    print("this number is not present in list")