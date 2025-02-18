from api import *


def get_crypto_choice():
    return input("Enter cryptocurrency symbol: ").upper() 

def main():
    choice = get_crypto_choice()
    id = symbol_to_id(choice)
    data = find_price(id)


main()