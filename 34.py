#  Number Pyramid: Write a Python program 
# using nested loops to print a number pyramid like the following: 1 22 333 4444 55555

def pyramid():
    rows = 5
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end="")  
        print()

pyramid()

