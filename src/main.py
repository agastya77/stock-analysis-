from fetch_data import get_stock_data
from indicators import add_moving_averages, calculate_risk_return
from visualize import plot_stock ,plot_candlestick

symbol = input("Enter stock symbol: ").upper()
df = get_stock_data(symbol, "2015-01-01", "2024-01-01")
df = add_moving_averages(df)
df, volatility, annual_return = calculate_risk_return(df)

plot_stock(df, symbol)
plot_candlestick(df, symbol)