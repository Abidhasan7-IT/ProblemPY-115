# Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci
# sequence up to a given limit N.
N = int(input("Enter the limit N for the Fibonacci sequence: "))

a, b = 0, 1

print("Fibonacci sequence up to", N, ":")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b 

