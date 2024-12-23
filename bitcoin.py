import requests
import time

def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    print(response)
    data = response.json()
    print(data)
    price = data['bpi']['USD']['rate']
    return price

while True:
    price = get_bitcoin_price()
    print(f'현재 비트코인 가격: ${price}')
    time.sleep(10)