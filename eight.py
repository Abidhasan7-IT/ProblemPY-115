# String Reversal with Slicing: Write a Python 
# function to reverse a given string using slicing.

def reverse_string(s):
    return s[::-1]

string = str(input('Enter Text: '))
reversed_string = reverse_string(string)
print(reversed_string)  

