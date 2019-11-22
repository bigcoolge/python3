"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    if len(input_array) == 1:
        if value == input_array[0]:
            return 0
    elif len(input_array) > 1:
        head = 0
        tail = len(input_array) - 1
        while head <= tail:
            index = (head + tail) >> 1
            print("head == " + str(head) + " | " + "tail == " + str(tail))
            print("index ==" + str(index) + " | " + str(input_array[index]))
            if value == input_array[index]:
                return index
            elif value < input_array[index]:
                tail = index - 1
            else:
                head = index + 1
    return -1


test_list = [1,3,9,11,15,19,29]
# test_val1 = 25
# print(binary_search(test_list, test_val1))
# test_val2 = 15
# print(binary_search(test_list, test_val2))
test_val3 = 2
print(binary_search(test_list, test_val3))
