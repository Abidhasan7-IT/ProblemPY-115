# String Palindrome: Write a Python function to check
# if a given string is a palindrome or not.

def ispalindrome(s):
    s = s.replace(" ", "").lower()
    # sos reverse sos theb palindrome
    return s == s[::-1]

string = str(input("Enter text: "))

if ispalindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
