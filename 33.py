# Chessboard Pattern: Write a Python program using nested loops to print a chessboard pattern 
# (alternating “X” and “O” characters) of size 8×8.34.

def chessboard():
    size = 8
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

chessboard()
