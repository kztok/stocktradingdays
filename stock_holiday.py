from calendar import c
from datetime import date, timedelta
from venv import create
from dateutil.easter import *

#import holidays
#us = holidays.US()
#for ptr in holidays.US(years = 2022).items():
#    print(ptr)

# class Day:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

def create_new_years(baseYear):
    checkWeekend = date(baseYear.year,1,1).weekday()
    newDay = 1
    while(checkWeekend == 5 or checkWeekend == 6):
        newDay += 1
        checkWeekend += 1
    #if changing to class replace return with class creation
    return date(baseYear.year,1,newDay)

def create_mlk_day(baseYear):
    dayBasis = date(baseYear.year,1,1).weekday()
    firstMonday = 1
    while(dayBasis != 0):
        firstMonday += 1
        dayBasis = (dayBasis + 1) % 7
    return date(baseYear.year,1,firstMonday + 2*7)

def create_washington_bday(baseYear):
    dayBasis = date(baseYear.year,2,1).weekday()
    firstMonday = 1
    while(dayBasis != 0):
        firstMonday += 1
        dayBasis = (dayBasis + 1) % 7
    return date(baseYear.year,2,firstMonday + 2*7)

def create_good_friday(baseYear):
    return easter(baseYear.year) - timedelta(days = 2)

def create_memorial_day(baseYear):
    dayBasis = date(baseYear.year,5,31).weekday()
    lastMonday = 31
    while(dayBasis != 0):
        lastMonday -= 1
        dayBasis = (dayBasis - 1) % 7
    return date(baseYear.year,5,lastMonday)

def create_juneteenth(baseYear):
    checkWeekend = date(baseYear.year,6,19).weekday()
    if(checkWeekend == 5): return date(baseYear.year,6,18)
    if(checkWeekend == 6): return date(baseYear.year,6,20)
    return date(baseYear.year,6,19)

def create_independence_day(baseYear):
    checkWeekend = date(baseYear.year,7,4).weekday()
    if(checkWeekend == 5): return date(baseYear.year,7,3)
    if(checkWeekend == 6): return date(baseYear.year,7,5)
    return date(baseYear.year,7,4)

# print(easter(2024).day)
# print(create_new_years(date(2022,2,1)))
# print(create_mlk(date(2024,1,1)))
# print(create_washington_bday(date(2024,1,1)))

test = date(2022,1,1)
for i in range(3):
    # print(create_good_friday(test))
    # print (create_memorial_day(test))
    print(create_juneteenth(test))
    test += timedelta(days = 365)