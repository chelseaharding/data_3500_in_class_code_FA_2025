# handling exceptions

num1 = input("Enter first num: ")
num2 = input("Enter second num: ")

try:
    result = int(num1)/int(num2)
    print("result:", result)
except:
    print("Invalid user input")


# checking for first buy
# open a file

# JSON

import json

mario = {}

mario["name"] = "Mario Mario"
mario["profession"] = "Plummer"
mario["lives"] = 3
mario["age"] = 44
mario["relationships"] = ["Peach", "Luigi", "Bowser", "Toad", "Donkey Kong"]

json.dump(mario, open("/workspaces/data_3500_in_class_code_FA_2025/Lecture_code/mario.json", "w"), indent=4)

mario_dict = json.load(open("/workspaces/data_3500_in_class_code_FA_2025/Lecture_code/mario.json"))
# print(mario_dict)


# api
import requests

url = "https://v2.jokeapi.dev/joke/programming"

# request = requests.get(url)
# # print(request.text)

# request_dict = json.loads(request.text)
# # print(request_dict)

while True:
    request = requests.get(url)
    # print(request.text)

    request_dict = json.loads(request.text)
    # print(request_dict)

    keep_going = input("Do you want to hear a programming joke? (Y/N) ")
    if keep_going == "Y":
        if request_dict["type"] == "single":
            print(request_dict["joke"])
        else:
            print(request_dict["setup"])
            input("(press enter to hear the punchline)")
            print(request_dict["delivery"])
    else:
        print("Okay no more jokes.")
        break