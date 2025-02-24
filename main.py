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
    while True:
        selection = input("Select an option:\n1. Find the current price of a coin\n2. Find the price change of a coin\n3. Find the polarity score of a coin\nEnter 'q' to quit.\n")
        if selection == '1':
            choice = get_crypto_choice()
            id = symbol_to_id_name(choice)
            price = find_price(id[0])
            print(f"Price: {format_price(price)}\n")
        elif selection == '2':
            choice = get_crypto_choice()
            id = symbol_to_id_name(choice)
            timeframe = get_timeframe()
            change = percent_change(id[0], timeframe)
            print(f"{timeframe.value} Change: {format_percent(change)}\n")
        elif selection == '3':
            choice = get_crypto_choice()
            id = symbol_to_id_name(choice)
            news_timeframe = get_news_timeframe()
            data = get_news(id, str(news_timeframe))
            polarity_score = get_score(data)
            print(f"Polarity score: {polarity_score}\n")
        elif selection.lower() == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid selection.\n")

if __name__ == "__main__":
    main()