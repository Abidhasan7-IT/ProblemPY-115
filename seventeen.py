# Triangle Type Checker: Write a Python program that takes three sides of a triangle 
# as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

side1 = float(input("Enter first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:

    if side1 == side2 == side3:
        print("Equilateral triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle.")
    else:
        print("Scalene triangle.")
else:
    print("The sides do not form valid triangle.")
