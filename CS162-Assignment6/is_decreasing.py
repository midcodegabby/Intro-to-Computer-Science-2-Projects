#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description : This program contains a function is_decreasing that takes as parameter a list of numbers and
#returns True if the list is strictly decreasing and false if not. Strictly decreasing refers to all elements in the
#list being smaller than their previously indexed element, not equal to or smaller than. This program assumes that
#the list has at least 2 elements.

def is_decreasing(a_list, pos=0):
    """This function takes as a parameter a list of no less than 2 numbers and returns True if the list is
    strictly decreasing and False otherwise. The pos default argument tracks the index of the list."""

    #define base case
    if pos + 1 == len(a_list):
        return True

    #create if statement to continue the recursion for when the first element in the recursion is greater than the
    #next element
    if a_list[pos+1] < a_list[pos]:
        return is_decreasing(a_list, pos+1)

    else:
        return False
