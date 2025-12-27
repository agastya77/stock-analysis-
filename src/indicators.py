def add_moving_averages(df):
    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()
    return df

def calculate_risk_return(df):
    df['Daily Return'] = df['Close'].pct_change()

    volatility = df['Daily Return'].std()
    annual_return = df['Daily Return'].mean() * 252

    return df, volatility, annual_return

