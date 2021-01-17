# two functions that do the same operations on a list, except one is in-place and the other 
# is out-of-place

def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element

def square_list_out_of_place(int_list):
    #We allocate a new list with the length of the input list
    squared_list = [None] * len(int_list)

    for index, element in enumerate(int_list):
        square_list[index] = element ** 2
    
    return squared_list