from flask import Flask, render_template
from stock_holiday import *

# def enter_date():
#     year = int(input("Year: "))
#     month = int(input("Month: "))
#     day = int(input("Day: "))
#     return date(year,month,day)

# # for i in range(2019,2024):
# #     print(i+1)
# one = date(2022,5,1)
# two = date(2022,5,5)
# print("total: ")
# # print(calculate_trading_days(one,two))
# # print(calculate_future_stock_date(two,calculate_trading_days(one,two)))
# print(calculate_future_stock_date(two,58))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')