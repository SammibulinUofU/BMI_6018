import sys

# Add 1 to every element of the most nested list using recursion

# Read in the input list from the command line
input_list = eval(sys.argv[1])

def recursive_method(input_list):
    # Define the base case #
    if type(input_list[-1]) == list:
        recursive_method(input_list[-1])
    # If the element is not a list, return x + 1 for all elements 
    else:
        new_list = list(map((lambda x: x+1), input_list))
        print(new_list)

# Function call
recursive_method(input_list)


