# # augmented assignment

# age = 7
# age = age + 1
# age += 1
# print("age:", age)
# age -= 1
# print("age:", age)
# age *= 1
# print("age:", age)
# age /= 1
# print("age:", age)
# age %= 2
# print("age:", age)
# age **= 2
# print("age:", age)


# # for loops
# for i in range(1, 10 + 1):
#     print("i:", i)


# counter = 0

# for i in range(10):
#     counter += 2
#     print("counter:", counter)

# counter = 0
# aggies = "Go Aggies!"

# for i in aggies:
#     counter += 1
#     print("i:", i)
#     print("counter:", counter)


# # while loops
# age = 9
# while age <= 20:
#     print("you are", age, "years old!")
#     age += 1


# # guess the secret number!
import random
# secret_number = random.randint(1, 100)
# guess = int(input("Guess the secret number: "))

# while guess != secret_number:
#     if guess > secret_number:
#         print("Too high, guess again!")
#     elif guess < secret_number:
#         print("Too low, guess again!")
#     elif guess > 100:
#         print("The secret number is less than 100 (duh)")

#     guess = int(input("Guess the secret number: "))
# else:
#     print("You got it!")


# do it with a for loop
# secret_number = random.randint(1, 100)

# for i in range(20):
#     guess = int(input("Guess the secret number: "))
#     if guess > secret_number:
#         print("Too high, guess again!")
#     elif guess < secret_number:
#         print("Too low, guess again!")
#     elif guess > 100:
#         print("The secret number is less than 100 (duh)")
#     else:
#         print("You got it!")
#         break

# nested for loop
words = ["zamboni", "moist", "chocolate"]
for word in words:
    print("word:", word)
    for letter in word:
        print("letter:", letter)

# for loop
counter = 0
sum = 0
for i in range(100):
    sum += (1/(2**counter))
    print("Sum:", sum, "iteration:", counter)
    counter += 1