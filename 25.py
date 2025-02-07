# Sum of Even Numbers: Write a Python program using a while loop to calculate the sum 
# of all even numbers between 1 and N, where N is taken as input from the user.

N = int(input("Enter the value of N: "))

sum = 0
i = 2 

while i <= N:
    sum += i
    i += 2  
print(f"The sum of all even numbers between 1 and {N} is: {sum}")
