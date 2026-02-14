import requests
import time

# RESTful API integration
def get_market_data(coin_id='bitcoin'):
    """" Feteches real-time price and 24h change in GBP."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=gbp&include_24hr_change=true"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[coin_id]['gbp']
        change = data[coin_id]['gbp_24h_change']
        return price, change
    except Exception as e:
        print(f"Technical Error: {e}")
        return None, None
    
def start_monitor():
    print("---🚀 UK Crypto Market Monitor (GBP)---")
    print("Press Ctrl+c to stop.")
    try:
        while True:
            price, change = get_market_data('bitcoin')
            if price:
                # Formatting data for readability, showcasing Data Analytics skills
                print(f"BTC: £{price:.2f} | 24h Change: {change:.2f}%")

            #30-second interval to manage API rate limits
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nMonitoring suspended.")

if __name__ == "__main__":
    start_monitor()
