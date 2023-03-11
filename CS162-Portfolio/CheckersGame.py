#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/19/23
#Description :

#exception for a player trying to play the game out of turn
class OutOfTurn(Exception):
    pass

#exception for a player trying to use an invalid square or an invalid checker (not the player's checker)
class InvalidSquare(Exception):
    pass

#exception for an invalid player name
class InvalidPlayer(Exception):
    pass


class Piece():
    """This class represents a piece on the checkers board that has several private data members:
    the piece color ('Black', 'White', 'Black_king', 'Black_Triple_King', etc.) and the piece's location as a tuple
    (row_number, column_number). If the piece has been captured then the piece object is deleted."""

    def __init__(self, piece_color, location):
        """initializing method that sets the piece object's piece color and location to the arguments passed in."""
        self._piece_color = piece_color
        self._location = location

    def set_piece_color(self, piece_color):
        """This set method allows the piece color to be changed. For example, this method allows a 'Black' piece
        to be turned into a 'Black_king' piece. No return value."""
        self._piece_color = piece_color

    def set_location(self, location):
        """This set method allows the location of the piece to be modified. In the event that a piece is captured,
        this method would be called to set its location to None. No return value."""
        self._location = location

    def get_piece_color(self):
        """This get method returns the color of the piece."""
        return self._piece_color

    def get_location(self):
        """This get method returns the location of the piece."""
        return self._location

def generate_pieces(row=0):
    """This generator function creates 24 pieces divided among two colors for the start of a checkers game, with
    the appropriate starting locations, and the value None in all other empty squares on the board, in correct order to
    be loaded onto a board later. The generator object created by this function will be used in the __init__
    method of the Board class, where the pieces/None values will be created and stored inside the Board object."""

    #create while loop to loop stuff
    while row <= 7:

        #if statement to filter out rows in the checkerboard that do not have starting white pieces
        if 0 <= row <= 2:

            #create another if/else statement to filter out odd vs even rows
            if row%2 == 0:

                #for loop iterates through a row
                for idx in range(0, 8):

                    #the next two conditionals make it so that None and the piece objects are placed in the correct
                    #order for a board when yielded.
                    if idx % 2 == 0:
                        yield None

                    else:
                        #yield each new white piece in the given even row
                        yield Piece("White", (row, idx))

                row += 1

            else:

                #for loop iterates through a row
                for idx in range(0, 8):

                    #the next two conditionals make it so that None and the piece objects are placed in the correct
                    #order for a board when yielded.
                    if idx % 2 != 0:
                        yield None

                    else:
                        #yield each new white piece in the given odd row
                        yield Piece("White", (row, idx))

                row += 1

        #if statement to filter out rows in the checkerboard that do not have starting black pieces
        elif 5 <= row <= 7:

            #create another if/else statement to filter out odd vs even rows
            if row%2 != 0:

                #for loop iterates through a row
                for idx in range(0, 8):

                    #the next two conditionals make it so that None and the piece objects are placed in the correct
                    #order for a board when yielded.
                    if idx % 2 != 0:
                        yield None

                    else:
                        #yield each new black piece in the given odd row
                        yield Piece("Black", (row, idx))

                row += 1

            else:

                #for loop iterates through a row
                for idx in range(0, 8):

                    #the next two conditionals make it so that None and the piece objects are placed in the correct
                    #order for a board when yielded.
                    if idx % 2 == 0:
                        yield None

                    else:
                        #yield each new black piece in the given even row
                        yield Piece("Black", (row, idx))

                row += 1

        #else statement moves the row from 3 to 5 so that the generator doesn't keep looping forever
        else:

            #for loop iterates through a row, yielding None for each empty square in rows 3 and 4
            for idx in range(0,8):
                yield None

            row += 1

class Board():
    """This class represents the board that the game checkers is played on, with 64 alternating light-dark squares in
    an 8 by 8 matrix. It has several private data members, including a board_dict representing the board."""

    def __init__(self):
        """This initializing method creates a Board object with the set requirements for starting:
        64 squares, with a white square in the top left and bottom right, alternating light-dark-light in a 8x8 matrix,
        with empty squares of either color holding a value of None. The values in the squares of the board are
        created by creating a generator object of the entire contents of a board (includes empty None squares and
        piece objects in non-empty squares) by calling the generate_pieces() generator function. This method then
        iterates over all the values in that generator objects and adds all the values to the board.
        The Board has a private data member, board_dict that represents the physical checkerboard.
        This board_dict has 8 key value pairs, with each key representing the row numbers (0-7), and each associated
        value being a list for that row containing piece objects or None. Example 0th row upon initializing the
        board object, with Piece_object referring to a unique piece object:
        [None, Piece_object, None, Piece_object, None, Piece_object, None, Piece_object]
        """
        #create variables to dictate the range of iteration
        high = 8
        low = 0

        #initialize the dictionary with keys being the row number on the board and corresponding values being empty
        #lists to store row contents
        self._board_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

        # initialize a generator object containing all values in the checkerboard by calling generate_pieces()
        initial_pieces = generate_pieces()

        #create for loop to populate the board_dict
        for key in self._board_dict:

            #loop through the range of iteration for a specific key and add each value of the generator object to the
            #list value in the board_dict
            for index in range(low, high):

                self._board_dict[key].append(next(initial_pieces))

            #shift range of iteration up by one row
            low += 8
            high += 8

    def get_board(self):
        """This method returns the board_dict"""
        return self._board_dict

    def move(self, piece, location):
        """This method allows for a piece to be moved, given the piece object and the specified moved to location.
        This method will have nested conditionals to prevent invalid moves. After a move is complete, the affected
        piece object data members will be updated. No return value."""
        pass

    def remove(self, piece):
        """This method allows for a piece to be removed from the board in the event of a capture.
        This method will call on the player object's (that did the capturing). No return value."""
        pass

    def get_piece(self, location):
        """This method returns the piece object that is at the passed in location."""

