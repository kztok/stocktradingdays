from calendar import c
from datetime import date, timedelta
from dateutil.easter import *

def find_delta(begin, end):
    delta = (end - begin).days
    return delta

# calculate holiday value out of 365 to make O(1)
def calculate_date_value(givenDate):
    return find_delta(date(givenDate.year,1,1),givenDate) + 1

def calculate_holidays_in_year(givenDate):
    holidays = [0]
    isSat = create_new_years(givenDate)

    if(isSat.weekday() != 5): holidays[0] = calculate_date_value(isSat)
    holidays.append(calculate_date_value(create_mlk_day(givenDate)))
    holidays.append(calculate_date_value(create_washington_bday(givenDate)))
    holidays.append(calculate_date_value(create_good_friday(givenDate)))
    holidays.append(calculate_date_value(create_memorial_day(givenDate)))
    holidays.append(calculate_date_value(create_juneteenth(givenDate)))
    holidays.append(calculate_date_value(create_independence_day(givenDate)))
    holidays.append(calculate_date_value(create_labor_day(givenDate)))
    holidays.append(calculate_date_value(create_thanksgiving(givenDate)))
    holidays.append(calculate_date_value(create_christmas(givenDate)))

    return holidays

# can refactor by making sub functions
# consider replacing baseYear date format to int
def create_new_years(baseYear):
    checkWeekend = date(baseYear.year,1,1).weekday()
    newDay = 1
    if(checkWeekend == 6):
        newDay += 1
    # if changing to class replace return with class creation
    # if saturday (5) no stock holiday
    return date(baseYear.year,1,newDay)

def create_mlk_day(baseYear):
    dayBasis = date(baseYear.year,1,1).weekday()
    firstMonday = 1
    while(dayBasis != 0):
        firstMonday += 1
        dayBasis = (dayBasis + 1) % 7
    return date(baseYear.year,1,firstMonday + 2*7)

# aka presidents day
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

def create_labor_day(baseYear):
    dayBasis = date(baseYear.year,9,1).weekday()
    firstMonday = 1
    while(dayBasis != 0):
        firstMonday += 1
        dayBasis = (dayBasis + 1) % 7
    return date(baseYear.year,9,firstMonday)

def create_thanksgiving(baseYear):
    dayBasis = date(baseYear.year,11,1).weekday()
    firstThursday = 1
    while(dayBasis != 3):
        firstThursday += 1
        dayBasis = (dayBasis + 1) % 7
    return date(baseYear.year,11,firstThursday + 3*7)

def create_christmas(baseYear):
    checkWeekend = date(baseYear.year,12,25).weekday()
    #if(checkWeekend == 5): return date(baseYear.year,12,24)
    #if(checkWeekend == 6): return date(baseYear.year,12,26)
    return date(baseYear.year,12,25)