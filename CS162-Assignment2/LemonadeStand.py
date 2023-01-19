"""
Author : Gabriel Rodgers
GitHub Username : trashcoder8
Date : 1/18/23
Description :
"""

#create exception
class InvalidSalesItemError(Exception):
    """user defined exception for an inputted sales item that does not exist in the menu_dict"""
    pass

class InvalidSalesNumberError(Exception):
    pass

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
    """represents a sale day class with 2 private data members: current day (integer)
    and a (dictionary) containing the (keys) names of sold items and the (values) number of each respective item sold"""

    # initialize data member objects in the class
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
        self._day = 0

        #initialize the menu to an empty dictionary:
        self._menu_dict = {}

        #initalize the sales_record list:
        self._sales_record = []


    #define a function to retrieve the private data member name of lemonade stand
    def get_name(self):
        """retrieves the private data member name (of the LemonadeStand)"""
        return self._name

    def add_menu_item(self, menu_item):
        """This method should take a MenuItem object and add it to the menu_dict, with the key being
        the MenuItem's name, and the corresponding value being the MenuItem object itself."""
        self._menu_dict[menu_item._name] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """This method should take a user-inputted dictionary of (keys) names of sold_items and
        (corresponding values) how many of each of the sold_items were sold. Then, this method should ensure
        that if a menu_item name is missing from sales_dict, then the method will automatically assign a
        value of zero sells for that item. This method should also raise an InvalidSalesItemError exception
        if a key in the sales_dict does not match any of the menu_item names. If the menu_item name is valid and
        in the inputted sales_dict, then the method should create a new SalesForDay object using the current day
        and the sales_dict, add that new SalesForDay object to the sales_record list, and then increment the current
        day by 1."""

        """create if statements to make sure that if an inputted sold_item (in sales_dict) does not exist, then
        the InvalidSalesItemError is raised. Lastly, to make sure that if an inputted sold_item corresponds to a 
        menu_item._name in menu_dict, then a new SalesForDay object is created."""

        #privatize sales_dict dictionary
        self._sales_dict = sales_dict

        #create for loop to loop through all keys in the sales_dict dictionary
        for key in self._sales_dict:

            # create elif statement to add the sales_dict to a new SalesForDay class
            if key in self._menu_dict:

                sales_for_day_x = SalesForDay(self._day, self._sales_dict)

                self._sales_record.append(sales_for_day_x)

            #create elif statement to deal with sales_dict keys that are not in the menu_dict keys
            elif key not in self._menu_dict:

                raise InvalidSalesItemError

            """ pretty much useless // delete if not needed
            #create elif statement to automatically set unsold menu items number of items sold to zero if not found in
            #sales_dict
            #elif self._menu_dict.keys() not in self._sales_dict:
                #exclude the missing menu item from the SalesForDay object or set it to zero?
                #print("That item was not sold today")
            """


    def sales_of_menu_item_today(self, day, menu_item):
        """This method should retrieve """

    def total_sales_for_menu_item(self, menu_item):
        """This method should take the name of a menu item and return the total number of that item
        sold over the history of the stand. This method should use sales_of_menu_item_today to find the
        required value"""

        return #value

    def total_profit_for_menu_item(self, menu_item):
        """This method should take the name of a menu_item and return the total profit on that item
        over the history of the stand. Should use total_sales_for_menu_item method"""

    def total_profit_for_stand(self):
        x = 1
        return x



#create test dictionary
day_0_sales = {
    "lemonade" : 5,
    "cookies" : 3
}

l = LemonadeStand("Gabe's Lemonade Stand")

item1 = MenuItem("cookies", 1, 2)
l.add_menu_item(item1)
item2 = MenuItem("lemonade", .5, 3)
l.add_menu_item(item2)

print(l._menu_dict)

ar = {
    "bastard" : 4,
    "lemonade" : 6

}

for key in ar:

    if key in l._menu_dict.keys():
        print("yes")
    else:
        print("no")
        print(l._menu_dict.keys())
        print(ar.get(key))
        print(ar.keys())


"""
for key in l._menu_dict:

    if type(l._menu_dict[key]) == str:
        print("valid")
    else:
        print(type(l._menu_dict.values()))
"""