#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/17/23
#Description : This program allows two people to play a game of Checkers. The program uses exceptions to prevent
#invalid moves, a Piece class that represents each piece on the checker board, a generator function generate_pieces()
#that creates a generator object containing all the starting values in the checker board at the start of the game
#(including initial pieces and None values for empty squares), a Player class that represents one of two people
#playing checkers, a Board class that represents the checker board and keeps track of all the locations of the
#pieces, and finally a Checkers class that represents the actual game being played, which uses all the other classes
#within itself to successfully allow the checkers game to be played. While the ReadMe for this project specified
#only 3 exception classes, I added another one called InvalidMove that is raised when a player makes a move that cannot
#be made with the piece chosen (for example, a king trying to capture 2 enemy pieces in one move).

#IMPORTANT NOTE: I coded in the InvalidMove exception, along with a massive amount of if/else statements in
#the play_game() method to ensure that players cannot make an invalid move (say, try to jump 2 consecutive friendly
#pieces with a triple king piece). This is definitely overkill, as according to the readme the program assumes that
#players play according to the rules and that we only need to handle InvalidSquares, InvalidPlayers, and OutofTurn.
#however, I felt that I wanted to make a completely fool-proof checker game program, and this is what I ended up with.
#please enjoy my hard work and overkill!

#exception for a player trying to play the game out of turn
class OutofTurn(Exception):
    pass

#exception for a player trying to use an invalid square or an invalid checker (not the player's checker)
class InvalidSquare(Exception):
    pass

#exception for an invalid player name
class InvalidPlayer(Exception):
    pass

#exception for an invalid move
class InvalidMove(Exception):
    pass

class Piece():
    """This class represents a piece on the checkers board that has 2 private data members:
    the piece color ('Black', 'White', 'Black_king', 'Black_Triple_King', etc.) and the piece's location as a tuple
    (row_number, column_number). If the piece has been captured then the piece object's location is set to None.
    The piece object is initialized with a passed in piece_color and square_location."""

    def __init__(self, piece_color, square_location):
        """initializing method that sets the piece object's piece color and location to the arguments passed in."""
        self._piece_color = piece_color
        self._square_location = square_location

    def set_piece_color(self, piece_color):
        """This set method allows the piece color to be changed. For example, this method allows a 'Black' piece
        to be turned into a 'Black_king' piece. No return value."""
        self._piece_color = piece_color

    def set_square_location(self, square_location):
        """This set method allows the location of the piece to be modified. In the event that a piece is captured,
        this method would be called to set its location to None. No return value."""
        self._square_location = square_location

    def get_piece_color(self):
        """This get method returns the color of the piece."""
        return self._piece_color

    def get_square_location(self):
        """This get method returns the location of the piece."""
        return self._square_location

def generate_pieces(row=0):
    """This generator function creates 24 pieces divided among two colors for the start of a checkers game, with
    the appropriate starting locations, and the value None in all other empty squares on the board, in correct order to
    be loaded onto a board later. The generator object created by this function will be used in the __init__
    method of the Board class, where the piece objects and None values will be created and stored inside the Board
    object."""

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
    """This class represents the board that the game of checkers is played on, with 64 alternating light-dark squares in
    an 8 by 8 matrix. It has one private data member, which is a board_dict representing the board."""

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

        #initialize a generator object containing all values in the checkerboard by calling generate_pieces()
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
        """This method returns the board_dict and takes no parameters"""
        return self._board_dict

    def move(self, piece, destination_square_location):
        """This method takes a piece object and a destination square location as parameters and
        allows for a piece to be moved on the board_dict, given the piece object and the specified moved
        to location. After a move is complete, the affected piece and player object data members will be updated."""

        #unpack the piece's starting and destination location
        start_row, start_col = piece.get_square_location()
        destination_row, destination_col = destination_square_location

        #reassign piece's location to be the destination_square_location
        piece.set_square_location(destination_square_location)

        #change the piece's start location on the board to None
        self._board_dict[start_row][start_col] = None

        #change the piece's destination location on the board to be the piece object
        self._board_dict[destination_row][destination_col] = piece

    def remove(self, piece):
        """This method allows for a piece to be removed from the board in the event of a capture and takes the piece
        object that will be removed as parameter. This method updates the piece's square_location data member and
        where the piece is on the board_dict.
        no returns."""

        #remove the piece from the board by looping through all values inside the board_dict and removing the piece
        for key in self._board_dict:

            for index in self._board_dict[key]:

                #if statement handles the removal of the piece once the piece is reached
                if index == piece:

                    #unpack the square_location to use
                    row, col = piece.get_square_location()

                    #set the piece to be removed location on the board to be None
                    self._board_dict[row][col] = None

                    #call on the piece object's set_square_location to change its location to None
                    piece.set_square_location = None

    def get_square_details(self, square_location):
        """This method returns the piece object that is at the passed in location."""

        #split the tuple square_location into two different variables
        row, col = square_location

        #use conditional statements to prevent invalid square_locations from being used
        if 0 <= row <= 7 and 0 <= col <= 7:

            #create conditional statements to seperate None valued squares and squares that have a piece object in them
            if self._board_dict[row][col] == None:
                return None

            else:
                return self._board_dict[row][col].get_piece_color()

        else:

            raise InvalidSquare

