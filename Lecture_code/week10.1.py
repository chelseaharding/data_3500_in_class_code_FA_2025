"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whoes sum will be equal to the given number.

A solution will always exist. (Goldbach's Conjecture)

Example:

Input: 4
Output: 2 + 2 = 4

Professor H Note:)
This might be kinda hard, so an alternative challenge is to write a function which returns if a number is prime or not. 

def is_prime(number):
    # should return either true or false
    return
"""

# function to find all primes up to X
# another funciton to check primes in a list and see if they add up to sum

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
def list_of_primes(x):
    primes = []
    for i in range(x):
        if is_prime(i):
            primes.append(i)
    return primes

def goldbachs(list_of_primes, target):
    for i in list_of_primes:
        for j in list_of_primes:
            if i + j == target:
                return str(i) + " and " + str(j) + " are prime pairs adding up to " + str(target)
            
primes = list_of_primes(12)
print(goldbachs(primes, 12))

# substrings
emojis = "😀😃😄😁😆😅🤣😂🙂😉😊😇🥰😍🤩😘😗☺️😚😙🥲😏"

if "🤣" in emojis:
    print("This is my favorite emoji: 🤣")

# replacing

sentance = "Our offices are mainly in California but some are in New York"

# we want CA instead of California
# NY instead of New York

sentance = sentance.replace("New York", "NY")
sentance = sentance.replace("California", "CA")
print(sentance)

# split and join
words = sentance.split(" ")
print("words:", words)

text = "0.0".join(words)
print("text:", text)

# char test
text = "0500 Old Main Hill Logan Utah 84322"
print(text.isalnum())
print(text.isalpha())
