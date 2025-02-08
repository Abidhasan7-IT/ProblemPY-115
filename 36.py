# List Max and Min: Write a Python program to find the maximum and minimum values 
# in a given list of integers.

# Function to find the maximum and minimum values in a list
def find(n):
    if len(n) == 0:
        return 0, 0  
    max_value = max(n)
    min_value = min(n)
    return max_value, min_value

n = [60, 10, 30, 23, 50]
max_value, min_value = find(n)

print(f"The maximum value in the list is: {max_value}")
print(f"The minimum value in the list is: {min_value}")
