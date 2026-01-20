import yfinance as yf

ticker = '^NSEI'

print("Data download ho raha hai")

data = yf.download(ticker, period='100d', auto_adjust=True)

print("\nLast 100 Days Data:")
s = data[['Open','Close']]
print(s)