#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description :

def list_max(a_list, pos=0, val=0):
    """This recursive function takes as parameter a list of numbers and returns the maximum value in the list."""

    #create base case
    if a_list[pos] ==0:
        print(0)

    if a_list[pos] > a_list[pos+1]:
