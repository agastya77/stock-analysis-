import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_stock(df, symbol):
    plt.figure(figsize=(10,6))
    plt.plot(df['Close'], label='Close')
    plt.plot(df['MA50'], label='50-Day MA')
    plt.plot(df['MA200'], label='200-Day MA')
    plt.title(f"{symbol} Stock Price with Moving Averages")
    plt.legend()
    plt.show()

def plot_candlestick(df, symbol):
    mpf.plot(
        df,
        type='candle',
        volume=True,
        style='yahoo',
        title=f"{symbol} Candlestick Chart",
        mav=(50, 200)
    )
