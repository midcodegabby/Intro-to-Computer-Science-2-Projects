"""
Author : Gabriel Rodgers
GitHub Username : trashcoder8
Date : 1/18/23
Description : This program's purpose is to perform calculations and handle errors in user input on user-inputted
information. The calculations/tasks this program is made to handle include holding and categorizing user-inputted
dictionaries of sales of particular items, storing item information (including item name, wholesale price, and
selling price), calculating profits on any day and calculating profits over an indeterminate time period of recorded
sales dictionaries, in the hopes of simulating a lemonade stand. This program is able to use user-inputted items
in a menu class and compare those to user-inputted items in a sales dictionary. If a sale item is inputted into a
sales dictionary that is not one of the previously inputted menu items, then this program is able to handle invalid
sale item input by raising errors and excepting them in a main function. This program uses user-inputs of
day, menu items, sale items, menu item wholesale and selling cost, and names in several different object forms
(including classes, dictionaries, and integers) to perform the previously stated calculations.
"""

class InvalidSalesItemError(Exception):
    """user defined exception for an inputted sales item that does not exist in the menu_dict"""
    pass

class MenuItem:
    """represents a menu class, with 3 private parameters/data members: name (string),
    wholesale_cost (float), and selling_price (float)"""

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

class SalesForDay:
    """represents a sale day class with 2 private data members: current day (integer)
    and a (dictionary) containing the (keys) names of sold items and the (values) number of each
    respective item sold"""

    def __init__(self, day, sales_dict):
        """creates a new sales for day class with 2 private data members"""
        self._day = day
        self._sales_dict = sales_dict

    #create get methods for both data members
    def get_day(self):
        """retrieves the private data member days"""
        return self._day

    def get_sales_dict(self):
        """retrieves the private data member sales_dict"""
        return self._sales_dict

