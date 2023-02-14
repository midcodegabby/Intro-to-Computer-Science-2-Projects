#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description :

def row_puzzle(a_list, token=0, memo=None):
    """This recursive function takes as parameter a row (or list) of integers, with a zero at the highest index, and
    returns True if the puzzle is solvable for that row and False otherwise. The puzzle involves making the token,
    which starts at index 0, get to the last index of the list by moving to different index values (where the token can
    then move left or right the same number as the token's current indexed value), and the token cannot go out of
    the row's bounds. This function does not change the contents of the row."""

    #create dictionary to store already indexed values
    #if memo is None:
        #memo = {}

    #create base case
    if token == len(a_list):
        return True

    #create base case for bound limitations
    if token > len(a_list) or token < 0:
        return None

    left = row_puzzle(a_list, -a_list[token])
    right = row_puzzle(a_list, a_list[token])

    if





    if token not in memo:
        memo[token] = a_list[token] #adds the token's index and value to the dictionary

        if a_list[token] < len(a_list):
            return row_puzzle(a_list, a_list[token]-1,memo)

    if token in memo:
        token = a_list[token] - 1

lst = [4, 3,1, 2, 2, 0]

token = lst[0] - 1 #gives index
print(token)

token += lst[token]
print(token)

if token+1 == len(lst):
    print("yes")





