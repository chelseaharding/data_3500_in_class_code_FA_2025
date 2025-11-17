"""
This problem was asked by Google:
Given a string of words delimated by space, reverse the order of the words in the string. For example, given "Hello world here" you should return "here world hello"
"""

string = "Aggie basketball rocks"

words = string.split(" ")
reversed_words = words[::-1]
reversed_string = " ".join(reversed_words)
print("string:", string)
print("rev string:", reversed_string)


# web json apis
"""
Programming Activity 1

Write a program which gets the json from the URL: 
https://api.datamuse.com/words?rel_trg=cow (Links to an external site.) and prints the score for the word "cheese". That URL returns words related 
to the word: cow.  
- import json and requests
- create a request (req = requests(url))
- create a dictionary (dct1  = json.loads(req.text))
- loop through the list of dictionaries looking for the key word "cheese"
- when you find the key word cheese, print the value for keyword "score" in the same dictionary
"""

import json
import requests

url = "https://api.datamuse.com/words?rel_trg=cow"

request = requests.get(url)
# print(request.text)

word_list = json.loads(request.text)
print(word_list[10])

for word_dictionary in word_list:
    if word_dictionary["word"] == "cheese":
        print(word_dictionary["score"])

        