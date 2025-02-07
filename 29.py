# Reverse String: Write a Python program using a while loop to reverse a given string.

def reverse_string(s):
    reversed_str = ""
    i = len(s) 
    
    while i > 0:
        reversed_str += s[i-1]  
        i -= 1  
    return reversed_str

input_string = str(input("Enter your String: "))
reversed_string = reverse_string(input_string)
print("Reversed String:", reversed_string)
