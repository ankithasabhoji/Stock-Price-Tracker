# Stock Market Data Tracker 

A Python application that fetches daily stock market information using the Alpha Vantage API.

## Features
- Search stocks using ticker symbols.
- Display the latest available trading date.
- Show the opening stock price.
- Handle API and network errors.

## Technologies
- Python
- Requests
- Alpha Vantage API
- python-dotenv

## Setup
1. Install dependencies:
   `pip install -r requirements.txt`
2. Create a `.env` file and add:
   `ALPHAVANTAGE_API_KEY=your_api_key`
3. Run:
   `python stock.py`

**Note:** A personal Alpha Vantage API key is required.