# numpy

import numpy
import statistics
import pandas

prices = [123, 234, 345, 456]
np_prices = numpy.array(prices)
print("np_prices:", np_prices)


# numpy zeros

arr = numpy.zeros(10)
print("arr:", arr)

# generate 5 random numbers from a normal distribution

random_distribution = numpy.random.normal(0, 1, 5)
print("random_distribution:", random_distribution)

# shuffle 
arr = numpy.array([1, 2, 3, 4, 5, 6, 7])
numpy.random.shuffle(arr)
print("arr:", arr)


"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homweork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""

# with open("/workspaces/data_3500_in_class_code_FA_2025/AAPL.2023.txt") as file:
#     prices = []
#     for line in file.readlines():
#         prices.append(float(line))

# print("prices:", prices)

# i = 0

# for price in prices:
#     if i >= len(prices) - 4:
#         break
#     moving_avg = (prices[i] + prices[i+1] + prices[i+2] + prices[i+3] + prices[i+4]) / 5
#     print("moving avg:", moving_avg)
#     i += 1


# i = 0

# for price in prices:
#     if i > 4:
#         moving_avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
#         print("moving avg:", moving_avg)
#     i += 1    

with open("/workspaces/data_3500_in_class_code_FA_2025/AAPL.2023.txt") as file:
    prices = []
    for line in file.readlines():
        prices.append(float(line))

np_prices = numpy.array(prices)

i = 0

for price in np_prices:
    if i > 4:
        moving_avg = (np_prices[i-1] + np_prices[i-2] + np_prices[i-3] + np_prices[i-4] + np_prices[i-5]) / 5
        print("moving avg:", moving_avg)
    i += 1   