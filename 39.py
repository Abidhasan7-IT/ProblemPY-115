# List Reversal: Write a Python program to reverse a given list
# without using any built-in functions.
numbers = [23, 1, 45, 12, 7, 89, 34]

reversed_list = []
for num in numbers:
    reversed_list.insert(0, num)

print("Reversed list:", reversed_list)


