import requests

server_url = "https://api.upbit.com"

params = {
    "markets": "KRW-BTC,KRW-ETH"
}

res = requests.get(server_url + "/v1/ticker", params=params)
data=res.json()
price=data[0]['trade_price']
print(price)
