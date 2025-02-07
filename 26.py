# Print Patterns: Write a Python program using nested for loops to print various patterns,
# such as a right-angled triangle, an inverted right-angled triangle, and so on.

rows = int(input("Enter the number of rows: "))

print("\n Right-angled Triangle:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  
    

print("\n Inverted Right-angled Triangle:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print() 
    
print("\n Pyramid Pattern:")
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ") 
    for k in range(2 * i - 1):
        print("*", end=" ")  
    print()

print("\n Inverted Pyramid Pattern:")
for i in range(rows ,0,-1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2*i- 1):
        print('*',end=" ")
    print()
    
print("\n Square Pattern:")
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()