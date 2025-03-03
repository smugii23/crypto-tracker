from requests import    Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY = os.getenv('CMC_API_KEY')
BASE_URL = "https://pro-api.coinmarketcap.com"

def symbol_to_id_name(choice):
    parameters = {'symbol': choice}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    session = Session()
    session.headers.update(headers)
    url = BASE_URL + "/v1/cryptocurrency/map"

    try:
        response = session.get(url, params=parameters)
        data = response.json() 
        # if there is an error, handle it
        if 'status' in data and data['status']['error_code'] != 0:
            print(f"❌ API Error: {data['status']['error_message']}")
            return None  
        # if data is successfully returned, return the id and name
        if 'data' in data and data['data']:
            return (data['data'][0]['id'], data['data'][0]['name'])
        # handle the case where no coin is found
        print("❌ No coin found.")
        return None

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"❌ API Request Error: {e}")
        return None



def find_price(id):
    parameters = {
     'id': id
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
    }

    session = Session()
    session.headers.update(headers)
    url = BASE_URL
    try:
        response = session.get(url + "/v2/cryptocurrency/quotes/latest", params=parameters)
        data = json.loads(response.text)
        if data['data']:
            return data['data'][str(id)]['quote']['USD']['price']
        else:
            raise Exception("Price not found")
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def percent_change(id, timeframe):
    parameters = {
     'id': id
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
    }

    session = Session()
    session.headers.update(headers)
    url = BASE_URL
    try:
        response = session.get(url + "/v2/cryptocurrency/quotes/latest", params=parameters)
        data = json.loads(response.text)
        if data['data']:
            return data['data'][str(id)]['quote']['USD'][f'percent_change_{timeframe.value}']
        else:
            raise Exception("Price not found")
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
