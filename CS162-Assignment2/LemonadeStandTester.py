"""
Author : Gabriel Rodgers
GitHub Username : trashcoder8
Date : 1/20/23
Description : This program is designed to test the LemonadeStand.py program's functionality using unit tests
"""

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError

class TestingLemonadeStand(unittest.TestCase):
    """This class must perform at least 5 unit tests on the LemonadeStand program
    and contain at least 2 different assert functions"""

    #create unit test methods (each method is a unit test)
    def test_1(self):
        """Tests the MenuItem class"""
        #create MenuItem classes for testing
        item1 = MenuItem("raspberries", 3, 6)
        item2 = MenuItem("blueberries", 2, 5)

        #test MenuItem get_name, get_wholesale_cost, and get_selling_price methods
        self.assertIs(item1.get_name(), "raspberries")
        self.assertEqual(item1.get_wholesale_cost(), 3)
        self.assertEqual(item2.get_selling_price(), 5)

    def test_2(self):
        """Tests the LemonadeStand get methods"""

        #create lemonadestand class
        lem = LemonadeStand("lalalala")
        self.assertIs(lem.get_name(), "lalalala")
        self.assertIsNot(lem.get_name(), "lalalaLa")

    def test_3(self):
        """Tests the LemonadeStand """

        #create lemonadestand class
        lem = LemonadeStand("lalalala")

        #create items to add to lem
        item1 = MenuItem("raspberries", 3, 6)
        item2 = MenuItem("blueberries", 2, 5)

        #add items to lem menu_dict
        lem.add_menu_item(item1)
        lem.add_menu_item(item2)

        #test menu_dict keys and values
        self.assertIn("raspberries", lem._menu_dict)
        self.assertNotIn("butternut squash", lem._menu_dict)
        self.assertEqual(6, lem._menu_dict.get("raspberries").get_selling_price())

    def test_4(self):
        """Tests the """

    def test_5(self):
        """"Tests the """

    def test_6(self):
        """Tests the """