class Player():
    """This class represents a player in the checkers game/class that has 4 private data members:
    the player name, the player piece color, a value of how many pieces the player has captured, and a list of all
    the player's pieces. The Player object takes a string name and checker_color as parameters upon initialization."""

    def __init__(self, player_name, checker_color):
        """initializing method for creating a Player object with a player's name, piece color, None captured pieces,
        and an empty list representing the pieces (and each location) that a player has on the board."""

        #initialize the player name and piece color
        self._player_name = player_name
        self._checker_color = checker_color

        #initialize the number of captured pieces as 0
        self._captured_pieces = 0

        #initialize a list to store all of a player's pieces (piece objects)
        self._piece_list = []

    def initialize_pieces(self, board_dict):
        """This method initializes the pieces of the player object without creating an entirely new generator object
        that has different piece objects than the pieces on the board by being called in the create_player() method of
        the Checkers object and using the board_dict in that checker_board object in the checkers object. This
        method takes the board_dict being used in the checkers object as parameter. No returns."""

        #create for loop to loop through all pieces in the board_dict
        for key in board_dict:

            for index in board_dict[key]:

                #if statement to filter out None valued squares in the board_dict
                if index == None:
                    pass

                #elif statement to filter out pieces that are not the player's checker color
                elif index.get_piece_color() != self._checker_color:
                    pass

                #else statement handles all pieces that are the same color as the player's checker color
                else:

                    #append each piece object of the player's color to the player's piece_list
                    self._piece_list.append(index)

    def remove_piece(self, piece):
        """Takes a piece object as parameter.
        This method allows the checkers class to remove a piece from the player's possession if it is captured
        by a different player by removing the captured piece from the player's piece_list. No returns."""

        #loop through the player's piece_list to find the piece to be removed
        for index in self._piece_list:

            #if statement removes the piece in the player's piece_list that is the same as the parameter piece
            if index == piece:

                self._piece_list.remove(piece)

    def add_captured_piece(self):
        """This method adds 1 to the captured_pieces variable for every time the method is called, or every time
        the player captures an opponent piece. No return value. Takes no parameters."""
        self._captured_pieces += 1

    def get_player_name(self):
        """This get method returns the name of the player object. Takes no parameters."""
        return self._player_name

    def get_checker_color(self):
        """This get method returns the piece color of the player object. Takes no parameters."""
        return self._checker_color

    def get_piece_list(self):
        """This get method returns the entire list of the player's piece objects. Takes no parameters."""
        return self._piece_list

    def get_king_count(self):
        """This get method returns the number of king pieces that the player has. This will be done by iterating over
        the piece_list and adding 1 to a counter for every king in the list. The final counter value will be returned.
        Takes no parameters.
        """
        #initialize a counter variable for king pieces
        king_count = 0

        #initialize a string with value "checkercolor_King"
        king_str = self._checker_color + "_King"

        #loop through the pieces in the player's piece_list
        for index in self._piece_list:

            #if statement adds one to the king counter every time the indexed piece has a king piece_color value
            if index.get_piece_color() == king_str:

                king_count += 1

        return king_count

    def get_triple_king_count(self):
        """This get method returns the number of triple king pieces that the player has. This will be done by iterating
        over the piece_list and adding 1 to a counter for every triple king in the list. The final counter value will
        be returned. Takes no parameters."""

        #initialize a counter variable for triple king pieces
        triple_king_count = 0

        #initialize a string with value "checkercolor_Triple_King"
        triple_king_str = self._checker_color + "_Triple_King"

        #loop through the pieces in the player's piece_list
        for index in self._piece_list:

            #if statement adds one to the king counter every time the indexed piece has a triple king piece_color value
            if index.get_piece_color() == triple_king_str:
                triple_king_count += 1

        return triple_king_count

    def get_captured_pieces_count(self):
        """This get method returns the number of opponent pieces the player has captured. Takes no parameters."""
        return self._captured_pieces

