"""
This problem was asked by Apple.
Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
Given integers N and X, write a python script that returns the number of times X appears as a value in an N by N multiplication table.
For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
"""
N = 1000
X = 56

"""
pseudo code

counter_row
counter_col

looping

if row * col == X:
    counter += 1
"""

counter = 0

for row in range(1, N + 1):
    # print(row)
    for col in range(1, N + 1):
        # print(col, end="")
        # print(row, col)
        # print(row * col, end="\t")
        if row * col == X:
            counter += 1
    # print()

print("There are", counter, "occurances of", X)


# nested statements - refer above


# sentinal value - break and continue

# print("Enter numbers to average. Enter -1 to end")

# counter = 0
# total = 0

# while True:
#     counter += 1
#     num = int(input("Enter a number: "))
#     if num == -1:
#         break
#     total += num
#     avg = total/counter

# print("Average:", avg)

# range function
for i in range(5, 96, 5):
    print(i)

# break and continue
for i in range(10):
    if i == 7:
        continue
    else:
        print("i:", i)

for i in range(10):
    if i == 7:
        break
    else:
        print("i:", i)

# boolean operators
# and
# not
# or

age = 18
citizenship = False

if age == 18 and citizenship:
    print("You can vote!")
else:
    print("You can't vote")


key = True
pin = "false"

if key or pin:
    print("You can get into my parent's garage")
else:
    print("Why are you trying to break in?")


num1 = 4
num2 = 6

if num1 == 4 or num2 == 10:
    print("Those are great numbers!")
else: 
    print("I don't like those numbers")


can_vote = age >= 18
is_greater = 40 < 7