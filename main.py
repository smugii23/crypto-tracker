from api import *
from utils import format_price, format_percent
from models import Timeframe
from info import get_news, get_score
from datetime import datetime
from portfolio import add_portfolio, load_portfolio, save_portfolio
import textwrap

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

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
    portfolio = load_portfolio()
    while True:
        clear_screen()
        menu = textwrap.dedent("""
            ================================
                     CRYPTO TRACKER
            ================================
            1. Find the current price of a coin
            2. Find the price change of a coin
            3. Find the polarity score of a coin
            --------------------------------
            Enter 'q' to quit.
        """)
        print(menu)

        selection = input("Your choice: ").strip().lower()

        if selection == '1':
            choice = get_crypto_choice()
            crypto_id = symbol_to_id_name(choice)[0]
            price = find_price(crypto_id)
            print(f"\n🔹 Price: {format_price(price)}")

        elif selection == '2':
            choice = get_crypto_choice()
            crypto_id = symbol_to_id_name(choice)[0]
            timeframe = get_timeframe()
            change = percent_change(crypto_id, timeframe)
            print(f"\n📉 {timeframe.value} Change: {format_percent(change)}")

        elif selection == '3':
            choice = get_crypto_choice()
            news_timeframe = get_news_timeframe()
            data = get_news(choice, str(news_timeframe))
            polarity_score = get_score(data)
            print(f"\n📰 Polarity Score: {polarity_score}")
        
        elif selection == '4':
            add_portfolio(portfolio)

        elif selection == 'q':
            print("\n👋 Exiting program.")
            break

        else:
            print("\n❌ Invalid selection. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()