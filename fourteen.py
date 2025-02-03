# Grades Classification: Write a Python program that takes a student’s number as input and prints their corresponding grade
# according to the following criteria: – 
# 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

number = float(input("Enter the student Mark: "))

if number >= 90:
    grade = "A+"
elif number >= 80:
    grade = "A"
elif number >= 70:
    grade = "B"
elif number >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"The student grade is: {grade}")
