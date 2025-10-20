# """
# This problem was recently asked by Google:

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k = 17, return true since 10 + 7 = 17.

# Bonus: Can you do this in one pass???????
# """

# # iterate through given list
# # take current index and do addition with every other index at some point
# # could use list slicing or indexing
# # nest a for loop

# # if I hit the target then 

# def find_the_target(num_list, k):
#     found = False
#     for i in num_list:

#         for j in num_list:
#             if i + j == k:
#                 found = True
#                 break
#     return found


# given = [9, 2, 24, 16]
# k = 13

# print(find_the_target(given, k))


# list comprehension

# newList = [expression for item in iterable if condition == True]

# example 1
mixed_data = [32, "hello", "world", 42.9, 12, 100, "Monday", 20]

nums = []
for item in mixed_data:
    if isinstance(item, int) == True:
        nums.append(item)

print("nums:", nums)

nums = [item for item in mixed_data if isinstance(item, int) == True]
print("nums list comp:", nums)


# example 2
words = ["racecar", "banana", "level", "civic", "kayak", "pop", "poop", "Aggies", "spider"]

pals = [pal for pal in words if pal == pal[::-1]]
print("pals:", pals)

# example 3
# use list comprehension to make a new list of all the chars in the string that are not spaces and return that list in alphabetical order
text = "hello world"

# item/expression will be each character of the string
# the for loop will be looping over the string - create iterator or value to hold char there
# the conditional is if the character isn't a space: char != " "
# how to sort in alphabetical order??????

letters = sorted([letter for letter in text if letter != " "])
print("letters:", letters)


# homework 4

# file = open("/workspaces/data_3500_in_class_code_FA_2025/AAPL.2023.txt")
# lines = file.readlines()

# prices = []
# for line in lines:
#     line = float(line)
#     prices.append(line)

# print("prices:", prices)

# what is the expression we want to end up with in the new list?
# what are we looping through?
# what is the iterator variable?
# what is the condition? Is there a condition?
# prices :)
file = open("/workspaces/data_3500_in_class_code_FA_2025/AAPL.2023.txt")

prices = [round(float(line), 2) for line in file.readlines()]

print("prices:", prices)
