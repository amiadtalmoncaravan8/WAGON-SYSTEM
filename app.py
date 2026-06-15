import streamlit as st
import yfinance as yf
import pandas as pd

# הגדרת ה-WAGON והמאקרו
WAGON_TICKERS = ["SPY", "QQQ", "IWM", "EEM", "GLD", "SLV", "TLT", "XLK"]
MACRO_TICKERS = {"S&P500": "^GSPC", "Nasdaq": "^NDX", "VIX": "^VIX", "10Y Yield": "^TNX"}

st.set_page_config(page_title="Wagon System Pro", layout="wide")
st.title("🏇 Wagon System: Diagnostic Protocol")

if st.button("הרצת פרוטוקול אבחון"):
    # 1. נתוני התיק
    data = yf.download(WAGON_TICKERS, period="1d")['Close'].iloc[-1]
    df = pd.DataFrame({'מחיר נוכחי': data})
    st.subheader("מצב הסוסים")
    st.table(df)
    
    # 2. נתוני מאקרו - תיקון המשיכה
    st.subheader("מדדי מאקרו לאבחון")
    macro_list = list(MACRO_TICKERS.values())
    macro_data = yf.download(macro_list, period="1d")['Close'].iloc[-1]
    
    # יצירת טבלה תקינה
    macro_df = pd.DataFrame({'ערך': macro_data})
    st.table(macro_df)
    
    # 3. הכנה לניתוח Out-Riders
    st.subheader("דוח אבחון חריגות")
    # כאן בעתיד נשווה את תשואת התיק מול המדדים
    st.write("המערכת ממתינה להגדרת משקולות התיק כדי להתריע על ביצועי חסר.")
