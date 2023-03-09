#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/19/23
#Description :

#outline for this project:

#exception for a player trying to play the game out of turn
class OutofTurn(Exception):
    pass

#exception for a player trying to use an invalid square or an invalid checker (not the player's checker)
class InvalidSquare(Exception):
    pass

#exception for an invalid player name
class InvalidPlayer(Exception):
    pass

class Square():
    """This class represents a square on the checkers board that has several private data members:
    the square color (string with value 'dark' or 'light'), its location as a tuple of integers, and the piece that
    is on the square object (None, 'Black', or 'White'). The square at location (0,0) is a light square that is the top
    left-most square on the board, and the square at location (7,7) is a light square that is the bottom right-most
    square on the board. The location tuple is in the following order: (row_number, column_number). """

    def __init__(self, square_color, square_location, square_piece=None):
        """initializes the square object with the passed in variables: the square color, the square location,
        and the piece that is on the square (default set to None). """
        self._square_color = square_color
        self._square_location = square_location
        self._square_piece = square_piece

    def get_square_color(self):
        """This get method returns the color of the square"""
        return self._square_color

    def get_square_location(self):
        """This get method returns the location of the square"""
        return self._square_location

    def get_square_piece(self):
        """This get method returns the piece on the square"""
        return self._square_piece


class Player():
    """This class represents a player in the checkers game/class that has several data members:
    the player name and the player piece color"""

    def __init__(self, player_name, piece_color):
        #initialize the player name and piece color
        self._player_name = player_name
        self._piece_color = piece_color

        #initialize the number of captured pieces
        self._captured_pieces = None

        #initialize an empty dictionary to store all of the player's pieces, with keys being the location of the piece
        #and its corresponding value being the piece string 'Black', 'White', 'Black_king', etc.
        self._pieces = {}


    def get_name(self):
        """This get method returns the name of the player object"""
        return self._player_name

    def get_color(self):
        """This get method returns the piece color of the player object"""
        return self._piece_color

    def get_king_count(self):
        """This get method returns the number of king pieces that the player has"""
        pass

    def get_triple_king_count(self):
        """This get method returns the number of triple king pieces that the player has"""
        pass

    def get_captured_pieces_count(self):
        """This get method returns the number of opponent pieces the player has captured"""
        return self._captured_pieces

class Checkers():
    """This is a class representing a game of checkers with 2 people, and stores information on
    the board and the players. """

    def __init__(self):
        #initialize a variable to tell which player's turn it is
        self._turn = None

    def create_player(self, player_name, piece_color):
        """This method creates a player object by calling the Player class and passing in the relevant variables,
        then returns that player object. The piece_color parameter must be a string of value 'Black' or 'White'"""
        return Player(player_name, piece_color)

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """This method takes as parameters the player's name, the location of the starting square and ending square.
        """

    def generate_board(self):
        """This method creates a generator object that can be called in the play_game() method to initialize
        a board."""

    def get_checker_details(self, square_location):
        """This method takes as parameter a square location and returns the checker details present in that square.
        checker details can be either None (no checker in that square), 'White', 'Black', 'Black_king', 'White_king',
        'Black_Triple_King', or 'White_Triple_King'"""

    def print_board(self):
        """This method prints out the current board in the form of an array."""

    def game_winner(self):
        """This method returns the name of the player that won the game, and returns 'Game has not ended' if there has
        not been a winner yet. There are two ways to win: either capture all opponent pieces or block all opponent
        pieces from moving"""


#DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
"""
1. Initializing the Checkers and Player classes
2. Determining how to implement create_player method
3. Determining how to implement print_board method
4. Determining how to implement game_winner method and how to check the winning condition
5. Determining how to implement play_game method; how to validate a move. Determine how to identify the promotion to king or triple king. Determine how to handle pieces being captured.
6. Determine how to implement get_checker_details method
7. Initializing exception classes 

"""
