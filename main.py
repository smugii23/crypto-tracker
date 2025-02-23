from api import *
from utils import format_price, format_percent
from models import Timeframe
from info import reddit, get_news, get_score
from datetime import datetime

def get_crypto_choice():
    return input("Enter cryptocurrency symbol: ").upper() 

def get_timeframe():
    while True:
        choice = input("Enter the timeframe (1h, 24h, 7d, 30d): ").lower()
        # make sure input is one of the valid timeframes
        for frame in Timeframe:
            if frame.value == choice:
                return frame
        print("Invalid timeframe! Please try again.")

def get_news_timeframe():
    while True:
        start = input("Enter date to search from (eg. 2024-02-03): ")
        try:
            start = datetime.strptime(start, "%Y-%m-%d")
        except:
            print("Invalid format.")
            continue
        end = input("Enter date to search to (eg. 2025-02-03): ")
        try:
            end = datetime.strptime(end, "%Y-%m-%d")
        except:
            print("Invalid format.")
            continue
        if start < end:
            return (start, end)

def main():
    choice = get_crypto_choice()
    timeframe = get_timeframe()
    news_timeframe = get_news_timeframe()

    id = symbol_to_id_name(choice)
    price = find_price(id[0])
    change = percent_change(id[0], timeframe)
    data = get_news(id, str(news_timeframe))
    polarity_score = get_score(data)
    
    print(f"\n{choice} Status:")
    print(f"Price: {format_price(price)}")
    print(f"{timeframe.value} Change: {format_percent(change)}")
    print(f"Polarity score: {polarity_score}")

if __name__ == "__main__":
    main()