class Player():
    """This class represents a player in the checkers game/class that has several private data members:
    the player name and the player piece color"""

    def __init__(self, player_name, piece_color):
        """initializing method for creating a Player object with a player's name, piece color, None captured pieces,
        and an empty list representing the pieces (and each location) that a player has on the board. Then the
        same colored pieces as the player's piece_color are added to the piece_list."""
        #initialize the player name and piece color
        self._player_name = player_name
        self._piece_color = piece_color

        #initialize the number of captured pieces as 0
        self._captured_pieces = 0

        #initialize a list to store all of a player's pieces (piece objects)
        self._piece_list = []

    def remove_piece(self, piece):
        """Takes a piece object as parameter.
        This method allows the checkers class to remove a piece from the player's possession if it is captured
        by a different player by removing the captured piece from the player's piece_list. No returns."""
        pass

    def add_captured_piece(self):
        """This method adds 1 to the captured_pieces variable for every time the method is called, or every time
        the player captures an opponent piece. No return value."""
        self._captured_pieces =+ 1

    def get_name(self):
        """This get method returns the name of the player object"""
        return self._player_name

    def get_color(self):
        """This get method returns the piece color of the player object"""
        return self._piece_color

    def get_king_count(self):
        """This get method returns the number of king pieces that the player has. This will be done by iterating over
        the piece_list and adding 1 to a counter for every king in the list. The final counter value will be returned.
        """
        pass

    def get_triple_king_count(self):
        """This get method returns the number of triple king pieces that the player has This will be done by iterating
        over the piece_list and adding 1 to a counter for every triple king in the list. The final counter value will
        be returned."""
        pass

    def get_captured_pieces_count(self):
        """This get method returns the number of opponent pieces the player has captured"""
        return self._captured_pieces

class Checkers():
    """This is a class representing a game of checkers with 2 people, and completes checker moves."""

    def __init__(self):
        """Initializing method to create a turn variable, an empty dictionary of the game's players
         ((keys) player names and (values) player objects) and a board object"""
        self._turn = None
        self._checkers_board = Board()
        self._player_dict = {}

    def create_player(self, player_name, piece_color):
        """This method creates a player object by calling the Player class and passing in the relevant variables,
        then returns that player object and adds that player object to the players dictionary of this class.
        The piece_color parameter must be a string of value 'Black' or 'White'"""
        pass

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """This method takes as parameters the player's name, the location of the starting square and ending square.
        Then this method passes the player_name through a conditional to see if the player is allowed to make a move
        or not (if it is the player's turn). If it is not the player's turn, then the OutOfTurn exception is raised.
        Then this method uses another conditional to check if the piece object in the starting_square_location has
        the same color as the player; if it does not, then the InvalidSquare exception is raised. If the starting or
        destination square locations are invalid (any integer in the tuple is under 0 or above 7), then the
        InvalidSquare exception is called. Also, if the player_name is not valid then the InvalidPlayer exception is
        raised.
        Then the method calls on the board object's (checkers_board) move method to complete the necessary move passed
        into the play_game method as parameters. The board object's move method determines if the move is legal or not
        and raises the relevant exceptions if it is not legal. Lastly, after the play_game method is called successfully
        the number of captured pieces in the move and updates the self._turn variable accordingly (if any pieces are
        captured then the turn variable stays as the same player, if not then the turn variable changes to be the
        opponent player
        """
        pass

    def get_checker_details(self, square_location):
        """This method takes as parameter a square location and returns the checker details present in that square.
        checker details can be either None (no checker in that square), 'White', 'Black', 'Black_king', 'White_king',
        'Black_Triple_King', or 'White_Triple_King'. This method works by passing the square_location argument into
        a call to the board class method get_piece, then returning the returned piece's get_color method."""
        pass

    def print_board(self):
        """This method prints out the current board in the form of an array."""

        #get the board by calling the board object's get_board() method
        board_dict = self._checkers_board.get_board()

        #initialize an array that will hold strings and None values instead of piece objects
        board_array = []

        #initalize a temporary array to hold a row's contents
        temp_array = []

        #for loop to loop through all 'rows' in the board_dict
        for key in board_dict:

            #for loop to loop through all values in the row values in the value list corresponding to the current key
            for index in range(8):

                #conditional statement to handle None valued squares
                if board_dict[key][index] == None:

                    temp_array.append(None) #add the None value to the temporary array

                #else statement to handle squares that are not empty
                else:

                    #add the piece color to the temporary array
                    temp_array.append(board_dict[key][index].get_piece_color())

            #append the temporary array to the board_array
            board_array.append(temp_array)

            #clear the temp_array
            temp_array = []

        print(board_array)







    def game_winner(self):
        """This method returns the name of the player that won the game, and returns 'Game has not ended' if there has
        not been a winner yet. There are two ways to win: either capture all opponent pieces or block all opponent
        pieces from moving."""



game = Checkers()

game.print_board()

