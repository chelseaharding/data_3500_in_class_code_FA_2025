# # pseudo code

# # code rock paper scissors

# """
# Steps for solving/writing Rock, Paper, Scissors

# Input from users(s)
# or 
# Random input from computer

# Some kind of loop

# Giant if (comparison)
#     Make sure there are at least two inputs
#     if inputs are equal
#     if inputs are greater than or less than others

# if we find a result
#     print the result, if its a tie or if one or two wins
# """

# # Input from users(s)
# player1 = input("R, P, or S: ")
# player2 = input("R, P, or S: ")

# #Giant if (comparison)
# #Make sure there are at least two inputs
# if player1 == None or player2 == None:
#     print("Can't play")
# #if inputs are equal
# if player1 == player2:
#     print("It's a tie!")
# #if inputs are greater than or less than others
# elif player1 == "R":
#     if player2 == "P":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")
# elif player1 == "P":
#     if player2 == "R":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")
# elif player1 == "S":
#     if player2 == "P":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")

# # garbage collection

# import gc

# x = [1, 2, 3]

# y = x

# print("y:", y)

# del x

# gc.collect()

# debugger

peanut_allergy = True
lactose_intolerant = True

# see what foods we can have
if peanut_allergy and lactose_intolerant:
    print("You can't have peanut butter ice cream")
if peanut_allergy:
    print("You can't have this PB and J")
if lactose_intolerant:
    print("You can't have ice cream :(")
