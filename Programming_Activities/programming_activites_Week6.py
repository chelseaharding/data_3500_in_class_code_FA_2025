"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""
colors = ["aggie blue", "mustard", "emerald green"]
for color in colors:
    print("color:", color)

"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""
for color in colors:
    for letter in color:
        print("letter:", letter)
    print()

"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random

rand_nums = []

for i in range(10):
    rand_nums.append(random.randint(1, 100))

print("random nums:", rand_nums)