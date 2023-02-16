#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/15/23
#Description : This program contains a recursive function row_puzzle that takes as parameter a list of integers with
#a zero at the end, a default argument token that serves as the current index in the recursion and a default argument
#puz_memo that is a dictionary of already visited indices in the list. The function's goal is to return True if the
#token can be moved to the 0 at the end of the list by moving the token left or right by the same value as its current
#index recursively multiple times, and False otherwise. This function also does not change the order or contents of
#the list being solved.

def row_puzzle(puz_list, token=0, puz_memo=None):
    """This recursive function takes as parameter a row (or list) of integers (puz_list), with a zero at the highest
    index, and returns True if the puzzle is solvable for that row and False otherwise. The puzzle involves
    making the token, which starts at index 0, get to the last index of the list by moving to different index values
    (where the token can then move left or right the same number as the token's current indexed value),
    and the token cannot go out of the row's bounds. This function does not change the contents of the row.
    This function uses a dictionary puz_memo to hold indices in the list (keys) and their corresponding movements
    from that index (values)."""

    #initialize dictionary to store already indexed values
    if puz_memo is None:
        puz_memo = {}

    #create base case
    if token + 1 == len(puz_list):
        return True

    #create movement variables
    move_right = token + puz_list[token]
    move_left = token - puz_list[token]

    #create if statement for case where a move to the right is in bounds and the index has not yet been visited
    if move_right < len(puz_list) and move_right not in puz_memo:

        ##links a move to the right with a token's index value
        puz_memo[token] = puz_list[token]

        return row_puzzle(puz_list, move_right, puz_memo) #recursive step

    #create elif statement for case where a move to the right is in bounds and the index has already been visited
    #this will contain if statements that cause a move to the left instead of a move to the right for that index
    elif move_right < len(puz_list) and move_right in puz_memo:

        #create if statement for case where a move to the left is out of bounds (dead end, puzzle has no solution)
        if move_left < 0:
            return False

        #create elif statement for case where a move to the left is in bounds
        elif move_left >= 0:

            #link a move to the left with a token's index value in the puz_memo
            puz_memo[token] = -puz_list[token]

            return row_puzzle(puz_list, move_left, puz_memo) #recursive step

    #create elif statement for case where a move to the right is out of bounds
    elif move_right >= len(puz_list):

        #create if statement for case where a move to the left is out of bounds (dead end, puzzle has no solution)
        if move_left < 0:
            return False

        #create elif statement for case where a move to the left is in bounds
        elif move_left >= 0:

            #link a move to the left with a token's index value in the puz_memo
            puz_memo[token] = -puz_list[token]

            return row_puzzle(puz_list, move_left, puz_memo) #recursive step

