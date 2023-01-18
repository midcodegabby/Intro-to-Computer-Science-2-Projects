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
    def __init__(self, days, sales_dict):
        """creates a new sales for day class with 2 private data members"""
        self._days = days
        self._sales_dict = sales_dict

    #create get methods for both data members
    def get_days(self):
        """retrieves the private data member days"""
        return self._days

    def get_sales_dict(self):
        """retrieves the private data member sales_dict"""
        return self._sales_dict

#create LemonadeStand class
class LemonadeStand:
    """represents a lemonade stand class with 4 private data members: name of stand (string), current day (integer),
    a (dictionary) of MenuItem objects (retrieved using get_ methods) where the keys are names of items and the values are
    corresponding MenuItem objects, and a (list) of SalesForDay objects"""

    #initialize data member objects for the class
    def __init__(self,name):
        """initializes 4 variables: the name of the (class) LemonadeStand to the passed in parameter,
        the current day (integer) to zero, the (dictionary) of MenuItems to be empty, and the (list)
        SalesForDay to an empty list"""
        self._name = name

        #initialize current day to zero
        day = 0

        #initialize the menu to an empty dictionary:
        menu_dict = {}

        #initalize the sales_record list
        sales_record = []

    #define a function to retrieve the private data member name of lemonade stand
    def get_name(self):
        """retrieves the private data member name (of the LemonadeStand)"""
        return self._name

    def add_menu_item(self, menu_item):
        """This function should take a MenuItem object and add it to the menu_dict, with the key being
        the MenuItem's name, and the corresponding value being the MenuItem object itself."""
        menu_dict[menu_item._name] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """This function should take a user-inputted dictionary of (keys) names of items sold and
        (corresponding values) how many of the item were sold, and """

    def sales_of_menu_item_today(self, day, menu_item):
        """This function should retrieve """

    def total_sales_for_menu_item(self, menu_item):
        """This function should take the name of a menu item and return the total number of that item
        sold over the history of the stand. This method should use sales_of_menu_item_today to find the
        required value"""

        return #value

    def total_profit_for_menu_item(self, menu_item):
        """This method should take the name of a menu_item and return the total profit on that item
        over the history of the stand. Should use total_sales_for_menu_item method"""

    def total_profit_for_stand(self):





