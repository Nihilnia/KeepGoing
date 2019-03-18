# DateTime module

from datetime import datetime

theDate = datetime.now()

#Now (Year, day, month, clock)
print("Year, day, month:", theDate)

#Only Year
print("Year:", theDate.year)

#Only Today
print("Day:", theDate.day)

#Only Month
print("Month:", theDate.month)

#Show as fancy
print(datetime.ctime(theDate))


# strftime() Function
"""
Year:   %Y
Month:  %B
Day(Name):    %A
Clock:  %X
Day:    %D
"""

print("Strftime:", datetime.strftime(theDate, "%D %A %B %Y"))

#Set datetime as your current location

import locale
locale.setlocale(locale.LC_ALL, "")

print("Strftime:", theDate.day, datetime.strftime(theDate, "%A %B %Y"))


# timestamp() and fromtimestamp()

asSeconds = datetime.timestamp(theDate)
print(asSeconds)

asDatetime = datetime.fromtimestamp(asSeconds)
print(asDatetime)


# LOOK AT THIS NOW :D

whereIsTheStart = datetime.fromtimestamp(0)
print(whereIsTheStart)

# Somethings between two dates.

future = datetime(2020, 4, 12)
now = datetime.now()

print("Remaining time:", future - now)