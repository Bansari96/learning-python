# Example for working with timedelta objets and calendars in python

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main():

    # timedelta
    print(timedelta(days=365,hours=10, minutes=5))

    now=datetime.now()
    print("Today is: " + str(now))

    print("one year from now it will be: " + str(now + timedelta(days=365)))

    print("In 5 days and 2 weeks, it will be " + str(now + timedelta(days=5,weeks=2)))

    #Calculate 1 week ago
    t=datetime.now()-timedelta(weeks=1)
    s=t.strftime("%A %B %d, %Y")
    print("one week ago it was: "+s)

    #how many days until april fool's day
    today=date.today()
    afd=date(today.year, 4,1)

    if afd<today:
        print("April fool's day already went by %d days ago" % ((today-afd).days))
        afd=afd.replace(year=today.year+1)

    time_to_afd=afd-today
    print("Its just ",time_to_afd.days,"days until April fool's day")

    #calendars
    c=calendar.TextCalendar(calendar.SUNDAY) #Here calendars shows up as Sunday is the first day of the week
    st=c.formatmonth(2017,1,0,0)
    print(st)

    hc=calendar.HTMLCalendar(calendar.SUNDAY) # defines calendar in HTML format
    st=hc.formatmonth(2018,1)
    print(st)

    for i in c.itermonthdays(2017,5):
        print(i)

    for name in calendar.month_name:
        print(name)
    
    for days in calendar.day_name:
        print(days)

    print("Team meetings will be on: ")
    for m in range(1,13):
        cal=calendar.monthcalendar(2019, m)
        week1=cal[0]
        week2=cal[1]

        if week1[calendar.FRIDAY]!=0:
            meetday=week1[calendar.FRIDAY]
        else:
            meetday=week2[calendar.FRIDAY]

        print("%10s %2d" %(calendar.month_name[m],meetday))

if __name__ == "__main__":
    main()