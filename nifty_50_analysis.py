import yfinance as yf
import pandas as pd

ticker = '^NSEI'

print("Data download ho raha hai")

data = yf.download(ticker, period='100d', auto_adjust=True)

print("\nLast 100 Days Data:")

nifty = data[['Open','Close']]
nifty= pd.DataFrame(nifty)
nifty.to_csv("open&close.csv")
print("data'open&close.csv' ban gayi hai")