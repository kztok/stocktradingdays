from flask import Flask, render_template, request
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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result/', methods=['POST'])
def result():
    in1 = request.form['Start']
    in2 = request.form['End']
    result = float(in1) + float(in2)
    return render_template(
        'index.html',
        input1=in1,
        input2=in2,
        result=result
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()