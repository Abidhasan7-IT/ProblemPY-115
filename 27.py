# Prime Number Checker: Write a Python program using a while loop to check 
# if a given number N is prime or not.

def is_prime(N):
    if N <= 1:
        return False  
    
    i = 2
    while i < N:
        if N % i == 0:  
            return False  
        i += 1
    return True 

N = int(input("Enter a number: "))
if is_prime(N):
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")

