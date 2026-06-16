import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🏇 Wagon System: Diagnostic Protocol")

WAGON_TICKERS = ["SPY", "QQQ", "IWM", "EEM", "GLD", "SLV", "TLT", "XLK"]
MACRO_TICKERS = {"S&P500": "^GSPC", "Nasdaq": "^NDX", "10Y Yield": "^TNX", "VIX": "^VIX"}

if st.button("הרצת פרוטוקול אבחון"):
    # 1. משיכת נתוני סוסים
    try:
        st.write("מושך נתוני סוסים...")
        data = yf.download(WAGON_TICKERS, period="1d")
        
        # ניקוי הנתונים - מוודא שאנחנו עובדים עם מחיר סגירה בלבד
        if 'Close' in data.columns:
            df = data['Close'].transpose()
            df.columns = ['מחיר נוכחי']
            st.subheader("מצב הסוסים")
            st.table(df)
        else:
            st.write("נתונים גולמיים:", data) # נראה מה הוא מחזיר אם 'Close' לא קיים
            
        # 2. משיכת נתוני מאקרו
        st.write("מושך נתוני מאקרו...")
        macro_raw = yf.download(list(MACRO_TICKERS.values()), period="1d")
        if 'Close' in macro_raw.columns:
            macro_df = macro_raw['Close'].transpose()
            macro_df.index = MACRO_TICKERS.keys()
            macro_df.columns = ['ערך']
            st.subheader("מדדי מאקרו")
            st.table(macro_df)

    except Exception as e:
        st.error(f"שגיאה בהרצת הפרוטוקול: {e}")
