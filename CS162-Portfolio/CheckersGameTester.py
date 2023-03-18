#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/19/23
#Description : This program is designed to test the CheckersGame.py program's functionality using unit tests

import unittest
from CheckersGame import Piece, Player, Board, Checkers, InvalidMove, InvalidPlayer, InvalidSquare, OutOfTurn, generate_pieces


class TestingCheckersGame(unittest.TestCase):
    """This class must perform at least 5 different unit tests on the CheckersGame program and contain at least 2
    different assert functions."""

    def test_1(self):
        """Tests that piece objects initialized onto the board_dict in the board object are the same objects as
        the piece objects inside the player objects' list of pieces, along with other player object methods"""

        #create the game
        game = Checkers()

        #create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

        #retrieve player1 and player2's lists of piece objects
        piece_list1 = player1.get_piece_list()
        piece_list2 = player2.get_piece_list()

        #retrieve the board_dict
        board_dict = game.get_board_object().get_board()

        #test the equivalences between player1 and player2 data members and their passed in values
        self.assertEqual(player1.get_player_name(), "Gabe")
        self.assertEqual(player2.get_player_name(), "Serena")
        self.assertEqual(player1.get_checker_color(), "White")
        self.assertEqual(player2.get_checker_color(), "Black")

        #test if a white piece on the board_dict is in player1's list of pieces
        self.assertIn(board_dict[0][1], piece_list1)

        #vice versa test for player2
        self.assertIn(board_dict[7][0], piece_list2)

    def test_2(self):
        """Tests pieces to see if their locations on the board_dict inside the board object match up to
        their own square_location data members"""

        # create the game
        game = game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

    def test_3(self):
        """Tests the validity of raising exceptions for a variety of different situations, including inputting
        invalid square locations, invalid players, invalid moves, and trying to play out of turn"""

        # create the game
        game = game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

    def test_4(self):
        """Tests the functionality of the get_checker_details() method, the print_board() method, and the game_winner()
        method"""

        # create the game
        game = game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

    def test_5(self):
        """Tests the get_king_count(), get_triple_king_count(), and get_captured_pieces_count() methods of the
        Player class"""

        # create the game
        game = game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")





