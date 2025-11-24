"""
This question was asked by Google:

write a function that will, given a sorted list of integers, square the elements and give the output in a sorted order.
For example, given [-9, -2, 0, 2, 3] return [0, 4, 4, 9, 81]
"""

def square_list(integers):
    # square_sorted = []
    # for integer in integers:
    #     square_sorted.append(integer ** 2)
    square_sorted = [integer ** 2 for integer in integers]
    square_sorted.sort()
    return square_sorted

integer_list = [-101, -9, -2, 0, 2, 3]

print(square_list(integer_list))



date1 = "2025-11-18"
date2 = "2025-11-02"

print(date1 < date2)
        