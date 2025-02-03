# Positive, Negative, or Zero: Write a Python program 
# that takes a number as input and prints whether it is positive, negative, or zero.

num= float(input("Enter a number: "))

if num > 0:
    print(num, "is positive.")

elif num < 0:
    print(num, "is negative.")
else:
    print(num, "is zero.")

