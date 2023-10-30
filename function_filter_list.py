import sys

"""
Write a python program that, given an input list, will filter the input 
above a user defined threshold. This is to be done with a standard function.
That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6),
 it should return [1,2,3,4,5,6]
"""

# The input list to filter
input_list = eval(sys.argv[1])
# The user provided threshold to filter the input list
user_threshold = eval(sys.argv[2])

def filterInputList(input_list, user_threshold):
    new_list = [x for x in range(len(input_list)) if x <= user_threshold]
    print(new_list)

filterInputList(input_list, user_threshold)

