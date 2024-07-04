
#  Calculate correlation coefficient between two cryptocurrency pairs. By default uses 1-day interval close price. Takes >10min to complete for 365 values.



import requests
import datetime
import time
import numpy as np
from scipy.stats import pearsonr

def get_binance_price(symbol, timestamp):
    api_url = "https://api.binance.com/api/v3/klines"
    interval = "1d"  # 1 day interval
    limit = 1000     # Maximum limit per request
    
    timestamp_ms = timestamp * 1000 # Convert timestamp to milliseconds
    
    # Construct query parameters
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
        "startTime": timestamp_ms,
        "endTime": timestamp_ms + 86400000
    }
    
    # Make request to Binance API
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            # The response contains a list of candlestick data, we are interested in the close price of the first candlestick
            return float(data[0][4])  # Closing price is at index 4
        else:
            return None
    else:
        print("Error fetching data from Binance API:", response.text)
        return None



if __name__ == "__main__":
    date=None

    # Parameters
    symbolA = "BTCUSDT"  # First pair
    symbolB = "ETHUSDT"  # Second pair
    period = 5 # Number of intervals (days by default)
    #date = "2024-03-10 00:00:00"   # The final (latest) date, comment out if using current
    

    # By default take current day as date
    date2 = datetime.datetime.now()
    date2 = date2.replace(hour=0, minute=0, second=0, microsecond=0)
    date2 = date2 - datetime.timedelta(days=1)
    
    # Convert date to a unix timestamp
    if date is not None:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_obj = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        print("Date not specified, assuming current.")
        date_obj=date2
    timestamp = int(date_obj.timestamp())

    A_price_list = []
    B_price_list = []
    correlation_list = []

    # Fetch list of A prices
    for i in range(period):
        # Fetch the price for the current timestamp
        price = get_binance_price(symbolA, timestamp)
        date_time = datetime.datetime.fromtimestamp(timestamp)
        print(f"Fetching A price {i+1}/{period} - Timestamp: {date_time}, Price: {price}")

        A_price_list.append(price) # Append the price to the list

        timestamp -= 86400  # Update the timestamp for the next iteration

        time.sleep(0.05) # Small delay to avoid hitting API rate limits
    print("============")

    # Fetch list of B prices
    timestamp = int(date_obj.timestamp())
    for i in range(period):
        price = get_binance_price(symbolB, timestamp)
        date_time = datetime.datetime.fromtimestamp(timestamp)
        print(f"Fetching B price {i+1}/{period} - Timestamp: {date_time}, Price: {price}")
        B_price_list.append(price)
        timestamp -= 86400
        time.sleep(0.05)   
    print("============")
    
    """
    # Uncomment to view the list of prices
    print("List of A prices:", A_price_list) 
    print("List of B prices:", B_price_list)
    """
    
    correlation_coefficient, p_value = pearsonr(A_price_list, B_price_list)

    print("Correlation Coefficient:", correlation_coefficient)  
    print("P-value:", p_value)


#symbols: BTCUSDT, ETHUSDT, BCHUSDT, XRPUSDT, EOSUSDT, LTCUSDT, ETCUSDT, BNBUSDT, DOGEUSDT, SOLUSDT, CHZUSDT, WLDUSDT, GALAUSDT, AVAXUSDT, CELOUSDT,
# NEARUSDT, LINKUSDT, ZRXUSDT, ADAUSDT, FILUSDT, DOTUSDT, MATICUSDT, POWRUSDT, THETAUSDT.
