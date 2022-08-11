from flask import Flask, render_template, request
from prog.stock_chart import *
from prog.stock_holiday import *
from prog.format_helper import *

stickyGraph = 0

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/stock/', methods=['POST'])
def stock():
    ticker = request.form['ticker']
    global stickyGraph 
    stickyGraph = save_chart(stock_chart(ticker),ticker)
    return render_template(
        'index.html',
        sticky = stickyGraph
        )

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
            sticky = stickyGraph,
            passDate = True
        )
    except:
        return render_template(
            'index.html',
            passDate = False,
            sticky = stickyGraph,
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
            sticky = stickyGraph,
            passDay = True
        )
    except:
        return render_template(
            'index.html',
            passDay = False,
            sticky = stickyGraph,
            error = "Check for appropriate inputs and try again"
        )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()