# dynamic types

print("I love wednesdays because they are so fun!")
how_much_i_love_wed = 27
print("this is how much I love wednesday: " + str(how_much_i_love_wed))

# eval()

# age = input("How old are you: ")
# print("You are " + eval(age) + " years old.")

# # age = input("How old will you be next year: ")
# # age = age - 1
# # print("That means you are", age, "years old this year!")

# # x = 23

# # x = "hello everyone"

# # float()
# # str()
# # int()
# # bool()
# # eval()

# # if statements

# # if ____ <= _____:
# #     # do some kind of logic

# erin_vote = int(input("enter the votes for Erin: "))
# isaac_vote = int(input("enter the votes for isaac: "))

# if erin_vote > isaac_vote:
#     print("Erin wins!")
# elif erin_vote < isaac_vote:
#     print("Isaac wins!")
# elif erin_vote == isaac_vote:
#     print("It's a tie. Co-presidents!")
# else:
#     print("something is wrong")

# # input


# # min max range
# num1 = int(input("enter a number:"))
# num2 = int(input("enter a number:"))
# num3 = int(input("enter a number:"))

# print(min(num1, num2, num3))


# Aggie Basketball

"""
If you are a student, you get in for free
If you have HURD premium, you get 15 min early
If you aren't either of these, you need to buy a ticket
If you're faculty, you still need to buy a ticket, but you get a discount
"""

student = input("Are you a USU student: (yes/no)")
HURD    = input("Are you a member of HURD premium: (yes/no)")
faculty = input("Are you USU faculty: (yes/no)")

# if student == "yes":
#     print("you get in for free!")
# elif HURD == "yes":
#     print("you get in 15 min early!")
# elif student == "no":
#     print("you need to buy a ticket.")
# elif faculty == "yes":
#     print("you wish you got for free, but you still need to pay some money")

if student == "yes":
    print("you get in for free!")
if HURD == "yes":
    print("you get in 15 min early!")
if student == "no":
    print("you need to buy a ticket.")
if faculty == "yes":
    print("you wish you got for free, but you still need to pay some money")
