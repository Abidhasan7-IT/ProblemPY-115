# Factorial Calculator: Write a Python program using a while loop to calculate the factorial 
# of a given number N.

N = int(input("Enter a number N: "))

factorial = 1
i = 1

while i <= N:
    factorial *= i
    i += 1

print(f"The factorial of {N} is: {factorial}")
