
import pandas as pd
import warnings; 
warnings.simplefilter('ignore')

#Yahoo Finance API´s
import yahoo_fin.stock_info as yf
tickers = yf.tickers_sp500()

# Prophet
from prophet import Prophet
from prophet.plot import plot_plotly
#Darts
from darts import TimeSeries
from darts.models import ExponentialSmoothing

# Interactive plots

import time
import datetime

# Functions to work with in this project:
stock = yf.get_data("TSLA", start_date = '01/01/1999', end_date = None, index_as_date = True, interval = "1d")
stock["date"] = pd.to_datetime(stock.index)
stock.reset_index(inplace=True)
stock_data = stock[["close",  "date"]]
stock_data.columns = ['y', 'ds']

series = TimeSeries.from_dataframe(stock_data,  "ds", "y")
print(series)








          




    

    

