"""
This question was asked by ContextLogic.
Write a function that implements the division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""

"""
write a function

count the number of times we subtract the first number from the second number

Answer will be the number of times we subtracted
"""

def division(numerator, denom):
    counter = 0

    while numerator >= denom:
        numerator -= denom
        counter += 1

    return counter


print(division(64, 8))
print(division(72, 3))
print(division(10, 4))


# files

# open()
# with open()

file = open("/workspaces/data_3500_in_class_code_FA_2025/Lecture_code/test.txt", "w")
names = ["Jacob\n", "Geoffery\n", "Sarah\n", "Steven\n"]
file.writelines(names)
file.close()

file = open("/workspaces/data_3500_in_class_code_FA_2025/Lecture_code/test.txt", "a")
ages = [25, 72, 5, 21]
for age in ages:
    file.write(str(age)+"\n")
# file.writelines(str(ages))
file.close()

# numbers file
# find standard deviation
# find mean
# write both of those things to a new file

import statistics
# statistics.mean()
# statistics.stdev()

with open("/workspaces/data_3500_in_class_code_FA_2025/Lecture_code/numbers.txt") as numbers_file:
    lines = numbers_file.readlines()

# print("lines before loop:", lines)
numbers = []
for line in lines:
    numbers.append(int(line))

mean = statistics.mean(numbers)
stdev = statistics.stdev(numbers)

print("mean:", mean, "stdev:", stdev)

with open("/workspaces/data_3500_in_class_code_FA_2025/Lecture_code/statistics.txt", "w") as file:
    file.write("Mean: " + str(mean) + "\n")
    file.write("StDev: " + str(stdev) + "\n")

# print("lines after loop:", lines)