class LemonadeStand:
    """represents a lemonade stand class with 4 private data members: name of stand (string), current day
    (integer), a (dictionary) of MenuItem objects (retrieved using get_ methods) where the keys are names
    of items and the values are corresponding MenuItem objects, and a (list) of SalesForDay objects"""

    def __init__(self, name):
        """initializes 4 variables: the name of the (class) LemonadeStand to the passed in parameter,
        the current day (integer) to zero, the (dictionary) of MenuItems to be empty, and the (list) of
        SalesForDay objects to an empty list"""
        self._name = name

        #initialize current day to zero
        self._day = 0

        #initialize the menu to an empty dictionary:
        self._menu_dict = {}

        #initalize the sales_record list:
        self._sales_record = []

    #define a function to retrieve the private data member name of lemonade stand
    def get_name(self):
        """retrieves the private data member name (of the LemonadeStand)"""
        return self._name

    def add_menu_item(self, menu_item_class):
        """This method should take a MenuItem object and add it to the menu_dict, with the key being
        the MenuItem's name, and the corresponding value being the MenuItem object itself."""
        self._menu_dict[menu_item_class.get_name()] = menu_item_class

    def enter_sales_for_today(self, sales_dict):
        """This method should take a user-inputted dictionary of (keys) names of sold_items and
        (corresponding values) how many of each of the sold_items were sold. This method should also raise an
        InvalidSalesItemError exception if a key in the sales_dict does not match any of the menu_item names.
        If the menu_item name is valid and in the inputted sales_dict, then the method should create a new
        SalesForDay object using the current day and the sales_dict, add that new SalesForDay object
        to the sales_record list, and then increment the current day by 1."""

        """create if statements to make sure that if an inputted sold_item (in sales_dict) does not exist, then
        the InvalidSalesItemError is raised. Lastly, to make sure that if an inputted sold_item corresponds to a 
        menu_item._name in menu_dict, then a new SalesForDay object is created."""

        #create for loop to loop through all keys in the sales_dict dictionary
        for key in sales_dict:

            # create elif statement to add the sales_dict to a new SalesForDay class
            if key in self._menu_dict:

                new_sales_for_day = SalesForDay(self._day, sales_dict)

            #create elif statement to deal with sales_dict keys that are not in the menu_dict keys
            elif key not in self._menu_dict:

                raise InvalidSalesItemError

        #outside of for loop, append the new_sales_for_day class into the sales_record list
        self._sales_record.append(new_sales_for_day)
        #add an increment of 1 day to the day after appending the above
        self._day += 1

    def sales_of_menu_item_for_day(self, day, menu_item):
        """This method should retrieve and return the number of the menu_item sold for a particular day (both
        parameters being inputted)."""

        """using the day parameter, get the sales_dict for that day from the corresponding SalesForDay object in
        the sales_record list; must initialize new dictionary to retrieve data using day parameter first though"""
        sales_on_that_day = self._sales_record[day].get_sales_dict()

        """create if statement to retrieve the value portion of the key (menu_item) if the menu_item exists 
        in the sales_on_that_day_dictionary"""
        if menu_item in sales_on_that_day:

            return sales_on_that_day.get(menu_item)

        #create else statement to handle situations where the item was not sold at all for that day
        else:
            return 0

    def total_sales_for_menu_item(self, menu_item):
        """This method should take the name of a menu item and return the total number of that item
        sold over the history of the stand. This method should use sales_of_menu_item_for_day to find the
        required value."""

        #initialize the returned value
        total_sales_of_item = 0

        """create for loop to iterate through the amount of days inputted and add the value of the number 
        of menu_items sold on that day (using the sales_of_menu_item_for_day method) to the initialized 
        total_sales_of_item variable"""
        for index in range(self._day):
            total_sales_of_item = total_sales_of_item + self.sales_of_menu_item_for_day(index, menu_item)

        return total_sales_of_item

    def total_profit_for_menu_item(self, menu_item):
        """This method should take the name of a menu_item and return the total profit on that item
        over the history of the stand. Should use total_sales_for_menu_item method"""

        """retrieve the selling_price and wholesale_cost from the MenuItem class value corresponding to the 
        menu_item key in the menu_dict, then subtract the wholesale_cost from the selling_price to calculate 
        the item_profit_margin"""
        item_profit_margin = self._menu_dict.get(menu_item).get_selling_price() - self._menu_dict.get(menu_item).get_wholesale_cost()

        """multiply the item_profit_margin by the total sales of the menu item (found by calling the 
        total_sales_for_menu_item method)"""
        total_item_profit = self.total_sales_for_menu_item(menu_item)*item_profit_margin

        return total_item_profit

    def total_profit_for_stand(self):
        """This method should take no parameters and return the total profit on all items sold over the
        entire history of the stand, and should use the total_profit_for_menu_item method"""

        #initalize total_profit variable
        total_profit = 0

        """create a for loop to loop through all keys in menu_dict, calculate the profits for each key, 
        then add them all together"""
        for key in self._menu_dict:
            total_profit = total_profit + self.total_profit_for_menu_item(key)

        return total_profit

def main():
    """This function will create a LemonadeStand object, create more than 1 MenuItem objects and add them to
    the LemonadeStand's menu, create a dictionary of sales for the day that includes sales of at least one item
    that is not in the menu, pass that dictionary into the enter_sales_for_today method, and handle any
    InvalidSalesItemError exceptions with a try/except block"""

    #create LemonStand object
    lemonhead = LemonadeStand("Lemonhead's Lemonade Stand")

    #create MenuItem objects
    item1 = MenuItem("cookies", 1, 4)
    item2 = MenuItem("lemonade", .75, 2)
    item3 = MenuItem("apples", .5, 2)

    #add MenuItem objects to lemonhead's menu dictionary
    lemonhead.add_menu_item(item1)
    lemonhead.add_menu_item(item2)
    lemonhead.add_menu_item(item3)

    #create a dictionary of sales for the day that includes an item that is not on lemonhead's menu dictionary
    day_0_sales = {
        "lemonade" : 24,
        "cookies" : 5,
        "apples" : 12,
        #"raisins" : 128,
        #"butternut squash" : 6
    }

    #use try/except block to handle exceptions when adding sales dictionary to lemonhead's sales record list
    try:
        lemonhead.enter_sales_for_today(day_0_sales)

    except InvalidSalesItemError:
        print("One of the items in day_0_sales is not in Lemonhead's Lemonade Stand's menu!")

    else:
        #print the total profit of the stand, which only executes if the InvalidSalesItemError is not raised
        print(lemonhead.total_profit_for_stand())




"""run the program, but include code that makes sure that the main() function only executes once 
if the program is ran as a script or as an imported module"""
if __name__ == '__main__':
    main()