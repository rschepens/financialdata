import requests
import json

api_url = 'https://finnhub.io/api/v1/stock/financials?symbol=AAPL&statement=bs&freq=annual&token='

response = requests.get(api_url)

content = json.loads(response.content.decode('utf-8'))


for line in content["financials"]:
    print(line["cash"])
