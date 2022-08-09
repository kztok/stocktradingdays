
from prog.stock_holiday import *
from prog.format_helper import *
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as py



# print(date_format_conversion("2011-1-1"))

# one = date(2022,1,1)

# readable_date(one)

msft = yf.Ticker("MSFT")
wer = msft.history(period="2y")
# print(wer[["Low","High"]])
wer["Avg"] = round((wer["Low"] + wer["High"])/2,2)
asd = wer["Avg"]
# print(wer["Avg"][6])
# for i in range(20):
#     print(wer["Avg"][i])
# f = open("test.txt","w")
# f.write(str(asd))
# f.close()
# asd.to_csv('out.csv')
df = pd.read_csv('out.csv')
sh = py.line(x=df['Date'],y=df['Avg'])
sh.show()
# plt.plot(df['Date'],df['Avg'])
# plt.show()
