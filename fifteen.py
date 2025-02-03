# Vowel or Consonant: Write a Python program that takes a single character 
# as input and determines whether it is a vowel or a consonant.

char = input("Enter a character: ").lower()

if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("Please enter a valid alphabet character.")

