# our project must have a main function and at least three other functions,
# each of which must be accompanied by tests that can be executed with pytest.

# get all ticker symbol
from stocksymbol import StockSymbol
api_key = '8a6ad6f5-0eeb-4a21-98bd-277e1d01f67d'
ss = StockSymbol(api_key)

# get ticker finance info
import yfinance as yf

# test if data follow normal distribution
# import scipy.stats as stats
from scipy.stats import shapiro

# Stand by to read the csv if needed
# import pandas as pd

def main():
    # get list of ticker
    symbols = get_symbol("FR")

    # request ticker info
    hist_clean = get_close_volume(symbols, "1y", "1d")

    # back-up the data
    hist_clean.to_csv("close_price_history.csv", index = True)

    # hist_clean = pd.read_csv("close_price_history.csv", header=[0, 1], index_col=[0])
    # hist_clean.drop(hist_clean.tail(1).index,inplace=True)

    # for column in hist_clean["Close"]:
    #     if hist_clean["Close"][column].isnull().values.any():
    #         hist_clean = hist_clean.drop(("Close", column), axis=1)

    # anlyse info
    symbole_normal = []
    for column in hist_clean["Close"]:
        if is_normal(hist_clean["Close"][column]):
            if is_profitable_5(hist_clean["Close"][column]):
                symbole_normal.append(column)
            # print(f"{column} SEEMS NORMAL")

    # print the result or better print result and anaylisis in a csv
    for stock in symbole_normal:
        print(f"the stock {stock} seems a good investment to achieve at least 5% return")

def is_normal(df):
    stat, p = shapiro(df)
    # print('Statistics=%.3f, p=%.3f' % (stat, p))
    alpha = 0.05
    if p > alpha:
        return True
    else:
        return False

def get_close_volume(list_symbols, duration, frequence):
    data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = list_symbols,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = duration,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = frequence,

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        # group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        # auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        # prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        # threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        # proxy = None
    )

    # remove unwanted info
    data =  data.drop(columns = ["Open", "High", "Low", "Adj Close", "Volume"])

    # Delete the last row
    data = data.drop(data.tail(1).index,inplace=False)

    # do not pass the value if column empty
    for column in data["Close"]:
        if data["Close"][column].isnull().values.any():
            data = data.drop(("Close", column), axis=1)

    return data

def get_symbol(mkt):
    symbol_list_us = ss.get_symbol_list(market=mkt)
    symbols = [stock["symbol"] for stock in symbol_list_us ]
    return " ".join(symbols)

def is_profitable_5(df):
    last = df.tail(1).item()
    mean = df.mean()
    if last < mean and (last*1.05) < mean:
        return True
    else:
        return False

if __name__ == "__main__":
    main()