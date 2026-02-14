import streamlit as st
import requests
import pandas as pd
import time

# Page Configurtion  - Demonstrates UI/UX
st.set_page_config(page_title="UK Finanace Monitor", page_icon='📈')

st.title("🚀 UK Crypto & Finance Dashboard")
st.markdown(f"**Developer:** Abdullah Mohammed | **Status:** BCS Student Member**")


# Sidebar for user settings - matches "Information Systems" module logic
st.sidebar.header("Settings")
currency = st.sidebar.selectbox("Select Currency", ("GBP", "USD"))
update_interval = st.sidebar.slider("Update Interval (seconds)", 10,60,30)


def get_data(coin_id='bitcoin'):
    url=f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency.lower()}&include_24hr_change=true"
    try:
        response = requests.get(url)
        return response.json()[coin_id]
    except:
        return None
    
# Placeholder for live data
placeholder = st.empty()

# Real-time loop
while True:
    data = get_data()
    if data:
        with placeholder.container():
            # Displaying metrics - Industry standard for dashboards
            col1, col2 = st.columns(2)
            col1.metric("Bitcoin Price", f"{currency} {data[currency.lower()]:,.2f}")
            col2.metric("24h Change", f"{data[f'{currency.lower()}_24h_change']:.2f}%")

    time.sleep(update_interval)    