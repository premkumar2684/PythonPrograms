#
# Example file for working with date information
#
from datetime import datetime
from datetime import date
from datetime import time




def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print(today)

  # print out the date's individual components
  print(today.day)
  print(today.month)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)

  print(today.weekday())
  days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  print(days[today.weekday()])
  ## DATETIME OBJECTS
  # Get today's date from the datetime class

 
  # Get the current time
  print((datetime.time(datetime.now())))
 

  
if __name__ == "__main__":
  main();
  