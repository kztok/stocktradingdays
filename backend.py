from datetime import date, timedelta

def find_delta(begin, end):
    delta = (end - begin).days
    return delta

def subtract_weekends(begin,end,total):
    weekdays = total - int(total/7) * 2
    #Check the remaining days (<7) from the end date for weekends.
    for i in range(total % 7):
        dayOfWeek = (end - timedelta(days = i)).weekday()
        if(dayOfWeek == 5 or dayOfWeek == 6):
            weekdays -= 1
    return weekdays

def enter_date():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    return date(year,month,day)


one = date(2020,7,5)
two = date(2022,7,10)


#hey = enter_date()
#total = find_delta(hey,two)
#subtract_weekends(hey,two,total)
