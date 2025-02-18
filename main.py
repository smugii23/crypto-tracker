from api import *


def get_crypto_choice():
    return input("Enter cryptocurrency symbol: ").upper() 

def get_timeframe():
    return input("Enter the timeframe (1h, 24h, 7d, 30d): ").lower()

def format_percent(change):
    if change > 0:
        return f"+{change:.2f}%"
    else:
        return f"{change:.2f}%"

def format_price(price):
    if price >= 1.0:
        return f"${price:.2f}"
    elif price >= 0.01:
        return f"${price:.4f}"
    else:
        return f"${price:.8f}"

def main():
    choice = get_crypto_choice()
    timeframe = get_timeframe()
    id = symbol_to_id(choice)

    price = find_price(id)
    change = percent_change(id, timeframe)
    
    print(f"\n{choice} Status:")
    print(f"Price: {format_price(price)}")
    print(f"{timeframe} Change: {format_percent(change)}")

main()