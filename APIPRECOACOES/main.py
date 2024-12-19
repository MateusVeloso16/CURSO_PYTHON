from chave import chave_api
import requests

#print(f"Testando a minha chave do api:{chave_api}")
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave_api}'
r = requests.get(url)
data = r.json()

print(data["Weekly Adjusted Time Series"]["2000-01-07"]["5. adjusted close"])