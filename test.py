
from prog.stock_holiday import *
from prog.format_helper import *
from prog.stock_chart import *
import yfinance as yf
import pandas as pd
import plotly.express as py



# print(date_format_conversion("2011-1-1"))

# one = date(2022,1,1)

# readable_date(one)

input = "GME"
save_chart(stock_chart(input))



# print(wer[["Low","High"]])
# print(wer["Avg"][6])
# for i in range(20):
#     print(wer["Avg"][i])
# f = open("test.txt","w")
# f.write(str(asd))
# f.close()
# asd.to_csv('out.csv')
# df = pd.read_csv('out.csv')
# plt.plot(df['Date'],df['Avg'])
# plt.show()
