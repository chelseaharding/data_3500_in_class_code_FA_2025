'''
This problem was asked by Uber.

Given an list of integers, return a new list such that each element at index i of the new list is the product of all the numbers in the original list except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

# steps:
# - write down all tools you will need (loops, list, multiplication, etc.)
# - think through the logic and maybe draw a picture of how the steps go together
# - pseudocode 

# start with an input list

# loop through input list

# loop through input list inside loop??????

# if the number is not the index, multiply it by all others and keep track of sum in a variable

# input_list = [1, 2, 3, 4, 5]
# output_list = []

# for i in input_list:

#     # print("input_list[i]:", input_list[i])
#     # print("i:", i)

#     product = 1
#     for j in input_list:
#         if i == j:
#             continue
#         product *= j

#     output_list.append(product)

# print("output list:", output_list)


# i = 0
colors = ["blue", "red", "pink", "green"]

# for color in colors:
#     print("i:", i)
#     print("colors[i]:", colors[i])
#     i += 1


j = 0
print(colors[j])
print(colors[j+1])

for i in [1, 2, 3, 4, 5]:
    pass


# lists

ages = [22, 34, 98, 67]
ages.append(21)
print("ages:", ages)
ages.pop()
print("ages:", ages)
ages.pop(2)
print("ages:", ages)
ages.insert(2, 101)
print("ages:", ages)

# anagram

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word1_list = []
for letter in word1:
    word1_list.append(letter)

word2_list = []
for letter in word2:
    word2_list.append(letter)

word1_list.sort()
word2_list.sort()

if word1_list == word2_list:
    print("These words are anagrams")
else:
    print("These words are not anagrams")
