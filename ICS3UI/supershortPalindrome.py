'''
Alexander Wei
April 9, 2018
Palindrome
Checks to see if an input string is a palindrome.
'''
def palindrome(userinput):
    print(userinput, "is a palindrome.") if userinput.upper() == userinput.upper()[::-1] else print(userinput, "is not a palindrome.")
while True:
    userinput = input("Please enter a word to see if it is a palindrome: ")
    if userinput == "END": break
    palindrome(userinput)
