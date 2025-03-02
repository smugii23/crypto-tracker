import json

def add_portfolio(portfolio):
    from main import get_crypto_choice
    symbol = get_crypto_choice()
    amount = input(f"Enter the amount of {symbol} you own: ")
    if symbol in portfolio:
        portfolio[symbol] += amount
    else:
        portfolio[symbol] = amount
    print(f"✅ Added {amount} {symbol} to your portfolio.")

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