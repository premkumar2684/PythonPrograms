#
# Example file for working with Calendars
#

# import the calendar module
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# create a plain text calendar


# create an HTML formatted calendar


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
now=datetime.now()
#print(now.strftime("%d-%b-%Y %H:%M:%S"))
#print(now.strftime("%d-%b-%Y %h:%m:%S"))

print(date.today())
print(datetime.date(datetime.now()))

print(datetime(date.today()))

today=date.today()
bday=date(today.year,10,30)
diff=(bday-today).days
print(diff)
if diff>0:
  print("birthday in %d days" % diff)
else:
  print("Birthday in %d days" % (diff+365))



today=date.today()
print(today.weekday())
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])