from api import find_price


def get_crypto_choice():
    return input("Enter cryptocurrency symbol: ").upper() 

def main():
    choice = get_crypto_choice()
    data = find_price(choice)
    

main()