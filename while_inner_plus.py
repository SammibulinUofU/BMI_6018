import sys

# Add 1 to every element of the most nested list using a while loop

# Read in string from command line and convert to list
input_list = eval(sys.argv[1])

# Set flag to True to enter while loop 
flag = True
while flag:
    # Check if last element is list
    if type(input_list[-1]) == list:
        input_list = input_list[-1]
    else:
        # If last element is not a list, add 1 to every element and return
        new_list = list(map((lambda x: x+1), input_list))
        print(new_list)
        flag = False