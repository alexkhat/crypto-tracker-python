import streamlit as st
import requests
import pandas as pd
import time
import plotly.express as px

st.set_page_config(page_title="UK FinTech Dashboard", layout="wide")

# Professional Sidebar
st.sidebar.title("💳 Portfolio Settings")
st.sidebar.info("Developer: Abdullah Mohammed | BCS Member")
currency = st.sidebar.selectbox("Base Currency", ["GBP", "USD", "EUR"])

# App Tabs - Shows organized architecture
tab1, tab2, tab3 = st.tabs(["🪙 Crypto Tracker", "📈 Stock Watch", "🛡️ Risk Analysis"])

def fetch_data(coins):
    ids = ",".join(coins)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={currency.lower()}&include_24hr_change=true"
    return requests.get(url).json()

with tab1:
    st.header("Live Crypto Market")
    tracked_coins = ['bitcoin', 'ethereum', 'solana', 'cardano']
    data = fetch_data(tracked_coins)
    
    # Create dynamic columns for the top 4 coins
    cols = st.columns(4)
    for i, coin in enumerate(tracked_coins):
        price = data[coin][currency.lower()]
        change = data[coin][f"{currency.lower()}_24h_change"]
        cols[i].metric(coin.capitalize(), f"{currency} {price:,.2f}", f"{change:.2f}%")

    # Visualisation Section - Demonstrates Pandas/Plotly skills
    st.subheader("Market Performance Comparison")
    df = pd.DataFrame({
        'Asset': [c.capitalize() for c in tracked_coins],
        'Price': [data[c][currency.lower()] for c in tracked_coins]
    })
    fig = px.bar(df, x='Asset', y='Price', color='Asset', title="Current Price Comparison")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.warning("⚠️ Integration with London Stock Exchange (LSE) API is currently in development.")
    st.info("Check the GitHub Issues tab for progress updates on Stock tracking.")

with tab3:
    st.subheader("Security & Compliance")
    st.write("This application adheres to **GDPR principles** for data handling. No personal financial data is stored locally.")