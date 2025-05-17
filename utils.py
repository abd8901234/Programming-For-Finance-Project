import streamlit as st
import pandas as pd
import yfinance as yf

# ----- Data loading utilities -----

def load_kaggle_data():
    st.markdown("#### Upload a Kaggle dataset (.csv)")
    file = st.file_uploader("Choose a CSV file", type="csv")
    if file:
        try:
            data = pd.read_csv(file)
            st.success("Kaggle data loaded successfully!")
            return data
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            return None
    return None

import streamlit as st
import yfinance as yf
import pandas as pd

def fetch_yahoo_data():
    st.markdown("#### Or fetch real-time Yahoo Finance data")
    ticker = st.text_input("Enter stock ticker (e.g., AAPL, GOOGL, TSLA)", "AAPL")
    period = st.selectbox("Select period", ["1mo", "3mo", "6mo", "1y", "5y"], index=2)
    fetch_btn = st.button("Fetch Data")
    
    # Use st.session_state to persist data
    if fetch_btn:
        try:
            data = yf.download(ticker, period=period)
            if data.empty:
                st.warning("No data found for this ticker/period.")
                st.session_state['fetched_data'] = None
                return None
            st.success(f"Data for {ticker} loaded!")
            st.session_state['fetched_data'] = data.reset_index()
            return st.session_state['fetched_data']
        except Exception as e:
            st.error(f"Failed to fetch Yahoo data: {e}")
            st.session_state['fetched_data'] = None
            return None
    elif 'fetched_data' in st.session_state and st.session_state['fetched_data'] is not None:
        return st.session_state['fetched_data']
    else:
        return None
# ----- THEMES: Custom CSS -----

def wallstreet_theme_style():
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(120deg, #2c3e50 0%, #bdc3c7 100%); }
    h2, h1, .css-10trblm { color: #13315C !important; font-family: 'Georgia', serif !important; }
    </style>
    """, unsafe_allow_html=True)

def retro_theme_style():
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #1a0033 0%, #ff00cc 100%); }
    h2, h1, .css-10trblm { color: #00ffe7 !important; font-family: 'Press Start 2P', monospace !important; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

def eco_theme_style():
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(120deg, #b7f8db 0%, #50a7c2 100%); }
    h2, h1, .css-10trblm { color: #145a32 !important; font-family: 'Trebuchet MS', Verdana, sans-serif !important; }
    </style>
    """, unsafe_allow_html=True)

def space_theme_style():
    st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at 60% 10%, #22223b 60%, #08001a 100%); }
    h2, h1, .css-10trblm { color: #fad744 !important; font-family: 'Orbitron', sans-serif !important; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
