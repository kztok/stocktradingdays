from stock_holiday import *

def enter_date():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    return date(year,month,day)

#hey = enter_date()

for i in range(2019,2024):
    print(i+1)
    one = date(i,12,31)
    two = date(i+1,12,31)
    print("total: ")
    print(calculate_trading_days(one,two))

