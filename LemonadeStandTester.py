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
        """Tests the MenuItem class get methods"""
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
        """Tests the LemonadeStand menu_dict"""

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
        """Tests the total_profit_for_menu_item method in the LemonadeStand class"""

        # create lemonadestand class
        lem = LemonadeStand("lalalala")

        # create items to add to lem
        item1 = MenuItem("raspberries", 3, 6)
        item2 = MenuItem("blueberries", 2, 5)

        # add items to lem menu_dict
        lem.add_menu_item(item1)
        lem.add_menu_item(item2)

        #create sales_dict
        day_x_sales = {
            "raspberries" : 28,
            "blueberries" : 87,
        }

        #add the sales dictionary to lem
        lem.enter_sales_for_today(day_x_sales)

        #test total_profit_for_menu_item method
        self.assertEqual(84, lem.total_profit_for_menu_item("raspberries"))
        self.assertAlmostEqual(261.00001, lem.total_profit_for_menu_item("blueberries"), 3)

    def test_5(self):
        """"Testing the enter_sales_for_today method in the LemonadeStand class to raise the
        InvalidSaleItemError"""

        # create lemonadestand class
        lem = LemonadeStand("lalalala")

        # create items to add to lem
        item1 = MenuItem("raspberries", 3, 6)
        item2 = MenuItem("blueberries", 2, 5)

        # add items to lem menu_dict
        lem.add_menu_item(item1)
        lem.add_menu_item(item2)

        # create sales_dict
        day_x_sales = {
            "raspberries": 28,
            "blueberries": 87,
            "rats" : -9
        }

        # add the sales dictionary to lem
        try:
            lem.enter_sales_for_today(day_x_sales)

        except InvalidSalesItemError:
            print("If you can see this message then this test successfully raised the InvalidSalesItemError")

    def test_6(self):
        """Testing the sales_dict inside the sales_record list in the enter_sales_for_today method"""

        # create lemonadestand class
        lem = LemonadeStand("lalalala")

        # create items to add to lem
        item1 = MenuItem("raspberries", 3, 6)
        item2 = MenuItem("blueberries", 2, 5)
        item3 = MenuItem("blue lemonade", 4, 25)

        # add items to lem menu_dict
        lem.add_menu_item(item1)
        lem.add_menu_item(item2)
        lem.add_menu_item(item3)

        # create sales_dicts
        day_0_sales = {
            "raspberries": 28,
            "blueberries": 87,
        }

        day_1_sales = {
            "raspberries" : 76,
            "blueberries" : 32,
            "blue lemonade" : 12
        }

        #add sales_dicts to lem
        lem.enter_sales_for_today(day_0_sales)
        lem.enter_sales_for_today(day_1_sales)

        #test the sales_record
        self.assertIs(lem._sales_record[0].get_day(), 0)
        self.assertIs(lem._sales_record[0].get_sales_dict().get("raspberries"), 28)




