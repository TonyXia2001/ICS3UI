'''
Tony(Tanglin) Xia
4/9/2018
DayoftheWeek.py
takes user input in the form of YYYY-MM-DD, returns what day it is in a week
'''

from datetime import date
def main():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                "Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    input = takeInput()
    try:
        theDate = date(input["year"], input["month"], input["date"])
    except ValueError:
        print(months[str(input["month"])] + " " + str(input["date"]) + ", " +
              str(input["year"]) + " is not a valid date.")
        return -1

    currentDate = date.today()
    if theDate < currentDate:
        be = " was a "
    elif theDate > currentDate:
        be = " will be a "
    elif theDate == currentDate:
        be = " is a "

    print(months[theDate.month] + " " + str(theDate.day) + ", " + str(theDate.year)
          + be + weekdays[theDate.weekday()])
    return 0

def takeInput():
    userInput = input("What's your date? ")
    while len(userInput) != 10 or userInput[4] != "-" or userInput[7] != "-":
        userInput = input("The date format needs to be YYYY-MM-DD. What's the date again?")
    userInput = userInput.split("-")

    while not (userInput[0].isdigit() and userInput[1].isdigit() and userInput[2].isdigit() and
               (1 <= int(userInput[1]) <= 12)):
        userInput = input("The date format needs to be YYYY-MM-DD. What's the date again?")
        userInput = userInput.split("-")

    return {"year": int(userInput[0]), "month": int(userInput[1]), "date": int(userInput[2])}

if __name__ == '__main__':
    main()
