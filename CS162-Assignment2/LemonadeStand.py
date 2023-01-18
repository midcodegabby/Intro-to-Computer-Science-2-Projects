"""
Author : Gabriel Rodgers
GitHub Username : trashcoder8
Date : 1/18/23
Description :
"""

#create MenuItem class
class MenuItem:
    """represents a menu class, with 3 private parameters/data members: name (string),
    wholesale_cost (float), and selling_price (float)"""

    #initialize data member objects in the class
    def __init__(self, name, wholesale_cost, selling_price):
        """creates a new MenuItem class with a name, cost, and price inputted by the user,
        while keeping all the data members private."""
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    #create get methods for each data member
    def get_name(self):
        """retrieves the name parameter inputted by the user while keeping it distinct from the class
        and its other objects by keeping the parameter private"""
        return self._name

    def get_wholesale_cost(self):
        """retrieves the wholesale_cost parameter inputted by the user while keeping it distinct from the class
        and its other objects by keeping the parameter private"""
        return self._wholesale_cost

    def get_selling_price(self):
        """retrieves the selling_price parameter inputted by the user while keeping it distinct from the class
        and its other objects by keeping the parameter private"""
        return self._selling_price

#create SalesForDay class
class SalesForDay:
    """represents a sale day class with 2 private data members: days the stand has been open for (integer)
    and a (dictionary) containing the (keys) names of sold items and the (values) number of each respective item sold"""

    # initialize data member objects in the class
    def __init__(self, number_of_days, sales_dictionary):
        """creates a new sales for day class with 2 private data members"""
        self._number_of_days = number_of_days
        self._sales_dictionary = sales_dictionary

    #create get methods for both data members
    def get_number_of_days(self):
        """retrieves the private data member number_of_days"""
        return self._number_of_days

    def get_sales_dictionary(self):
        """retrieves the private data member sales_dictionary"""
        return self._sales_dictionary

#create LemonadeStand class
class LemonadeStand:
    """represents a lemonade stand class with 4 private data members: name of stand (string), current day (integer),
    a (dictionary) of MenuItem objects (retrieved using get_ methods) where the keys are names of items and the values are
    corresponding MenuItem objects, and a (list) of SalesForDay objects"""

    #initialize data member objects for the class