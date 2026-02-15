import streamlit as st
from engine.finance_engine import FinanceEngine
import plotly.graph_objects as go

# Custom CSS to make it look like a High-End Fintech App
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .metric-card { background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Secure Finance Hub (V1.0)")
st.info("Professional Student Member: British Computer Society (BCS) | Edinburgh Napier University")

# Initialize Engine
engine = FinanceEngine(currency="GBP")

# Main Interface
menu = st.sidebar.radio("Navigation", ["Dashboard", "Asset Intelligence", "Banking Simulation"])

if menu == "Dashboard":
    st.subheader("Global Portfolio Overview")
    
    # Real-time Crypto Metrics
    crypto_data = engine.get_crypto_assets()
    c1, c2, c3 = st.columns(3)
    c1.metric("Bitcoin", f"£{crypto_data['bitcoin']['gbp']:,}")
    c2.metric("Ethereum", f"£{crypto_data['ethereum']['gbp']:,}")
    c3.metric("Solana", f"£{crypto_data['solana']['gbp']:,}")

elif menu == "Asset Intelligence":
    st.subheader("UK Stock Market Integration (FTSE)")
    stocks_df = engine.get_uk_stocks()
    st.table(stocks_df)
    st.caption("Data provided via LSE Real-time integration (Simulated API Pipeline).")

elif menu == "Banking Simulation":
    st.subheader("Fintech Integration (Revolut / Monzo)")
    st.warning("Secure API Handshake simulation active.")
    # Demonstrates your Cybersecurity & Secure Coding skills
    st.code("POST /auth/v1/bank-connect HTTP/1.1\nHost: api.revolut.com\nAuthorization: Bearer [ENCRYPTED_JWT]")
    st.success("GDPR-Compliant Connection Established.")