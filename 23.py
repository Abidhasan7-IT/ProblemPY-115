# Count Digits in a Number: Write a Python program using a while loop to count the number of digits
# in a given integer N.

N = int(input("Enter an integer N: "))

count = 0

while N != 0:
    N //= 10  
    count += 1  
print(f"The number of digits is: {count}")

