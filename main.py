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
    try:
        in1 = date_format_conversion(request.form['from1'])
        in2 = date_format_conversion(request.form['to'])
        inRange = True
        if in1 >= in2:
            inRange = False
        result = calculate_trading_days(in1,in2)
        resultDate = readable_date(calculate_future_stock_date(in2,result))
        in1 = readable_date(in1)
        in2 = readable_date(in2)
        return render_template(
            'index.html',
            input1 = in1,
            input2 = in2,
            resultTd = result,
            resultDate = resultDate,
            inRange = inRange,
            passDate = True
        )
    except:
        return render_template(
            'index.html',
            passDate = False,
            error = "Check for appropriate inputs and try again"
        )

@app.route('/by_day/', methods=['POST'])
def by_day():
    try:
        in3 = date_format_conversion(request.form['from2'])
        in4 = int(request.form['days'])
        result = readable_date(calculate_future_stock_date(in3,in4))
        in3 = readable_date(in3)
        return render_template(
            'index.html',
            input3 = in3,
            input4 = in4,
            resultDay = result,
            passDay = True
        )
    except:
        return render_template(
            'index.html',
            passDay = False,
            error = "Check for appropriate inputs and try again"
        )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()