import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime
import warnings

# Suppress warnings for clean output
warnings.filterwarnings("ignore")

# Title
st.title("📈 Bitcoin Price Predictor")

# Date range for historical data
start_date = "2020-01-01"
end_date = datetime.date.today().strftime("%Y-%m-%d")

# Download Bitcoin data
df = yf.download("BTC-USD", start=start_date, end=end_date, auto_adjust=False)

# Prepare data
df = df.reset_index()
df = df[['Date', 'Close']]  # Keep only Date & Close
df['Prediction'] = df[['Close']].shift(-1)  # Next day price

# Features (X) and Labels (y)
X = df[['Close']][:-1]  # All but last row
y = df['Prediction'][:-1]

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit input: user enters number of future days
days = st.number_input("Enter number of days to predict ahead:", min_value=1, max_value=30, value=1)

# Predict future prices
last_price = df[['Close']].iloc[-1].values[0]
future_price = last_price

for _ in range(days):
    future_price = model.predict(pd.DataFrame([[future_price]], columns=['Close']))[0]

# Show result
st.subheader(f"Predicted Bitcoin Closing Price after {days} day(s):")
st.success(f"${future_price:,.2f}")
