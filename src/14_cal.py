"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime as dt
args = sys.argv
# print(args)

now = dt.now()
MAX_YEAR = 10000
MIN_YEAR = 0

def print_calendar(month, year):
    '''Returns calendar for a given month and year'''
    c = calendar.TextCalendar(calendar.SUNDAY)
    str_cal = c.formatmonth(year, month)
    print ("\n",str_cal)

def month_check(month):
    if month > 12 or month < 1:
        return False
    else:
        return True

def year_check(year):
    if year > MAX_YEAR or year < MIN_YEAR:
        return False
    else:
        return True        

if len(args) == 2:
    month = int(args[1])
    year = now.year

elif len(args) == 3:
    month = int(args[1])
    year = int(args[2])

# calendar.TextCalendar.prmonth(theyear=year, themonth=month)
if month_check(month) == False:
    print('Invalid Month, select a month between 1 and 12.')
if year_check(year) == False:
    print(f'Invalid Year, select a year between {MIN_YEAR} and {MAX_YEAR}.')

if month_check(month) and year_check(year):
    print_calendar(month,year)