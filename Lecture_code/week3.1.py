print("hello everyone, I love Mondays!")

# variables
# one = 1
# 1 = 2 # can't do this!
# float = 3.14 # can't do this!
# list
# int
# str

day_of_the_week = "Monday"
day = "Monday"
favDay = "Wednesday"
age = 20
is_raining = False

# math
age = 25
print("age:", age)

age = age + 1
# 26
print("age:", age)
age = age - 1
# 25
print("age:", age)
age = age * 2
# 50
print("age:", age)
age = age / 2
# 25
print("age:", age)
age = age // 2
# 12
print("age:", age)
age = age % 2
# 0
print("age:", age)

# print statements
print("Hello everyone!")
print("\n")
print("test")

welcome_message = '''
Hello, welcome to the interactive __________ program!

To begin using the program, please type your name:
'''

print(welcome_message)

"""
For each problem, write a comment just before the code specifying the problem number
i.e.
# 2.3
if grade >= 90:
"""


# examples

"""
Professor Harding is running a half marathon - she ran 10 miles in 1 hr 18 min with a pace of about 7:42
For the half (13.2), what is her projected finish time? Print it out like this: "Projected Finish Time: hr:min:sec"
"""

minutes = 7
seconds = 42

pace = minutes * 60 + 42
print("pace in seconds:", pace)

half_distance = 13.2

half_time = half_distance * pace
print("half in seconds:", half_time)

projected_hours = int(half_time // 3600)
projected_mins  = int((half_time % 3600) // 60)
projected_secs  = int(half_time % 60)

print("Project Finish Time: " + str(projected_hours) + ":" + str(projected_mins) + ":" + str(projected_secs))

# art!
awesome = """
        |[FINISH]|
        |        |
        |        |
        
"""
print(awesome)

castle = """
        |>>>
        |
   _   _|  _
  |;|_|;|_|;|
  \\.     .//
   \\     //
    ||   ||
    ||   ||
    ||   ||
    ||_[]||

"""
print(castle)