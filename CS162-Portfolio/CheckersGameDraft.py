#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/8/23
#Description : outline for the CheckersGame portfolio project, with psuedocode, explanations, docstrings, and classes
#(with methods) explained in the following code.

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

    """The piece class communicates with the board class, where the board class stores all the pieces in a game of 
    checkers, the generator function generate_pieces(), which creates a generator object of starting pieces, and
    the checkers class which will call on piece object methods to change the piece color or location when pieces
    move or are captured or are promoted."""

    def __init__(self, piece_color, location):
        """initializing method that sets the piece object's piece color and location to the arguments passed in and
        sets the affiliation to 'on_board'."""
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

def generate_pieces():
    """This generator function creates 24 pieces divided among two colors for the start of a checkers game, with
    the appropriate starting locations. The generator object created by this function will be used in the __init__
    method of the Board class, where the pieces will be created and stored inside the Board object."""
    pass

class Board():
    """This class represents the board that the game checkers is played on, with 64 alternating light-dark squares in
    an 8 by 8 matrix. It has several private data members, including a board_dict representing the board."""

    """This class communicates with the checkers class and the piece class, where the checkers class calls on the 
    board class to move and remove pieces, while the board class uses piece objects in its board_dict, and also
    initializes a full starting set of pieces in the __init__ method."""

    def __init__(self):
        """This initializing method creates a Board object with the set requirements for starting:
        64 squares, with a white square in the top left and bottom right, alternating light-dark-light in a 8x8 matrix,
        the starting positions for all pieces (starting pieces are created in this method by iterating over a generator
        object that creates the objects), and the following syntax for empty squares: dark and light empty squares
        contain the value None.
        The Board has a private data member, board_dict that represents the physical checkerboard.
        This board_dict has 8 key value pairs, with each key representing the row numbers (0-7), and each associated
        value being a list for that row containing piece objects or . Example 0th row upon initializing the
        board object, with Piece_object referring to a unique piece object:
        [None, Piece_object, None, Piece_object, None, Piece_object, None, Piece_object]
        """
        pass

    def get_board(self):
        """This method returns the board_dict"""
        pass

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

    """This class is used by the checkers() class to keep track of the amount of pieces each player has captured and
    their pieces' locations."""

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

    """this class interacts and calls the board, player, and piece classes in its methods."""

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
        pass

    def game_winner(self):
        """This method returns the name of the player that won the game, and returns 'Game has not ended' if there has
        not been a winner yet. There are two ways to win: either capture all opponent pieces or block all opponent
        pieces from moving."""


#DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
"""
1. Initializing the Checkers and Player classes:
When the checkers class is initialized, the checkers() __init__ method causes the turn variable to be set to None,
initializes the player_dict to be an empty dictionary and 
creates a new Board() object by assigning the Board call to a private data member called checkers_board. By doing this, 
the new board object initializes (through the board() __init__ method) the starting pieces by creating a generator
object of the starting pieces by calling the generate_pieces() function and iterating over the pieces, adding those
pieces to a board_dict that will contain all the squares in a checkerboard (each square either has its color ('dark'
or 'light') as its value in the board_dict or a piece object), with the board_dict key-value pairs consisting of 
(key) row number, 0-7 and (value) list of values in that row (either square color or piece object). When the Player
class is initialized (player object is created) through the player() __init__ method, the player's name and color are
passed in and allocated to private data members within the player object, a list of a player's pieces is set to an empty
list (and then the relevant pieces of the player's color are added to that list), and the number of captured pieces
for that player is set to 0.

2. Determining how to implement create_player method
The create_player method first checks if there are already 2 players; if there is then the create_player method does 
not allow a new player to be created; if there is not then the create_player method adds a new entry to the player_dict
dictionary with key being the argument player_name, and the value being a player object created from a call to the 
player class with the given parameters in the create_player method. 

3. Determining how to implement print_board method
The board being used in the Checkers class is a Board object, where the board object contains a dictionary board_dict
that contains 8 key value pairs of (key: row number, 0-7 and value: list of row contents). Given this information, the 
print_board method calls the board object's get_board() method (which returns the board_dict), then prints out each 
value in the dictionary (each value is a list of the board contents for a specific row) separated by line, but 
each value in that list that is not None has the piece method get_color() called on it then printed out (because
each non-None value in the list for a value in the dictionary is a piece object). The line separation will not 
occur if I misread the instructions and all board values must be printed out in one array. 

4. Determining how to implement game_winner method and how to check the winning condition
The game_winner method first checks if any one player has 12 captured pieces; if one does, then the game_winner 
method returns that player's name by calling the get_player_name() on that player object. If neither player has 12
captured pieces then the game_winner method checks if any one player is unable to move any of their pieces 
(although I have not figured out how to test for this yet). If any player is unable to make a move then the other 
player's name is returned as the winner. If neither of these situations happen a string is returned with value 
"Game has not ended". 

5. Determining how to implement play_game method; how to validate a move. Determine how to identify the promotion to 
-king or triple king. Determine how to handle pieces being captured.
Captured pieces are handled by the following: The player that had the piece has the piece removed from their piece_list, 
the piece that has been captured has its location set to None, the board object has its remove() method called using 
the captured piece, therefore removing it from the board, and the player that captured the piece has a 1 added to their
captured_pieces data member. Moves are validated inside the move() method in the Board object, by using a large amount
of conditionals that filter out different piece colors/statuses and check the move according to the rules governing
regular, king, and triple king pieces. Promotions are done by the following: in the play_game method there will be 
conditional statements for checking if a regular piece has gotten to the other side of the board; if it has then the 
piece's piece_color is changed by calling the set_piece_color() method on that piece object and changing its value to 
be king, and a different conditional checks for if a king piece has reached its initial side and modifies its 
piece_color data member in the same process as in the regular-king piece promotion process. The play_game method will
first check for do exception handling for if a player_name argument is invalid, if a player does not own the piece
designated by the starting_square_location or if the starting or destination square locations are invalid. Then the
play_game method will call on the board object move() method to complete the move inside the board_dict and update
the relevant piece locations or whatever else.

6. Determine how to implement get_checker_details method
The get_checker_details first checks if the square_location parameter is on the board; if it is not then it raises
the InvalidSquare exception. Then the get_checker_details method
calls the board object get_piece() method (on the passed in location), which will return 
None if no piece is at that location, or return the piece at that location. Now that the piece object has been found,
the get_checker_details method returns a call to that piece object's get_piece_color() method, which will return 
the piece string value ('Black', 'White', 'White_Triple_King', etc.).

7. Initializing exception classes 
The Exception classes are already initialized under the description portion of this code.

"""

