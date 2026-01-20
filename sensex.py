import yfinance as yf
import pandas as pd

sensex = yf.download("^BSESN", start="2023-01-01", end="2024-01-01")
sensex.to_csv("sensex.csv")
print(sensex)
