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