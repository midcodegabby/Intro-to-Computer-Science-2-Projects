#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description : This program contains a recursive function that takes as parameter a list of numbers and finds the
#highest value in the list (returns it). This program assumes the list contains at least one element.

def list_max(a_list, pos=0, high=0):
    """This recursive function takes as parameter a list of numbers and returns the maximum value in the list."""

    # create case for when the length of the list is 1
    if len(a_list) == 1:
        return a_list[pos]

    #create base case
    if pos + 1 == len(a_list):
        return high

    #define an intermediary variable for the current recursion element
    intermediary = a_list[pos]

    #create if statement to change value of intermediary if the high value is larger
    if high > intermediary:
        intermediary = high

    #if statement for doing a recursion
    if intermediary > a_list[pos+1]:

        return list_max(a_list, pos+1, intermediary)

    #elif statement for doing a recursion with a new high value
    elif intermediary <= a_list[pos+1]:

        #update the value of high
        high = a_list[pos + 1]
        return list_max(a_list, pos+1, high)


