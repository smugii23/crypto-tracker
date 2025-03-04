from api import symbol_to_id_name
import json

def add_portfolio(portfolio):
    from main import get_crypto_choice  

    while True: 
        symbol = get_crypto_choice()
        crypto_data = symbol_to_id_name(symbol)
        
        if crypto_data is None:
            print("❌ Invalid cryptocurrency symbol. Please try again.")
            continue
        try:
            amount = float(input(f"Enter the amount of {symbol} you own: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
            continue

        portfolio[symbol] = float(portfolio.get(symbol, 0)) + amount
        print(f"✅ Added {amount} {symbol} to your portfolio.")
        break


def subtract_portfolio(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return
    print("📜 Your portfolio:")
    for symbol, amount in portfolio.items():
        print(f"- {symbol}: {amount}")
    delete_symbol = input("Enter the symbol of the coin to subtract from your portfolio: ")
    if delete_symbol in portfolio:
        try:
            subtract_amount = float(input(f"Enter the amount of {delete_symbol} to subtract: "))
            if subtract_amount <= 0:
                print("❌ Amount must be greater than 0.")
                return
            if subtract_amount > portfolio[delete_symbol]:
                print("❌ You cannot subtract more than you have in your portfolio.")
                return
            portfolio[delete_symbol] -= subtract_amount
            if portfolio[delete_symbol] == 0:
                del portfolio[delete_symbol]
                print(f"{delete_symbol} has been deleted from your portfolio.")
            else:
                print(f"{subtract_amount} {delete_symbol} has been subtracted from your portfolio.")
        except ValueError:
            print(f"❌ Invalid amount.")
    else:
        print(f"❌ {delete_symbol} not found in your portfolio.")
    


def save_portfolio(portfolio, filename="portfolio.json"):
    with open(filename, 'w') as file:
        json.dump(portfolio, file)
    print(f"✅ Portfolio saved to {filename}.")

def load_portfolio(filename="portfolio.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}