# Write a program that creates a list of integers and then finds the sum of all the even numbers in the list. Print the sum.
# list = [1,2,3,4,5,6,7,8]
# sum = 0
# for i in list:
#     if (i%2 == 0):
#         sum += i
# print(sum) 
list = int(input("enter number: "))
sum = 0
for i in range(1, list):
    if(i%2 == 0):
        sum += i
print(sum)