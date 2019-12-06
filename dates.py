# Example of Date manipulation in python

from datetime import date
from datetime import time
from datetime import datetime

def main():

    today=date.today()
    print("Today's date is ", today)

    print("Date components: ", today.day, today.month, today.year)

    print("Today's weekday number is: ", today.weekday())
    days=["mon","tue","wed","thu","fri","sat","sun"]
    print("Which is a: ", days[today.weekday()])

    today2=datetime.now()
    print("The current date and time is ", today)

    t=datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main()