class Checkers():
    """This is a class representing a game of checkers with 2 people, and completes checker moves. It has
    3 private data members, a turn variable that holds a string of value "Black", or "White", a board object
    called checkers_board, and a dictionary containing 2 Player names and their corresponding Player objects.
    No parameters are needed for initialization. """

    def __init__(self):
        """Initializing method to create a turn variable (set to "Black") an empty dictionary of the game's players
         ((keys) player names and (values) player objects) and a board object"""

        self._turn = "Black"
        self._checkers_board = Board()
        self._player_dict = {}

    def get_board_object(self):
        """This get method returns the board object used in this checkers object"""
        return self._checkers_board

    def create_player(self, player_name, checker_color):
        """This method creates a player object by calling the Player class and passing in the relevant variables,
        then returns that player object and adds that player object to the players dictionary of this class.
        The piece_color parameter must be a string of value 'Black' or 'White'. Takes a player_name and
        a checker_color as parameters."""

        #if statement to handle invalid color parameter
        if checker_color != "Black" and checker_color != "White":

            return "Invalid checker color: can only choose 'Black' or 'White', not " + checker_color

        #this elif statement handles the creation of the first player
        elif len(self._player_dict) == 0:

            #add the new player to the player_dict then return the player object
            self._player_dict[player_name] = Player(player_name, checker_color)

            #initialize the player's initial pieces by using the same pieces that are in the board object
            self._player_dict[player_name].initialize_pieces(self._checkers_board.get_board())

            return self._player_dict[player_name]

        #create conditional statements to prevent more than two players being created or other edge cases
        elif len(self._player_dict) == 1:

            #nested if statements to prevent a player object being created that has the same color as the other player
            if next(iter(self._player_dict.values())).get_checker_color() == checker_color:

                return "Checker color taken, please choose the other color!"

            #nested elif statement to prevent duplicate names
            elif next(iter(self._player_dict.values())).get_player_name() == player_name:

                return "Name taken, please choose a different name!"

            else:

                #add the new player to the player_dict then return the player object
                self._player_dict[player_name] = Player(player_name, checker_color)

                #initialize the player's initial pieces by using the same pieces that are in the board object
                self._player_dict[player_name].initialize_pieces(self._checkers_board.get_board())

                return self._player_dict[player_name]

        else:

            raise InvalidPlayer

    def get_players(self):
        """This get method returns the dictionary of player objects. Takes no parameters."""
        return self._player_dict

    def promote(self, piece, piece_color):
        """This method takes a piece object and its piece_color data member as parameters. This method allows other
        checkers methods (specifically play_game()) to call this method to perform a promotion. This method assumes that
        the piece is only promoted or this method is only called when the sufficient conditions for the piece's
        promotion are met. No return value."""

        #create if/elif statements to do different promotions based on what level the piece is
        if "King" not in piece_color:

            piece.set_piece_color(piece_color + "_King")

        elif piece_color == "Black_King":

            piece.set_piece_color("Black_Triple_King")

        else:

            piece.set_piece_color("White_Triple_King")

    def capture(self, piece):
        """This method allows other checkers methods to call this function to capture a piece and update the captured
        piece's location, the checkers_board's piece location, and the player's piece_list. No returns and takes
        a piece object to be captured as parameter."""

        #simplify the piece's color
        piece_color = piece.get_piece_color()

        #remove the piece from their respective player's piece list and add to the other player's captured_pieces
        #data member
        for key in self._player_dict:

            #remove the piece from the same colored player
            if self._player_dict[key].get_checker_color() in piece_color:

                #remove the piece from the player's piece list by calling the remove_piece() method of the player object
                self._player_dict[key].remove_piece(piece)

            else:

                #add to the captured_pieces data member of the player that did the capturing
                self._player_dict[key].add_captured_piece()

        #remove the piece from the checkers_board object (calling the remove() method also sets the piece's location
        #to None hence why we do not set it equal to None in this method
        self._checkers_board.remove(piece)

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """This method takes as parameters the player's name and the location of the starting square and ending square.
        Then this method passes the player_name through a conditional to see if the player is allowed to make a move
        or not (if it is the player's turn). If it is not the player's turn, then the OutofTurn exception is raised.
        Then this method uses another conditional to check if the piece object in the starting_square_location has
        the same color as the player; if it does not, then the InvalidSquare exception is raised. If the starting or
        destination square locations are invalid (any integer in the tuple is under 0 or above 7), then the
        InvalidSquare exception is called. Also, if the player_name is not valid then the InvalidPlayer exception is
        raised. There are numerous nested conditionals in this method to determine if a move is legal or not and
        raise the InvalidMove exception accordingly, as well as move a piece in accordance to its status in color or
        regular/king/triple king. Then this method calls the move() method from the checkers_board object, which
        makes the move on the board_dict and updates the piece's location data member. Lastly, after the play_game
        method is called successfully, the number of captured pieces in the move is returned and the method updates the
        self._turn variable accordingly (if any pieces are captured then the turn variable stays as the same player,
        if not then the turn variable changes to be the opponent player). If the piece needs to be promoted then the
        method also calls the promote() method on the to be promoted piece.
        """

        #define the board_dict in the checkers_board object to shorten lines
        board_dict = self._checkers_board.get_board()

        #unpack starting_square_location and destination_square_location tuples
        start_row, start_col = starting_square_location
        destination_row, destination_col = destination_square_location

        #define a temporary row and column number for use in iteration that "start" at the
        #start position of the piece
        temp_row = start_row
        temp_col = start_col

        #create an empty list to store the enemy pieces between the start and
        #destination squares
        enemy_pieces = []

        #create space-saving booleans:
        row_diff = destination_row - start_row
        col_diff = destination_col - start_col

        #if statement handles invalid player_name
        if player_name not in self._player_dict:

            raise InvalidPlayer

        #elif statement handles player trying to move when not their turn
        elif self._turn != self._player_dict[player_name].get_checker_color():

            raise OutofTurn

        else:

            #define player object to shorten code
            player = self._player_dict[player_name]

            #store the initial number of captured pieces that a player has
            initial_cap = player.get_captured_pieces_count()

            #check if the starting_square_location and destination_square_location are valid using conditionals
            if 0 <= start_row <= 7 and 0 <= start_col <= 7 and 0 <= destination_row <= 7 and 0 <= destination_col <= 7:

                #define positions on the board to shorten code (these can either refer to None or the piece object
                #in that square)
                start_square = board_dict[start_row][start_col]
                destination_square = board_dict[destination_row][destination_col]

                #check if the piece at the location is not None
                if start_square == None:

                    raise InvalidSquare

                #use elif statement to check if the piece on the start_square is not the same color as the player's
                #checker color:
                elif player.get_checker_color() not in start_square.get_piece_color():

                    raise InvalidSquare

                #else statement handles a situation where the player's checker color is the same as the piece in the
                #given starting location
                else:

                    #use if statement to prevent moves from happening that have a non-None destination square location
                    if destination_square == None:

                        #create conditionals to filter different piece_types (i.e. kings, triple kings, and color)
                        if start_square.get_piece_color() == "White":

                            #if statement handles non-capture moves
                            if destination_row == start_row+1 and (destination_col == start_col+1 or destination_col == start_col-1):

                                #call the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                #if statement to check if promotion is required
                                if destination_row == 7:

                                    #call the promote() method to perform the promotion
                                    self.promote(start_square, start_square.get_piece_color())

                                #change the turn to the other player
                                for key in self._player_dict:
                                    if key != player_name:
                                        self._turn = self._player_dict[key].get_checker_color()

                            #elif statement handles capture moves to the right
                            elif destination_row == start_row+2 and destination_col == start_col+2:

                                #conditional handles if the jumped over square is empty
                                if board_dict[start_row+1][start_col+1] == None:

                                    raise InvalidMove

                                #conditional statement handles if the jumped over square has a friendly piece
                                elif player.get_checker_color() in board_dict[start_row+1][start_col+1].get_piece_color():

                                    raise InvalidMove

                                #else statement handles a valid capture move to the right
                                else:

                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row + 1][start_col + 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #if statement to check if promotion is required
                                    if destination_row == 7:
                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            #elif statement handles capture moves to the left
                            elif destination_row == start_row + 2 and destination_col == start_col - 2:

                                #conditional handles if the jumped over square is empty
                                if board_dict[start_row + 1][start_col - 1] == None:

                                    raise InvalidMove

                                #conditional statement handles if the jumped over square has a friendly piece
                                elif player.get_checker_color() in board_dict[start_row + 1][start_col - 1].get_piece_color():

                                    raise InvalidMove

                                #else statement handles a valid capture move to the left
                                else:

                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row + 1][start_col - 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #if statement to check if promotion is required
                                    if destination_row == 7:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            else:

                                raise InvalidMove

                        elif start_square.get_piece_color() == "Black":

                            #if statement handles non-capture moves
                            if destination_row == start_row - 1 and (destination_col == start_col + 1 or destination_col == start_col - 1):

                                #call the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                #if statement to check if promotion is required
                                if destination_row == 0:

                                    #call the promote() method to perform the promotion
                                    self.promote(start_square, start_square.get_piece_color())

                                #change the turn to the other player
                                for key in self._player_dict:
                                    if key != player_name:
                                        self._turn = self._player_dict[key].get_checker_color()

                            #elif statement handles capture moves to the right
                            elif destination_row == start_row - 2 and destination_col == start_col + 2:

                                #conditional handles if the jumped over square is empty
                                if board_dict[start_row - 1][start_col + 1] == None:

                                    raise InvalidMove

                                #conditional statement handles if the jumped over square has a friendly piece
                                elif player.get_checker_color() in board_dict[start_row - 1][start_col + 1].get_piece_color():

                                    raise InvalidMove

                                #else statement handles a valid capture move to the right
                                else:

                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row - 1][start_col + 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #if statement to check if promotion is required
                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            #elif statement handles capture moves to the left
                            elif destination_row == start_row - 2 and destination_col == start_col - 2:

                                #conditional handles if the jumped over square is empty
                                if board_dict[start_row - 1][start_col - 1] == None:

                                    raise InvalidMove

                                #conditional statement handles if the jumped over square has a friendly piece
                                elif player.get_checker_color() in board_dict[start_row - 1][start_col - 1].get_piece_color():

                                    raise InvalidMove

                                #else statement handles a valid capture move to the left
                                else:

                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row - 1][start_col - 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #if statement to check if promotion is required
                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            else:

                                raise InvalidMove

                        #both colored king checkers have same movement rules
                        elif start_square.get_piece_color() == "Black_King" or start_square.get_piece_color() == "White_King":

                            #non capture move code
                            if (destination_row == start_row + 1 or destination_row == start_row - 1) and (destination_col == start_col + 1 or destination_col == start_col - 1):

                                #call the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                #if statement to check if promotion is required
                                #this if statement handles black king promotions
                                if "Black" in start_square.get_piece_color():

                                    if destination_row == 7:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                                #this else statement handles white king promotions
                                else:

                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                                #change the turn to the other player
                                for key in self._player_dict:
                                    if key != player_name:
                                        self._turn = self._player_dict[key].get_checker_color()

                            #if statement handles capture moves down and to the right:
                            elif row_diff == col_diff and row_diff > 0 and col_diff > 0:

                                #define a temporary row and column number for use in iteration that "start" at the
                                #start position of the piece
                                temp_row = start_row
                                temp_col = start_col

                                #create an empty list to store the enemy pieces between the start and
                                #destination squares
                                enemy_pieces = []

                                #use while loop to iterate through the movement
                                while temp_row < destination_row:

                                    #move one square diagonally
                                    temp_row +=1
                                    temp_col +=1

                                    #check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    #check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    #this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        #add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    #create else statement to raise an error if the number of enemy pieces on the
                                    #move is greater than one
                                    if len(enemy_pieces) > 1:

                                        raise InvalidMove

                                #after the while loop has terminated (without raising the InvalidMove exception),
                                #we can now complete the capture and move

                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                #get the enemy piece location in row, col form
                                enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                #complete a capture by calling the capture() method on the enemy piece
                                self.capture(board_dict[enemy_row][enemy_col])

                                #complete the move by calling the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                #lastly, check for promotions
                                #this if statement handles black king promotions
                                if "Black" in start_square.get_piece_color():

                                    if destination_row == 7:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                                #this else statement handles white king promotions
                                else:

                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            #if statement handles capture moves down and to the left:
                            elif row_diff == -col_diff and row_diff > 0 and col_diff < 0:

                                # use while loop to iterate through the movement
                                while temp_row < destination_row:

                                    # move one square diagonally
                                    temp_row += 1
                                    temp_col -= 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than one
                                    if len(enemy_pieces) > 1:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move
                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                # get the enemy piece location in row, col form
                                enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                # complete a capture by calling the capture() method on the enemy piece
                                self.capture(board_dict[enemy_row][enemy_col])

                                # complete the move by calling the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                # lastly, check for promotions
                                # this if statement handles black king promotions
                                if "Black" in start_square.get_piece_color():

                                    if destination_row == 7:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                                #this else statement handles white king promotions
                                else:

                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            # if statement handles capture moves up and to the right:
                            elif row_diff == -col_diff and row_diff < 0 and col_diff > 0:

                                # use while loop to iterate through the movement
                                while temp_row > destination_row:

                                    # move one square diagonally
                                    temp_row -= 1
                                    temp_col += 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than one
                                    if len(enemy_pieces) > 1:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move

                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                # get the enemy piece location in row, col form
                                enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                # complete a capture by calling the capture() method on the enemy piece
                                self.capture(board_dict[enemy_row][enemy_col])

                                # complete the move by calling the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                # lastly, check for promotions
                                # this if statement handles black king promotions
                                if "Black" in start_square.get_piece_color():

                                    if destination_row == 7:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                                # this else statement handles white king promotions
                                else:

                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            # if statement handles capture moves up and to the left:
                            elif row_diff == col_diff and row_diff < 0 and col_diff < 0:

                                # use while loop to iterate through the movement
                                while temp_row > destination_row:

                                    # move one square diagonally
                                    temp_row -= 1
                                    temp_col -= 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than one
                                    if len(enemy_pieces) > 1:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move

                                #create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                # get the enemy piece location in row, col form
                                enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                # complete a capture by calling the capture() method on the enemy piece
                                self.capture(board_dict[enemy_row][enemy_col])

                                # complete the move by calling the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                # lastly, check for promotions
                                # this if statement handles black king promotions
                                if "Black" in start_square.get_piece_color():

                                    if destination_row == 7:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                                # this else statement handles white king promotions
                                else:

                                    if destination_row == 0:

                                        # call the promote() method to perform the promotion
                                        self.promote(start_square, start_square.get_piece_color())

                            #else statement handles a case where the move is not diagonal
                            else:

                                raise InvalidMove

                        #both colored triple king checkers have same movement rules
                        elif start_square.get_piece_color() == "Black_Triple_King" or start_square.get_piece_color() == "White_Triple_King":

                            #non capture move of one diagonal square
                            if (destination_row == start_row + 1 or destination_row == start_row - 1) and (destination_col == start_col + 1 or destination_col == start_col - 1):

                                #call the move() method on the checkers_board object
                                self._checkers_board.move(start_square, destination_square_location)

                                #change the turn to the other player
                                for key in self._player_dict:
                                    if key != player_name:
                                        self._turn = self._player_dict[key].get_checker_color()

                            #a capture or non-capture move down and to the right depending on jumped square/piece
                            elif destination_row == start_row + 2 and destination_col == start_col + 2:

                                #check if the jumped square has a value of None in it
                                if board_dict[start_row+1][start_col+1] == None:

                                    raise InvalidMove

                                #check if jumped square has a friendly piece in it
                                elif player.get_checker_color() in board_dict[start_row + 1][start_col + 1].get_piece_color():

                                    #complete the move
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #change the turn to the other player
                                    for key in self._player_dict:
                                        if key != player_name:
                                            self._turn = self._player_dict[key].get_checker_color()

                                #else statement handles cases where the jumped square has an enemy piece in it
                                else:
                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row + 1][start_col + 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            #a capture or non-capture move down and to the left depending on jumped square/piece
                            elif destination_row == start_row + 2 and destination_col == start_col - 2:

                                #check if the jumped square has a value of None in it
                                if board_dict[start_row + 1][start_col - 1] == None:

                                    raise InvalidMove

                                #check if jumped square has a friendly piece in it
                                elif player.get_checker_color() in board_dict[start_row + 1][start_col - 1].get_piece_color():

                                    #complete the move
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #change the turn to the other player
                                    for key in self._player_dict:
                                        if key != player_name:
                                            self._turn = self._player_dict[key].get_checker_color()

                                #else statement handles cases where the jumped square has an enemy piece in it
                                else:
                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row + 1][start_col - 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            #a capture or non-capture move up and to the right depending on jumped square/piece
                            elif destination_row == start_row - 2 and destination_col == start_col + 2:

                                #check if the jumped square has a value of None in it
                                if board_dict[start_row - 1][start_col + 1] == None:

                                    raise InvalidMove

                                #check if jumped square has a friendly piece in it
                                elif player.get_checker_color() in board_dict[start_row - 1][start_col + 1].get_piece_color():

                                    #complete the move
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #change the turn to the other player
                                    for key in self._player_dict:
                                        if key != player_name:
                                            self._turn = self._player_dict[key].get_checker_color()

                                #else statement handles cases where the jumped square has an enemy piece in it
                                else:
                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row - 1][start_col + 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            #a capture or non-capture move up and to the left depending on jumped square/piece
                            elif destination_row == start_row - 2 and destination_col == start_col - 2:

                                #check if the jumped square has a value of None in it
                                if board_dict[start_row - 1][start_col - 1] == None:

                                    raise InvalidMove

                                #check if jumped square has a friendly piece in it
                                elif player.get_checker_color() in board_dict[start_row - 1][start_col - 1].get_piece_color():

                                    #complete the move
                                    self._checkers_board.move(start_square, destination_square_location)

                                    #change the turn to the other player
                                    for key in self._player_dict:
                                        if key != player_name:
                                            self._turn = self._player_dict[key].get_checker_color()

                                #else statement handles cases where the jumped square has an enemy piece in it
                                else:
                                    #complete a capture by calling the capture() method on the captured piece
                                    self.capture(board_dict[start_row - 1][start_col - 1])

                                    #complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            #code for capture moves over more than one square:
                            #elif statement handles capture moves down and to the right:
                            elif row_diff == col_diff and row_diff > 0 and col_diff > 0:

                                # use while loop to iterate through the movement
                                while temp_row < destination_row:

                                    # move one square diagonally
                                    temp_row += 1
                                    temp_col += 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than two
                                    if len(enemy_pieces) > 2:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move

                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                #elif statement completes the necessary actions for a move that captures one piece
                                elif len(enemy_pieces) == 1:

                                    #unpack the enemy square location in row, col format
                                    enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                    # complete a capture by calling the capture() method on the enemy piece
                                    self.capture(board_dict[enemy_row][enemy_col])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                #elif statement completes the necessary actions for a move that captures two pieces
                                elif len(enemy_pieces) == 2:

                                    # unpack the both enemy square locations in row, col format
                                    enemy_row_1, enemy_col_1 = enemy_pieces[0].get_square_location()
                                    enemy_row_2, enemy_col_2 = enemy_pieces[1].get_square_location()

                                    # complete two captures by calling the capture() method on the enemy pieces
                                    self.capture(board_dict[enemy_row_1][enemy_col_1])
                                    self.capture(board_dict[enemy_row_2][enemy_col_2])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            # elif statement handles capture moves down and to the left:
                            elif row_diff == -col_diff and row_diff > 0 and col_diff < 0:

                                # use while loop to iterate through the movement
                                while temp_row < destination_row:

                                    # move one square diagonally
                                    temp_row += 1
                                    temp_col -= 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than two
                                    if len(enemy_pieces) > 2:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move

                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                # elif statement completes the necessary actions for a move that captures one piece
                                elif len(enemy_pieces) == 1:

                                    # unpack the enemy square location in row, col format
                                    enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                    # complete a capture by calling the capture() method on the enemy piece
                                    self.capture(board_dict[enemy_row][enemy_col])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                # elif statement completes the necessary actions for a move that captures two pieces
                                elif len(enemy_pieces) == 2:

                                    # unpack the both enemy square locations in row, col format
                                    enemy_row_1, enemy_col_1 = enemy_pieces[0].get_square_location()
                                    enemy_row_2, enemy_col_2 = enemy_pieces[1].get_square_location()

                                    # complete two captures by calling the capture() method on the enemy pieces
                                    self.capture(board_dict[enemy_row_1][enemy_col_1])
                                    self.capture(board_dict[enemy_row_2][enemy_col_2])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            # elif statement handles capture moves up and to the right:
                            elif row_diff == -col_diff and row_diff < 0 and col_diff > 0:

                                # use while loop to iterate through the movement
                                while temp_row > destination_row:

                                    # move one square diagonally
                                    temp_row -= 1
                                    temp_col += 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than two
                                    if len(enemy_pieces) > 2:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move

                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                # elif statement completes the necessary actions for a move that captures one piece
                                elif len(enemy_pieces) == 1:

                                    # unpack the enemy square location in row, col format
                                    enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                    # complete a capture by calling the capture() method on the enemy piece
                                    self.capture(board_dict[enemy_row][enemy_col])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                # elif statement completes the necessary actions for a move that captures two pieces
                                elif len(enemy_pieces) == 2:

                                    # unpack the both enemy square locations in row, col format
                                    enemy_row_1, enemy_col_1 = enemy_pieces[0].get_square_location()
                                    enemy_row_2, enemy_col_2 = enemy_pieces[1].get_square_location()

                                    # complete two captures by calling the capture() method on the enemy pieces
                                    self.capture(board_dict[enemy_row_1][enemy_col_1])
                                    self.capture(board_dict[enemy_row_2][enemy_col_2])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            # elif statement handles capture moves up and to the left:
                            elif row_diff == -col_diff and row_diff < 0 and col_diff < 0:

                                # use while loop to iterate through the movement
                                while temp_row > destination_row:

                                    # move one square diagonally
                                    temp_row -= 1
                                    temp_col -= 1

                                    # check if the new square is empty
                                    if board_dict[temp_row][temp_col] == None:
                                        pass

                                    # check if the new square has a friendly piece in it
                                    elif player.get_checker_color() in board_dict[temp_row][temp_col].get_piece_color():

                                        raise InvalidMove

                                    # this elif statement handles cases where the new square has an enemy piece in it
                                    else:

                                        # add the enemy piece to the enemy_pieces list
                                        enemy_pieces.append(board_dict[temp_row][temp_col])

                                    # create else statement to raise an error if the number of enemy pieces on the
                                    # move is greater than two
                                    if len(enemy_pieces) > 2:
                                        raise InvalidMove

                                # after the while loop has terminated (without raising the InvalidMove exception),
                                # we can now complete the capture and move

                                # create if statement to check if the move had no enemy pieces across it
                                if len(enemy_pieces) == 0:
                                    raise InvalidMove

                                # elif statement completes the necessary actions for a move that captures one piece
                                elif len(enemy_pieces) == 1:

                                    # unpack the enemy square location in row, col format
                                    enemy_row, enemy_col = enemy_pieces[0].get_square_location()

                                    # complete a capture by calling the capture() method on the enemy piece
                                    self.capture(board_dict[enemy_row][enemy_col])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                                # elif statement completes the necessary actions for a move that captures two pieces
                                elif len(enemy_pieces) == 2:

                                    # unpack the both enemy square locations in row, col format
                                    enemy_row_1, enemy_col_1 = enemy_pieces[0].get_square_location()
                                    enemy_row_2, enemy_col_2 = enemy_pieces[1].get_square_location()

                                    # complete two captures by calling the capture() method on the enemy pieces
                                    self.capture(board_dict[enemy_row_1][enemy_col_1])
                                    self.capture(board_dict[enemy_row_2][enemy_col_2])

                                    # complete the move by calling the move() method on the checkers_board object
                                    self._checkers_board.move(start_square, destination_square_location)

                            #else statement handles cases where the move is not diagonal
                            else:
                                raise InvalidMove

                    else: #for destination square non-None valued

                        raise InvalidSquare

            #else statement handles invalid parameter square
            else:

                raise InvalidSquare

            #store the final number of captured pieces that a player has
            final_cap = player.get_captured_pieces_count()

            return final_cap - initial_cap

    def get_checker_details(self, square_location):
        """This method takes as parameter a square location and returns the checker details present in that square.
        checker details can be either None (no checker in that square), 'White', 'Black', 'Black_king', 'White_king',
        'Black_Triple_King', or 'White_Triple_King'. This method works by passing the square_location argument into
        a call to the checkers_board object's method get_square_details(), then returning the returned piece's
        get_color() method's result. The exception handling is done in the get_square_details() method where an invalid
        square location raises the InvalidSquare exception."""
        return self._checkers_board.get_square_details(square_location)

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
        pieces from moving. Only the former condition is checked in this method."""

        #initialize a random value to be used to count the number of iterations
        val = 0

        #first test for a game winner conventionally, using the amount of captured pieces:
        #use for loop to accomplish the above
        for key in self._player_dict:

            #if statement handles if the currently indexed player has captured all 12 opponent pieces
            if self._player_dict[key].get_captured_pieces_count() == 12:

                return key

            #add one to the random val for every time the currently indexed player has not captured all 12 opponent
            #pieces
            else:
                val += 1

        #if statement to handle if val == 2 (if both players have not captured all 12 pieces)
        if val == 2:

            return "Game has not ended"
