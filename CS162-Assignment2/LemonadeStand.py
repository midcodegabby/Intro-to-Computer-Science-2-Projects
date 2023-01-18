"""
Author : Gabriel Rodgers
GitHub Username : trashcoder8
Date : 1/18/23
Description :
"""

#create MenuItem class
class MenuItem:

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

