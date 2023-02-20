#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/18/23
#Description :

class Node:
    """represents a node in a linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT, with all methods done recursively. Its methods include add, remove,
    contains, insert, reverse, display, get_head, and to_plain_list.
    """

    def __init__(self):
        #head represents the first Node
        self._head = None

    def get_head(self):
        """This method returns the first Node object in the LinkedList"""
        return self._head

    def add(self, val):
        """recursive add helper method"""
        self.rec_add(val, self._head)

    def rec_add(self, val, current=None):
        """This method recursively adds a Node that contains val to the end of the LinkedList"""

        #if statement to handle adding a Node to an empty LinkedList
        if self._head == None:
            self._head = Node(val)

        else:
            #create base case for recursion, where the recursion ends when the recursion gets to the last Node
            if current.next is None:
                current.next = Node(val)  # adds a node to the end of the LinkedList

            else:
                return self.rec_add(val, current.next)

    def display(self):
        """This method recursively prints out the values in the LinkedList"""

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)

    def remove(self, val):
        """This method recursively removes the node containing the parameter val from the LinkedList"""


    def is_empty(self):
        """This method returns True if the LinkedList is empty and False otherwise"""
        return self._head is None


    def to_plain_list(self):
        """This method recursively returns a regular python list of the data in each Node of the LinkedList
        in correct order"""


    def contains(self, val):
        """This method recursively takes a value as parameter and returns True if the value is in one of the Nodes in
        the LinkedList and False otherwise"""


    def insert(self, val, pos):
        """This recursive method takes as parameters a value and a position for that value to be inserted in the LinkedList as
        a node. pos = 0 means the value becomes the head node, pos greater than the length of the LinkedList means the
        value becomes a node at the end of the LinkedList, and pos in between means the value becomes a node at that
        position in the LinkedList."""


    def reverse(self):
        """This method recursively reverses the order of the LinkedList by modifying each Node's next data member and
        does not change the data values of any Nodes."""



lst = LinkedList()
lst.add(0)
lst.add(1)
lst.add(2)
lst.add(3)
lst.add("beta")
lst.display()