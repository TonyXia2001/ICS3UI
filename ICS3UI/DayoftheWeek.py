'''
Tony(Tanglin) Xia
4/9/2018
DayoftheWeek.py
takes user input in the form of YYYY-MM-DD, returns what day it is in a week
'''

from datetime import date
def main():
    weekdays = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday",
               "6": "Saturday", "7": "Sunday"}
    months = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May",
              "6": "June", "7": "July", "8": "August", "9": "September", "10": "October",
              "11": "November", "12": "December"}
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

    print(months[str(theDate.month)] + " " + str(theDate.day) + ", " + str(theDate.year)
          + be + weekdays[str(theDate.isoweekday())])
    return 0

def takeInput():
    userInput = input("What's your date? ")
    while len(userInput) != 10:
        userInput = input("The date format needs to be YYYY-MM-DD.")
    while userInput[4] != "-" or userInput[7] != "-":
        userInput = input("The date format needs to be YYYY-MM-DD.")
    year = userInput[:4]
    month = userInput[5:7]
    date = userInput[8:]

    while not (year.isdigit() and month.isdigit() and date.isdigit() and
               (1 <= int(month) <= 12)):
        userInput = input("The date format needs to be YYYY-MM-DD.")
        year = userInput[:4]
        month = userInput[5:7]
        date = userInput[8:]

    return {"year": int(year), "month": int(month), "date": int(date)}

if __name__ == '__main__':
    main()
