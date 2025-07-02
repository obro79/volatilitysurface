import numpy as np
import pandas as pd
import yfinance as yf


ticker = 'T'
data = yf.download(ticker, start='2020-01-01', end='2021-12-31')
print(data.head())

