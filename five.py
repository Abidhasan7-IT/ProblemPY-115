# Temperature Converter: Write a Python program that converts a temperature 
# in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

def celsiusTofahrenheit(celsius):
    d=9/5
    return (celsius * d) + 32

celsius = float(input("Enter the temperature in Celsius: "))

F= celsiusTofahrenheit(celsius)

print(f"{celsius}°C is equal to {F}°F")
