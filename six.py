# Data Type Checker: Write a Python function that takes a variable
# as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).
# Function to check the data type of a variable
def datatype(var):
    return str(type(var)).split("'")[1]

var = input("Enter a value: ")

try:
    var = int(var)
except ValueError:
    try:
        var = float(var)
    except ValueError:

        pass

print("Data type:", datatype(var))



