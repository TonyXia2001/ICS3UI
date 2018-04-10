'''
Tony(Tanglin) Xia
4/9/2018
Palindrome
take an input, detect whether it's a palindrome, return True or False
'''
def main():
    userInput = input("Please type in your word:")
    isPalindrome(userInput)

def isPalindrome(userInput):
    tempList = list(userInput)
    for i in range(len(tempList)):
        tempList[i] = tempList[i].upper()
    tempList2 = list(tempList)
    tempList2.reverse()
    if tempList2 == tempList:
        print(userInput + " is a palindrome.")
    else:
        print(userInput + " is not a palindrome.")

if __name__ == '__main__':
    main()
