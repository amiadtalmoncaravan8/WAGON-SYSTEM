import streamlit as st
import yfinance as yf
import pandas as pd

# הגדרת ה-WAGON והמאקרו
WAGON_TICKERS = ["SPY", "QQQ", "IWM", "EEM", "GLD", "SLV", "TLT", "XLK"]
MACRO_TICKERS = {"S&P500": "^GSPC", "Nasdaq": "^NDX", "VIX": "^VIX", "10Y Yield": "^TNX"}

st.set_page_config(page_title="Wagon System Pro", layout="wide")
st.title("🏇 Wagon System: Diagnostic Protocol")

if st.button("הרצת פרוטוקול אבחון"):
    # 1. נתוני התיק (הקראוון)
    data = yf.download(WAGON_TICKERS, period="1d", interval="1m")['Close'].iloc[-1]
    df = pd.DataFrame({'מחיר נוכחי': data})
    
    st.subheader("מצב הסוסים")
    st.table(df)
    
    # 2. נתוני מאקרו להשוואה
    st.subheader("מדדי מאקרו לאבחון")
    macro_data = yf.download(list(MACRO_TICKERS.values()), period="1d")['Close'].iloc[-1]
    macro_df = pd.DataFrame({'ערך': macro_data}, index=MACRO_TICKERS.keys())
    st.table(macro_df)
    
    st.success("פרוטוקול אבחון הושלם.")
