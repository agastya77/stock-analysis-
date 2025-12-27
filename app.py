import streamlit as st
from src.fetch_data import get_stock_data
from src.indicators import add_moving_averages
from src.visualize import plot_stock, plot_candlestick


st.title("📈 Stock Market Analysis Dashboard")

symbol = st.text_input("Enter Stock Symbol", "AAPL")
start = st.date_input("Start Date")
end = st.date_input("End Date")

if st.button("Analyze"):
    df = get_stock_data(symbol, start, end)
    df = add_moving_averages(df)
    st.line_chart(df[['Close','MA50','MA200']])
    st.write(df.tail())
