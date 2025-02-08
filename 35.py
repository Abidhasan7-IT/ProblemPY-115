# List Average: Write a Python program to calculate the average of all elements 
# in a given list of integers.

def average(n):
    if len(n) == 0:
        return 0 
    return sum(n) / len(n)

n = [10, 20, 30, 40, 50]
average = average(n)

print(f"The average of the list is: {average}")
