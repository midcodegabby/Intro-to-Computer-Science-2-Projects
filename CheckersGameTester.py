#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/17/23
#Description : This program is designed to test the CheckersGame.py program's functionality using unit tests.

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
        their own square_location data members and other data members of the piece class"""

        # create the game
        game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

        # retrieve the board_dict
        board_dict = game.get_board_object().get_board()

        #test if a piece's square_location is the same as its location on the board
        self.assertEqual(board_dict[0][3].get_square_location(), (0,3))

        #test if a piece's piece_color is the same as its passed in value at initialization
        self.assertEqual(board_dict[0][3].get_piece_color(), "White")

    def test_3(self):
        """Tests the validity of raising exceptions for a variety of different situations, including inputting
        invalid square locations, invalid players, invalid moves, and trying to play out of turn"""

        # create the game
        game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

        #test the OutOfTurn exception, where the first move of the checkers game is done by white instead of black.
        #test other exceptions in other try/except blocks
        try:
            #test invalid turn
            game.play_game("Gabe", (2,1), (3,0))

        except OutOfTurn:
            print("If you can see this message then this test successfully raised the OutOfTurn Exception")

        try:
            #test invalid square
            game.play_game("Serena", (7, 0), (6, 1))

        except InvalidSquare:
            print("If you can see this message then this test successfully raised the InvalidSquare Exception")

        try:
            #test invalid player
            game.play_game("Bob", (0, 3), (4, 0))

        except InvalidPlayer:
            print("If you can see this message then this test successfully raised the InvalidPlayer Exception")

        try:
            #test invalid move
            game.play_game("Serena", (5, 0), (3, 2))

        except InvalidMove:
            print("If you can see this message then this test successfully raised the InvalidMove Exception")

    def test_4(self):
        """Tests the functionality of the get_checker_details() method and the game_winner() method"""

        # create the game
        game = Checkers()

        # create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

        # retrieve the board_dict
        board_dict = game.get_board_object().get_board()

        #test the equivalence between expected and actual get_checker_details for an empty square and a non-empty square
        self.assertIs(game.get_checker_details((2, 2)), None)
        self.assertIs(game.get_checker_details((2,1)), "White")

        #play an entire game, and check if the game winner is player2
        game.play_game("Serena", (5, 0), (4, 1))
        game.play_game("Gabe", (2, 1), (3, 0))
        game.play_game("Serena", (5, 2), (4, 3))
        game.play_game("Gabe", (3, 0), (5, 2))
        game.play_game("Gabe", (1, 0), (2, 1))
        game.play_game("Serena", (6, 3), (4, 1))
        game.play_game("Serena", (6, 1), (5, 0))
        game.play_game("Gabe", (2, 7), (3, 6))
        game.play_game("Serena", (4, 3), (3, 2))
        game.play_game("Gabe", (2, 1), (3, 0))
        game.play_game("Serena", (3, 2), (2, 1))
        game.play_game("Gabe", (2, 5), (3, 4))
        game.play_game("Serena", (2, 1), (1, 0))
        game.play_game("Gabe", (1, 2), (2, 1))
        game.play_game("Serena", (4, 1), (3, 2))
        game.play_game("Gabe", (0, 1), (1, 2))
        game.play_game("Serena", (1, 0), (0, 1))
        game.play_game("Gabe", (2, 3), (4, 1))
        game.play_game("Gabe", (2, 1), (3, 2))
        game.play_game("Serena", (0, 1), (2, 3))
        game.play_game("Serena", (2, 3), (4, 5))
        game.play_game("Serena", (4, 5), (2, 7))
        game.play_game("Serena", (5, 4), (4, 5))
        game.play_game("Gabe", (4, 1), (5, 2))
        game.play_game("Serena", (2, 7), (3, 6))
        game.play_game("Gabe", (5, 2), (6, 3))
        game.play_game("Serena", (7, 2), (6, 1))
        game.play_game("Gabe", (6, 3), (7, 2))
        game.play_game("Serena", (4, 5), (3, 4))
        game.play_game("Gabe", (7, 2), (6, 3))
        game.play_game("Serena", (3, 6), (4, 5))
        game.play_game("Gabe", (6, 3), (5, 4))
        game.play_game("Serena", (5, 6), (4, 7))
        game.play_game("Gabe", (5, 4), (4, 3))
        game.play_game("Serena", (4, 5), (5, 6))
        game.play_game("Gabe", (1, 4), (2, 5))
        game.play_game("Serena", (6, 5), (5, 4))
        game.play_game("Gabe", (3, 2), (4, 1))
        game.play_game("Serena", (5, 6), (6, 5))
        game.play_game("Gabe", (4, 3), (3, 2))
        game.play_game("Serena", (7, 4), (6, 3))
        game.play_game("Gabe", (4, 1), (5, 2))
        game.play_game("Serena", (6, 5), (7, 4))
        game.play_game("Gabe", (2, 5), (4, 3))
        game.play_game("Gabe", (4, 3), (6, 5))
        game.play_game("Gabe", (3, 2), (2, 1))
        game.play_game("Serena", (5, 0), (4, 1))
        game.play_game("Gabe", (2, 1), (1, 0))
        game.play_game("Serena", (6, 1), (5, 0))
        game.play_game("Gabe", (5, 2), (6, 1))
        game.play_game("Serena", (7, 4), (5, 2))
        game.play_game("Gabe", (6, 1), (7, 2))
        game.play_game("Serena", (6, 3), (5, 4))
        game.play_game("Gabe", (1, 0), (0, 1))
        game.play_game("Serena", (4, 7), (3, 6))
        game.play_game("Gabe", (0, 1), (1, 2))
        game.play_game("Serena", (5, 4), (4, 5))
        game.play_game("Gabe", (1, 2), (5, 6))
        game.play_game("Gabe", (1, 6), (2, 5))
        game.play_game("Serena", (5, 2), (4, 3))
        game.play_game("Gabe", (0, 7), (1, 6))
        game.play_game("Serena", (7, 6), (5, 4))
        game.play_game("Serena", (4, 1), (3, 2))
        game.play_game("Gabe", (2, 5), (3, 4))
        game.play_game("Serena", (4, 3), (0, 7))
        game.play_game("Serena", (6, 7), (4, 5))
        game.play_game("Serena", (3, 2), (2, 3))
        game.play_game("Gabe", (0, 5), (1, 6))
        game.play_game("Serena", (0, 7), (6, 1))
        game.play_game("Serena", (3, 6), (2, 7))
        game.play_game("Gabe", (3, 0), (4, 1))
        game.play_game("Serena", (5, 0), (3, 2))
        game.play_game("Serena", (6, 1), (5, 2))
        game.play_game("Gabe", (0, 3), (1, 2))
        game.play_game("Serena", (2, 3), (0, 1))
        game.play_game("Serena", (0, 1), (1, 0))
        game.play_game("Gabe", (7, 2), (6, 3))
        game.play_game("Serena", (5, 2), (7, 4))

        #test game_winner() method
        self.assertIs("Serena", game.game_winner())


    def test_5(self):
        """Tests the get_king_count(), get_triple_king_count(), and get_captured_pieces_count() methods of the
        Player class"""

        #create the game
        game = Checkers()

        #create players
        player1 = game.create_player("Gabe", "White")
        player2 = game.create_player("Serena", "Black")

        #play the entire game until completion, then check the number of kings, triple kings, and captured pieces for
        #both players at different times during the game
        game.play_game("Serena", (5, 0), (4, 1))
        game.play_game("Gabe", (2, 1), (3, 0))
        game.play_game("Serena", (5, 2), (4, 3))
        game.play_game("Gabe", (3, 0), (5, 2))
        game.play_game("Gabe", (1, 0), (2, 1))
        game.play_game("Serena", (6, 3), (4, 1))
        game.play_game("Serena", (6, 1), (5, 0))
        game.play_game("Gabe", (2, 7), (3, 6))
        game.play_game("Serena", (4, 3), (3, 2))
        game.play_game("Gabe", (2, 1), (3, 0))
        game.play_game("Serena", (3, 2), (2, 1))
        game.play_game("Gabe", (2, 5), (3, 4))
        game.play_game("Serena", (2, 1), (1, 0))
        game.play_game("Gabe", (1, 2), (2, 1))
        game.play_game("Serena", (4, 1), (3, 2))
        game.play_game("Gabe", (0, 1), (1, 2))
        game.play_game("Serena", (1, 0), (0, 1))
        game.play_game("Gabe", (2, 3), (4, 1))
        game.play_game("Gabe", (2, 1), (3, 2))
        game.play_game("Serena", (0, 1), (2, 3))
        game.play_game("Serena", (2, 3), (4, 5))
        game.play_game("Serena", (4, 5), (2, 7))
        game.play_game("Serena", (5, 4), (4, 5))
        game.play_game("Gabe", (4, 1), (5, 2))
        game.play_game("Serena", (2, 7), (3, 6))
        game.play_game("Gabe", (5, 2), (6, 3))
        game.play_game("Serena", (7, 2), (6, 1))
        game.play_game("Gabe", (6, 3), (7, 2))
        game.play_game("Serena", (4, 5), (3, 4))
        game.play_game("Gabe", (7, 2), (6, 3))
        game.play_game("Serena", (3, 6), (4, 5))
        game.play_game("Gabe", (6, 3), (5, 4))
        game.play_game("Serena", (5, 6), (4, 7))
        game.play_game("Gabe", (5, 4), (4, 3))
        game.play_game("Serena", (4, 5), (5, 6))
        game.play_game("Gabe", (1, 4), (2, 5))
        game.play_game("Serena", (6, 5), (5, 4))

        #test captured pieces method for both players
        self.assertEqual(player1.get_captured_pieces_count(), 2)
        self.assertEqual(player2.get_captured_pieces_count(), 4)

        #test king count method for both players
        self.assertEqual(player1.get_king_count(), 1)
        self.assertEqual(player2.get_king_count(), 1)

        #continue the game
        game.play_game("Gabe", (3, 2), (4, 1))
        game.play_game("Serena", (5, 6), (6, 5))
        game.play_game("Gabe", (4, 3), (3, 2))
        game.play_game("Serena", (7, 4), (6, 3))
        game.play_game("Gabe", (4, 1), (5, 2))
        game.play_game("Serena", (6, 5), (7, 4))
        game.play_game("Gabe", (2, 5), (4, 3))
        game.play_game("Gabe", (4, 3), (6, 5))
        game.play_game("Gabe", (3, 2), (2, 1))
        game.play_game("Serena", (5, 0), (4, 1))
        game.play_game("Gabe", (2, 1), (1, 0))
        game.play_game("Serena", (6, 1), (5, 0))
        game.play_game("Gabe", (5, 2), (6, 1))
        game.play_game("Serena", (7, 4), (5, 2))
        game.play_game("Gabe", (6, 1), (7, 2))
        game.play_game("Serena", (6, 3), (5, 4))
        game.play_game("Gabe", (1, 0), (0, 1))
        game.play_game("Serena", (4, 7), (3, 6))
        game.play_game("Gabe", (0, 1), (1, 2))
        game.play_game("Serena", (5, 4), (4, 5))
        game.play_game("Gabe", (1, 2), (5, 6))
        game.play_game("Gabe", (1, 6), (2, 5))
        game.play_game("Serena", (5, 2), (4, 3))
        game.play_game("Gabe", (0, 7), (1, 6))

        #test triple_king_count() method for both players
        self.assertEqual(player1.get_triple_king_count(), 1)
        self.assertEqual(player2.get_triple_king_count(), 1)

        game.play_game("Serena", (7, 6), (5, 4))
        game.play_game("Serena", (4, 1), (3, 2))
        game.play_game("Gabe", (2, 5), (3, 4))
        game.play_game("Serena", (4, 3), (0, 7))
        game.play_game("Serena", (6, 7), (4, 5))
        game.play_game("Serena", (3, 2), (2, 3))
        game.play_game("Gabe", (0, 5), (1, 6))
        game.play_game("Serena", (0, 7), (6, 1))
        game.play_game("Serena", (3, 6), (2, 7))
        game.play_game("Gabe", (3, 0), (4, 1))
        game.play_game("Serena", (5, 0), (3, 2))
        game.play_game("Serena", (6, 1), (5, 2))
        game.play_game("Gabe", (0, 3), (1, 2))
        game.play_game("Serena", (2, 3), (0, 1))
        game.play_game("Serena", (0, 1), (1, 0))
        game.play_game("Gabe", (7, 2), (6, 3))
        game.play_game("Serena", (5, 2), (7, 4))

        #test triple_king_count() method for both players after game completion
        self.assertEqual(player1.get_triple_king_count(), 0)
        self.assertEqual(player2.get_triple_king_count(), 1)





