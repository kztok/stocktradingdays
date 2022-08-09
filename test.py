
from prog.stock_holiday import *
from prog.format_helper import *
import yfinance as yf
import matplotlib.pyplot as plt

# print(date_format_conversion("2011-1-1"))

# one = date(2022,1,1)

# readable_date(one)

msft = yf.Ticker("MSFT")
wer = msft.history(period="2d")
print(wer[""][0])
print(wer)