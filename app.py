import streamlit as st
import requests
import pandas as pd
import time
import plotly.express as px
import yfinance as yf

st.set_page_config(page_title="UK FinTech Dashboard", layout="wide", page_icon="🏦")

# Professional Sidebar - Showcasing your Napier & BCS Status
st.sidebar.title("💳 Portfolio Control")
st.sidebar.info(f"Developer: Abdullah Mohammed\nBCS Student Member | Napier Rep")
currency = st.sidebar.selectbox("Base Currency", ["GBP", "USD", "EUR"])

tab1, tab2, tab3 = st.tabs(["🪙 Crypto Tracker", "📈 UK Stock Watch", "🛡️ Compliance & Risk"])

def fetch_crypto(coins):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={currency.lower()}&include_24hr_change=true"
    return requests.get(url).json()

with tab1:
    st.header("Live Crypto Market")
    tracked_coins = ['bitcoin', 'ethereum', 'solana']
    data = fetch_crypto(tracked_coins)
    
    cols = st.columns(3)
    for i, coin in enumerate(tracked_coins):
        price = data[coin][currency.lower()]
        change = data[coin][f"{currency.lower()}_24h_change"]
        cols[i].metric(coin.capitalize(), f"{currency} {price:,.2f}", f"{change:.2f}%")

    # Interactive Chart using Plotly
    df = pd.DataFrame({'Asset': [c.capitalize() for c in tracked_coins], 
                       'Price': [data[c][currency.lower()] for c in tracked_coins]})
    st.plotly_chart(px.bar(df, x='Asset', y='Price', color='Asset', title="Real-time Price Comparison"), use_container_width=True)

with tab2:
    st.header("FTSE 100 & UK Market Watch")
    # Using yfinance to track actual UK Stocks (Matches your IEUK experience with Dyson/PwC)
    uk_stocks = ['RR.L', 'BP.L', 'VOD.L'] # Rolls Royce, BP, Vodafone
    stock_data = []
    
    for symbol in uk_stocks:
        ticker = yf.Ticker(symbol)
        price = ticker.fast_info['last_price']
        stock_data.append({"Ticker": symbol, "Price": round(price, 2)})
    
    st.table(pd.DataFrame(stock_data))
    st.info("Stock data is pulled via Yahoo Finance API - Demonstrating multi-API integration.")

with tab3:
    st.subheader("GDPR & Ethical AI Principles")
    st.write("This dashboard follows **Ethical AI principles** as studied at Edinburgh Napier[cite: 14, 68]. No user financial data is logged or stored, ensuring total data privacy.")