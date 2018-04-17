'''
Tony(Tanglin) Xia
4/9/2018
Palindrome
take an input, detect whether it's a palindrome, return True or False
'''
def isPalindrome(userInput):
    tempList = list(userInput)
    for i in range(len(tempList)): tempList[i] = tempList[i].upper()
    if tempList == tempList[::-1]: return True
    else: return False
userInput = input("Please type in your word:")
while userInput.upper() != "END":
    Itis = isPalindrome(userInput)
    print(userInput + " is a palindrome") if Itis else print(userInput + " is not a palindrome")
    userInput = input("Please type in your word:")
