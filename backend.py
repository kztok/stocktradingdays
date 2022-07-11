from datetime import date

def find_days(begin, end):
    delta = end - begin
    print(delta.days)

def enter_date():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    return date(year,month,day)


one = date(2020,7,5)
two = date(2020,7,7)


hey = enter_date()
find_days(hey,two)