import streamlit as st
import yfinance as yf
import pandas as pd

# הגדרת ה-WAGON
WAGON_TICKERS = ["SPY", "QQQ", "IWM", "EEM", "GLD", "SLV", "TLT", "XLK"]

st.set_page_config(page_title="Wagon System", layout="wide")
st.title("🏇 Wagon System: Live Diagnostic")

if st.button("סרוק נתוני שוק"):
    data = yf.download(WAGON_TICKERS, period="1d", interval="1m")['Close'].iloc[-1]
    df = pd.DataFrame({'מחיר נוכחי': data})
    st.table(df)
