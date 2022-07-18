from stock_holiday import *

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
two = date(2024,7,10)


#hey = enter_date()
total = find_delta(one,two)
#subtract_weekends(hey,two,total)
print(total)

test = date(2022,1,1)
# for i in range(3):
#     # print(create_good_friday(test))
#     # print (create_memorial_day(test))
#     # print(create_juneteenth(test))
#     # print(create_labor_day(test))
#     # print(create_new_years(test))
#     # print(create_thanksgiving(test))
#     # print(create_christmas(test))
#     print(calculate_date_value(date(2022,1,1)))
#     test += timedelta(days = 365)

check = calculate_holidays_in_year(two)

for i in range(len(check)):
    print(check[i])