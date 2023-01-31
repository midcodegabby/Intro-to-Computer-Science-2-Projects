#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 1/11/23
#Description : This program is a modification of the basic binary search function that returns a TargetNotFound
#exception instead of a -1 when the target value is not in the list. When the target is found, the target's index
#is returned.

class TargetNotFound(Exception):
    pass

def binary_search(a_list, target):
    """
    Searches a_list for an occurrence of target.
    If the target is found, returns the index of its position in the list
    If the target is not found, raises the TargetNotFound exception, indicating that the target value isn't in the list
    """
    #define indices
    first = 0
    last = len(a_list) - 1

    #iterates as long as the first index is lesser or equal to the last index
    while first <= last:
        #define midpoint index
        middle = (first + last) // 2

        #create if statement for the case where the midpoint index value is the target value
        if a_list[middle] == target:
            return middle

        #create if statement for cases where the target is in the first half of the list
        if a_list[middle] > target:
            #updates last index so that while loop iterates over the first half of the list
            last = middle - 1

        #create else statement for cases where the target is in the second half of the list
        else:
            #updates first index so that the while loop iterates over the second half of the list
            first = middle + 1

    #only raised if the target is never found in the list
    raise TargetNotFound





