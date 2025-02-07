# For & While Loops: 20. Sum of N Numbers: Write a Python program using a for loop
# to calculate the sum of the first N natural numbers, where N is taken as input from the user.

N = int(input("Enter a number N: "))

sum = 0

for i in range(1, N+1):
    sum += i
print(f"ForLoop: The sum of the first {N} natural numbers is: {sum}")

sum_of_numbers = 0
a = 1

while a <= N:
    sum_of_numbers += a
    a += 1
print(f"WhileLoop: The sum of the first {N} natural numbers is: {sum_of_numbers}")

