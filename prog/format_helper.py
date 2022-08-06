from datetime import date

# using date type in html
def date_format_conversion(original):
    numbers = list(map(int,original.split("-")))
    return date(numbers[0],numbers[1],numbers[2])

def readable_date(ymd):
    readable = ymd.strftime("%B") + " " + str(ymd.day) + ", " + str(ymd.year)
    return readable
