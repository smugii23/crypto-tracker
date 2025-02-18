from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from config import BASE_URL, API_KEY
import json

def find_price(choice):
    parameters = {
     'symbol': choice
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
        return(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)