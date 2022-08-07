from flask import Flask, render_template, request
from prog.stock_holiday import *
from prog.format_helper import *

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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/by_date/', methods=['POST'])
def by_date():
    in1 = date_format_conversion(request.form['Start'])
    in2 = date_format_conversion(request.form['End'])
    result = calculate_trading_days(in1,in2)
    in1 = readable_date(in1)
    in2 = readable_date(in2)
    return render_template(
        'index.html',
        input1=in1,
        input2=in2,
        result=result
    )

@app.route('/by_day/', methods=['POST'])
def by_day():
    return render_template(
        'index.html'
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()