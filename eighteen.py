# Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic 
# equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.
# ax^2+bx+c=0

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The real roots are: {root1} and {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"The real root is: {root}")
else:
    real_part = -b / (2 * a)
    com_part = math.sqrt(-d) / (2 * a)
    print(f"The complex roots are: {real_part} + {com_part}i and {real_part} - {com_part}i")

