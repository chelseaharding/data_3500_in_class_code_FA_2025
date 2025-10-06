# # list slicing

states = ["North Carolina", "Wyoming", "Texas", "Massachusetts", "Pennsylvania", "Arizona", "Utah", "alabama"]

# index of MA
print(states[3])

# slice operator : classic slice
subset1 = states[1:4]
print("subset1:", subset1)

# just the last element of our list
last_element = states[-1:]
print("last_element:", last_element)

# reverse a list
reversed_states = states[::-1]
print("reversed states:", reversed_states)

# return everything except for the last two elements
subset2 = states[:-2]
print("subset2:", subset2)

# every other element
subset3 = states[::2]
print("subset3:", subset3)

# reversed 
states.reverse()
print("reversed 2:", states)

# sort
states.sort()
print("sorted states:", states)


"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""

# write a function to calculate avg for year of stock prices

file = open("/workspaces/data_3500_in_class_code_FA_2025/AAPL.2023.txt")
print("file:", file)
lines = file.readlines()
print("lines:", lines)
print(len(lines))

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

print("prices:", prices)

def avg_calculator(prices):
    return sum(prices)/len(prices)

print("avg:", avg_calculator(prices))

def avg_first_5_days(prices):
    return sum(prices[0:5])/5

print("first 5 days:", avg_first_5_days(prices))

print("first 5 days:", avg_calculator(prices[0:5]))

# moving avg??????

print("last 5:", avg_calculator(prices[-5:]))


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
