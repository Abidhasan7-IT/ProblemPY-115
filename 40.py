# List Manipulation: Given two lists of integers,
# write a Python program to create a new list that contains elements common to both lists.

list1 = [23, 1, 45, 12, 7, 89, 34]
list2 = [12, 7, 50, 89, 3, 34]

common_elements = [num for num in list1 if num in list2]

print("Common elements:", common_elements)
