from pydoc import visiblename
import yfinance as yf
import pandas as pd
import plotly.express as py

def stock_chart(tick):
    return yf.Ticker(tick).history(period='2y')

def save_chart(check,tick):
    if not check.empty:
        sf = py.line(
            x=check.index, 
            y=round((check['Low'] + check['High'])/2,2), 
            title='<b>'+tick.upper()+'</b>', 
            labels={'x': 'Date', 'y': 'Price Avg'}
            )
        sf.update_layout(
            title_x=0.54,
            title_y=0.94,
            title_font_family="Roboto",
            title_font_size=18,
            margin={'t':50, 'r':30}
            )
        sf.update_yaxes(title=None)
        sf.update_xaxes(title=None)
        return sf.to_html(full_html=False)