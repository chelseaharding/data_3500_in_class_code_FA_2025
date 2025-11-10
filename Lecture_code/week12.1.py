"""
This question was asked by Google.
Given an integer num and a list of integers int_list, write a function that randomly generates a number from 0 to num-1 that isn't in int_list.

example:

num = 10
int_list = [1, 3, 5, 7, 9]
generate_random_excluding(num, int_list)
"""

import random

# def random_list_num(num, int_list):
#     possible_randoms = []
    
#     for i in range(num):
#         if i not in int_list:
#             possible_randoms.append(i)

#     random_choice = random.randint(1, len(possible_randoms))
#     return possible_randoms[random_choice]

# num = 80
# int_list = [1, 3, 5, 7, 9]
# print(random_list_num(num, int_list))

# dictionary
lance = {}

lance["name"] = "Lance Nielsen"
lance["age"] = 25
lance["car"] = {"make":"Hyundai", "model":"Sonata" , "year":2010, "mileage":185000, "transmission":"Automatic", "color":"Blue", "num_doors":4}
lance["major"] = "Information Systems"
lance["married"] = True
lance["schedule"] = ["DATA3500", "DATA4330", "IS3600", "MSLE3890", "DATA5360"]
lance["fav_temp"] = 72.5

# print("lance:", lance)

print(lance["age"])
print(lance["schedule"])
print(lance["car"])

# how do I access a list element from a list stored in a dictionary?
print(lance["schedule"][2])

lance["schedule"].append("STAT1040")
print(lance)

print(lance["car"]["num_doors"])

for key in lance["car"].keys():
    print("key:", key)

"""
Write a program that asks the user the following survey information (a mixture of strings and numbers)
How many years have you lived in Cache Valley (enter a float)?
What is your favorite color (enter a string)?
What is your favorite programming language (enter a string)?

store the user's answers in a Dictionary
loop through the dictionary and print all the values
solution to checkpoint is in python code, link above
"""

years_in_CV = float(input("How long have you lived in CV: "))
fav_color = input("What is your fav color: ")
fav_prog_lang = input("What is your favorite programming language: ")

survey = {"years_in_CV":years_in_CV, "fav_color":fav_color, "fav_prog_lang":fav_prog_lang}

for key in survey.keys():
    print("key:", key, "value:", survey[key])