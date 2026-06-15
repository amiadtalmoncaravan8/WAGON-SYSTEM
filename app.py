import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🏇 Wagon System: Diagnostic Protocol")

# רשימת הטיקרים
WAGON_TICKERS = ["SPY", "QQQ", "IWM", "EEM", "GLD", "SLV", "TLT", "XLK"]
MACRO_TICKERS = {"S&P500": "^GSPC", "Nasdaq": "^NDX", "10Y Yield": "^TNX", "VIX": "^VIX"}

if st.button("הרצת פרוטוקול אבחון"):
    try:
        # משיכת נתונים עם תוקף של יום אחד
        data = yf.download(WAGON_TICKERS, period="1d")
        
        # בדיקה אם קיבלנו נתונים בכלל
        if not data.empty:
            # אם יש עמודת 'Close', ניקח אותה
            if 'Close' in data.columns:
                prices = data['Close'].iloc[-1]
            else:
                prices = data.iloc[-1]
                
            df = pd.DataFrame({'מחיר נוכחי': prices})
            st.subheader("מצב הסוסים")
            st.table(df)
        else:
            st.error("לא הצלחתי למשוך נתונים מ-Yahoo Finance. נסה שוב.")

        # משיכת נתוני מאקרו
        macro_raw = yf.download(list(MACRO_TICKERS.values()), period="1d")
        if not macro_raw.empty:
            macro_prices = macro_raw['Close'].iloc[-1] if 'Close' in macro_raw.columns else macro_raw.iloc[-1]
            macro_df = pd.DataFrame({'ערך': macro_prices}, index=MACRO_TICKERS.keys())
            st.subheader("מדדי מאקרו")
            st.table(macro_df)
            
    except Exception as e:
        st.error(f"שגיאה בהרצת הפרוטוקול: {e}")
else:
    st.info("לחץ על הכפתור כדי להתחיל את האבחון.")
