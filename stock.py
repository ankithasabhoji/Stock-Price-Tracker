
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_stock_price(symbol):
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    base_url = "https://www.alphavantage.co/query"

    if not api_key:
        print("Error: API key not found. Check your .env file.")
        return

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol.upper(),
        "outputsize": "compact",
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        # Check API messages
        if "Error Message" in data:
            print("Invalid stock symbol. Please check and try again.")
            return

        if "Note" in data:
            print("API rate limit reached. Please try again later.")
            return

        if "Information" in data:
            print("API information:", data["Information"])
            return

        time_series = data.get("Time Series (Daily)", {})

        if time_series:
            latest_time = max(time_series.keys())
            latest_price = time_series[latest_time]["1. open"]

            print(f"\nStock: {symbol.upper()}")
            print(f"Latest available date: {latest_time}")
            print(f"Opening price: ${latest_price}")

        else:
            print("No stock data available.")
            print("The API may not provide intraday data for this symbol or plan.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")

    except requests.exceptions.RequestException:
        print("Unable to connect to the stock API.")

    except (ValueError, KeyError):
        print("Unable to process stock data.")


symbol = input("Enter stock symbol (e.g. AAPL): ").strip()

if not symbol:
    print("Stock symbol cannot be empty.")
else:
    get_stock_price(symbol)
