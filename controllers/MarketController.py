# market_controller.py

import yfinance as yf
from datetime import datetime, timedelta
import random

def get_change_data(ticker, start_date, end_date):
    """fetches the data for the given ticker, calculates relevant changes """
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        close_prices = stock_data['Close']
        current_price = close_prices[-1]
        daily_change = current_price - close_prices[-2]
        weekly_change = current_price - close_prices[-7]
        monthly_change = current_price - close_prices[-23]
        three_month_change = current_price - close_prices[-67]
        
        # Check if the index -250 is out of bounds
        twelve_month_index = -250 if len(close_prices) >= 250 else -(len(close_prices) - 1)
        twelve_month_change = current_price - close_prices[twelve_month_index]

        return {
            "ticker": ticker,
            "current_price": current_price,
            "daily_change": daily_change,
            "weekly_change": weekly_change,
            "monthly_change": monthly_change,
            "three_month_change": three_month_change,
            "twelve_month_change": twelve_month_change
        }
    except KeyError as e:
        print(f"Error: {e}")
        return {
            "ticker": ticker,
            "error": "Data not available for the specified ticker or date range."
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "ticker": ticker,
            "error": "An error occurred while fetching data. Please check your connection and try again."
        }

class MarketController:
    def get_market_data(self, tickers = ['^GSPC', '^GSPTSE', 'GC=F', 'CL=F', 'BTC-USD']):
        # tickers = ['^GSPC', '^GSPTSE', 'GC=F', 'CL=F', 'BTC-USD']
        date = datetime.now()
        end_date = date.strftime('%Y-%m-%d')
        start_date = (date - timedelta(days=365)).strftime('%Y-%m-%d')

        market_data = []
        for ticker in tickers:
            data = get_change_data(ticker, start_date, end_date)
            market_data.append(data)

        return market_data
    
    def get_dummy_data(self, tickers = ['^GSPC', '^GSPTSE', 'GC=F', 'CL=F', 'BTC-USD']):
        """dummy api function"""
        dummy_market_data = []

        for ticker in tickers:
            data = {
                "ticker": ticker,
                "current_price": random.randint(8000, 25000),
                "daily_change": random.randint(-10, 10),
                "weekly_change": random.randint(-25, 25),
                "monthly_change": random.randint(-40, 40),
                "three_month_change": random.randint(-150, 150),
                "twelve_month_change": random.randint(-300, 300)
            }
            dummy_market_data.append(data)
        
        return dummy_market_data


