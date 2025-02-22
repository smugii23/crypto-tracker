from api import *
from utils import format_price, format_percent
from models import Timeframe
from info import reddit, get_news, get_score

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


def main():
    choice = get_crypto_choice()
    timeframe = get_timeframe()
    id = symbol_to_id(choice)

    price = find_price(id)
    change = percent_change(id, timeframe)
    data = get_news(choice)
    polarity_score = get_score(data)
    
    print(f"\n{choice} Status:")
    print(f"Price: {format_price(price)}")
    print(f"{timeframe.value} Change: {format_percent(change)}")
    print(polarity_score)

if __name__ == "__main__":
    main()