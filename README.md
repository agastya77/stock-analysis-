

<h1>Stock Market Analysis & Visualization System</h1>

<p>
This is a Python-based project that fetches, analyzes, and visualizes historical stock market
data using real-time financial data APIs. The project is built using a modular architecture
and provides both command-line execution and an interactive web interface using Streamlit.
</p>

<h2>Features</h2>
<ul>
    <li>Fetches historical stock data using yFinance</li>
    <li>Visualizes stock prices using line charts</li>
    <li>Displays candlestick charts with volume</li>
    <li>Calculates technical indicators:
        <ul>
            <li>50-day Moving Average</li>
            <li>200-day Moving Average</li>
        </ul>
    </li>
    <li>Performs risk and return analysis:
        <ul>
            <li>Daily Returns</li>
            <li>Volatility</li>
            <li>Annualized Return</li>
        </ul>
    </li>
    <li>Interactive dashboard using Streamlit</li>
    <li>Stores fetched stock data in CSV format</li>
</ul>

<h2>Tech Stack</h2>
<ul>
    <li>Programming Language: Python</li>
    <li>Libraries: pandas, numpy, matplotlib, mplfinance, yfinance, streamlit</li>
    <li>IDE: Visual Studio Code</li>
</ul>

<h2>Project Structure</h2>
<pre>
stock-analysis/
│
├── app.py
├── requirements.txt
├── data/
│
├── src/
│   ├── __init__.py
│   ├── fetch_data.py
│   ├── indicators.py
│   ├── visualize.py
│   └── main.py
</pre>

<h2>Installation</h2>
<ol>
    <li>Clone the repository</li>
    <li>Navigate to the project directory</li>
    <li>Install dependencies using:
        <pre>python -m pip install -r requirements.txt</pre>
    </li>
</ol>

<h2>How to Run</h2>

<h3>Run as a Streamlit Web Application</h3>
<pre>python -m streamlit run app.py</pre>

<h3>Run from Command Line</h3>
<pre>python src/main.py</pre>

<h2>Sample Usage</h2>
<ul>
    <li>User enters a stock symbol (example: AAPL, TSLA, INFY)</li>
    <li>The system fetches historical data</li>
    <li>Indicators and risk metrics are calculated</li>
    <li>Charts are displayed</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li>Add machine learning-based price prediction</li>
    <li>Include technical indicators like RSI and MACD</li>
    <li>Deploy the application using Streamlit Cloud</li>
</ul>

<h2>Author</h2>
<p>
Agastya Singal<br>
B.Tech (2nd Year)<br>
Aspiring Software Engineer / Data Analyst
</p>
