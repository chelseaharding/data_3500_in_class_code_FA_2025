import requests
import json


# keys
key1 = "Time Series (Daily)"
key2 = "4. close"
# date_key = "" # I know I need all the dates (maybe use an iterator variable???)

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

request = requests.get(url)
request_dictionary = json.loads(request.text)
# print(request_dictionary)


file = open("/workspaces/data_3500_in_class_code_FA_2025/stock_market_trading/AAPL.csv", "w")

lines = []

for date in request_dictionary[key1].keys():
    lines.append(date + ", " + request_dictionary[key1][date][key2] + "\n")

lines = lines[::-1]
file.writelines(lines)
file.close()


