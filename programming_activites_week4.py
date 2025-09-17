"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Gen Beta 2025
 - Gen Alpha 2013
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""

# get input from use about year of birth
year = int(input("What year were you born: "))

# giant if statment to see which gen they belong to - also print it :)
if year >= 2026:
    print("you aren't born yet")
elif year <= 1964:
    print("You are a boomer")
elif year <= 1980:
    print("You are gen x")
elif year <= 1996:
    print("You are a millennial")
elif year <= 2012:
    print("You are gen z")
elif year <= 2024:
    print("You are gen alpha")
else:
    print("You are gen beta")


"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""
age = int(input("How old are you: "))
current_year = 2025
while age >= 1:
    print("You were alive in", current_year)
    age -= 1
    current_year -= 1
else:
    print("You were born in", current_year)
"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5, 96, 5):
    print("i:", i)
"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
num = 5
while num < 96:
    print("num:", num)
    num += 5