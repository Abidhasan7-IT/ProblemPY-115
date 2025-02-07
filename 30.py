# Nested Loops: 30. Multiplication Table: Write a Python program using nested loops to print 
# the multiplication table from 1 to 10.

def multiplication_table():  
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()
        
multiplication_table()  

