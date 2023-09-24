# Write a program that creates a list of integers and then finds the median value of the list. Print the median.
my_list = [5, 2, 9, 1, 7, 6, 4]
my_list.sort()
n = len(my_list)
if n % 2 == 1:
    median = my_list[n // 2]
else:
    middle1 = my_list[(n // 2) - 1]
    middle2 = my_list[n // 2]
    median = (middle1 + middle2) / 2
print("Median:", median)
