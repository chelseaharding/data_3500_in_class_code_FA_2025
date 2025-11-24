import requests
import json
import time


results = {}
tickers = ["AAPL", "TSLA", "NVDA", "SONY", "COST", "META", "AMZN", "SNAP", "DAL", "FIX"]
# tickers = ["AAPL"]

def inital_data_pull(ticker):
    # keys
    key1 = "Time Series (Daily)"
    key2 = "4. close"
    # date_key = "" # I know I need all the dates (maybe use an iterator variable???)

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

    request = requests.get(url)
    request_dictionary = json.loads(request.text)
    # print(request_dictionary)

    file = open("/workspaces/data_3500_in_class_code_FA_2025/stock_market_trading/"+ticker+".csv", "w")

    lines = []

    for date in request_dictionary[key1].keys():
        lines.append(date + ", " + request_dictionary[key1][date][key2] + "\n")

    lines = lines[::-1]
    file.writelines(lines)
    file.close()

def append_data(ticker):
    time.sleep(20)
    # keys
    key1 = "Time Series (Daily)"
    key2 = "4. close"

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&apikey=MA2ML1YNK446WMJU"

    request = requests.get(url)
    request_dictionary = json.loads(request.text)

    # print(request_dictionary)

    with open("stock_market_trading/"+ticker+".csv") as file:
        lines = file.readlines()

    recentest_date = lines[-1].split(", ")[0]
    # print(recentest_date)

    new_lines = []
    for date in request_dictionary[key1].keys():
        if date > recentest_date:
            new_lines.append(date + ", " + request_dictionary[key1][date][key2] + "\n")

    new_lines = new_lines[::-1]

    with open("/workspaces/data_3500_in_class_code_FA_2025/stock_market_trading/"+ticker+".csv", "a") as file:
        file.writelines(new_lines)

def mean_reversion(prices):
    buy             = 0
    first_buy       = 0
    total_profit    = 0
    i               = 0

    for price in prices:
        if i > 4:
            current_price = price
            average_price = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5])/5

            if current_price < (average_price * 0.98) and buy == 0:
                buy = current_price
                # print("Buying at: \t", buy)
                if first_buy == 0:
                    first_buy = current_price
            elif current_price > (average_price * 1.02) and buy != 0:
                trade_profit = current_price - buy
                buy = 0
                # print("Selling at: \t", current_price)
                # print("Trade Profit: \t", trade_profit)
                total_profit += trade_profit

        i += 1

    return total_profit, (total_profit/first_buy)

    # print("------------------------------------")
    # print("Total Profit: \t", total_profit)
    # print("First Buy: \t", first_buy)
    # print("% Return: \t", (total_profit/first_buy) * 100)

def simple_moving_average(prices):
    buy             = 0
    first_buy       = 0
    total_profit    = 0
    i               = 0

    for price in prices:
        if i > 4:
            current_price = price
            average_price = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5])/5

            if current_price > average_price and buy == 0:
                buy = current_price
                # print("Buying at: \t", buy)
                if first_buy == 0:
                    first_buy = current_price
            elif current_price < average_price and buy != 0:
                trade_profit = current_price - buy
                buy = 0
                # print("Selling at: \t", current_price)
                # print("Trade Profit: \t", trade_profit)
                total_profit += trade_profit

        i += 1

    return total_profit, (total_profit/first_buy)

    # print("------------------------------------")
    # print("Total Profit: \t", total_profit)
    # print("First Buy: \t", first_buy)
    # print("% Return: \t", (total_profit/first_buy) * 100)

def load_prices(file):
    prices = [float(line.split(", ")[1]) for line in file.readlines()]
    return prices

def save_results(results):
    json.dump(results, open("/workspaces/data_3500_in_class_code_FA_2025/stock_market_trading/results.json", "w"), indent=4)

for ticker in tickers:
    # inital_data_pull(ticker)
    # append_data(ticker)
    file = open("/workspaces/data_3500_in_class_code_FA_2025/stock_market_trading/"+ticker+".csv")
    prices = load_prices(file)
    results[ticker+"_Prices"] = prices

    mr_total_profit, mr_returns = mean_reversion(prices)
    results[ticker+"_MR_Profit"]  = mr_total_profit
    results[ticker+"_MR_Returns"] = mr_returns

    sma_total_profit, sma_returns = simple_moving_average(prices)
    results[ticker+"_SMA_Profit"]  = sma_total_profit
    results[ticker+"_SMA_Returns"] = sma_returns

save_results(results)