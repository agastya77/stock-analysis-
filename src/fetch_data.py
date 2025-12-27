import yfinance as yf

def get_stock_data(symbol, start, end):
    stock = yf.Ticker(symbol)
    return stock.history(start=start, end=end)
