import numpy as np
import pandas as pd
import yfinance as yf


def download_option_data(ticker, type="call"):
    ticker = yf.Ticker(ticker)
    expiries = ticker.options
    expiry = expiries[0]
    opt_chain = ticker.option_chain(expiry)
    if type == "call":
        data = clean_data(opt_chain.calls)
    else:
        data = clean_data(opt_chain.puts)

    print(data.columns)
    print(data)
    print(data)
    return data


def clean_data(data):
    data = data.dropna()
    data = data.drop(columns=["contractSymbol", "lastPrice", "bid", "ask", "change", "percentChange", "volume", "openInterest", "inTheMoney", "contractSize", "currency"])
    data = data.reset_index(drop=True)
    return data

def save_data(data, filename):
    data.to_csv(filename)


def calculate_implied_volatility(underyling, type,dividend, spot_price, interest_rate):
    if type == "call":
        return data["impliedVolatility"]
    else:
        return data["impliedVolatility"] - 100

if __name__ == "__main__":
    data = download_option_data("T")
    save_data(data, "T.csv")

