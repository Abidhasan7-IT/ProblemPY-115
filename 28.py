# List Manipulation: Given a list of integers, write a Python program using 
# a for loop to find the sum, average, maximum, and minimum values in the list.

list = [10, 2, 5, 8, 15, 3]

sum_value = 0
for i in range(len(list)):
    sum_value += list[i]

average = sum_value / len(list)

max_value = max(list)
min_value = min(list)

print(f"Sum: {sum_value} Average: {average} Max: {max_value} Min: {min_value}")

