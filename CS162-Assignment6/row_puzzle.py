#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description :

def row_puzzle(puz_list, token=0, puz_memo=None):
    """This recursive function takes as parameter a row (or list) of integers, with a zero at the highest index, and
    returns True if the puzzle is solvable for that row and False otherwise. The puzzle involves making the token,
    which starts at index 0, get to the last index of the list by moving to different index values (where the token can
    then move left or right the same number as the token's current indexed value), and the token cannot go out of
    the row's bounds. This function does not change the contents of the row."""

    #create dictionary to store already indexed values
    if puz_memo is None:
        puz_memo = {}

    #create base case
    if token == len(puz_list):
        return True

    #create movement variables
    move_right = token + puz_list[token]
    move_left = token - puz_list[token]

    #create if statement for case where a move to the right is in bounds
    if move_right <= len(puz_list):

        #update puzzle dict
        puz_memo[token] = puz_list[token] #links a move to the right with a token's index value

        return row_puzzle(puz_list, move_right, puz_memo)

    #create elif statement for case where a move to the right is out of bounds
    elif move_right > len(puz_list):

        #create if statement for case where a move to the left is out of bounds
        if move_left < 0:
            return False #this is a dead end for a puzzle, must do something else

        #create elif statement for case where a move to the left is in bounds
        elif move_left >= 0:

            #update puzzle dict
            puz_memo[token] = -puz_list[token]  # links a move to the left with a token's index value

            return row_puzzle(puz_list, move_left, puz_memo)

list = [2, 4, 5, 3, 1, 3, 1, 4, 0]
print(row_puzzle(list))




