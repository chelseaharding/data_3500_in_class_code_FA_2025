"""
Authors: Chelsea, Jacob, Patrick
Assignment 6

Please note that this code is the best thin you will EVER see so take that into account while you are viewing it
"""

import numpy as np

"""
Programming Activity 1

Write a program, and have the user enter their name and their favorite 
color, as two separate variables. Write the sentence to a file using the 
with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""

name = input("NAME: ")
color = input("COLOR: ")

with open("sentance.txt", "w") as file:
    file.write(name + "'s favorite color is " + color)

"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""
 
arr = np.zeros(100)
arr = np.random.rand(100)
print("arr:", arr)
