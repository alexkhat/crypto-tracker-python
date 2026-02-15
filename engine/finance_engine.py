import yfinance as yf
import requests
import pandas as pd

class FinanceEngine:
    """Professional Finance Engine for multi-asset tracking."""
    
    def __init__(self, currency="GBP"):
        self.currency = currency.lower()
        self.crypto_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_uk_stocks(self, tickers=['RR.L', 'BP.L', 'VOD.L', 'BARC.L']):
        """Fetches live LSE data, mimicking IEUK consulting standards."""
        stock_list = []
        for ticker in tickers:
            try:
                data = yf.Ticker(ticker).fast_info
                stock_list.append({
                    "Symbol": ticker,
                    "Price": round(data['last_price'], 2),
                    "Market": "LSE"
                })
            except Exception as e:
                print(f"Stock Fetch Error for {ticker}: {e}")
        return pd.DataFrame(stock_list)

    def get_crypto_assets(self, coins=['bitcoin', 'ethereum', 'solana']):
        """Aggregates crypto data for high-end portfolio management."""
        params = {
            'ids': ','.join(coins),
            'vs_currencies': self.currency,
            'include_24hr_change': 'true'
        }
        try:
            res = requests.get(self.crypto_url, params=params).json()
            return res
        except Exception as e:
            return f"Crypto API Error: {e}"