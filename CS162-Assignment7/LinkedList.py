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

    def is_empty(self):
        """This method returns True if the LinkedList is empty and False otherwise"""
        return self._head is None

    def rec_add(self, val, current=None):
        """This method recursively adds a Node that contains val to the end of the LinkedList, using a current
        default parameter that acts as the current node being checked"""

        #if statement to handle adding a Node to an empty LinkedList
        if self._head == None:
            self._head = Node(val)

        else:
            #create base case for recursion, where the recursion ends when the recursion gets to the last Node
            if current.next is None:
                current.next = Node(val)  # adds a node to the end of the LinkedList

            else:
                return self.rec_add(val, current.next)

    def add(self, val):
        """recursive add helper method"""
        self.rec_add(val, self._head)

    def rec_display(self, a_node):
        """This method recursively prints out the values in the LinkedList"""

        #if statement to handle empty LinkedList and act as base case
        if a_node is None:
            #print a new line
            print()

        else:
            #print the current node's data
            print(a_node.data, end=" ")

            #recursively call the next node to print data
            self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)

    def rec_remove(self, val, current=None):
        """This method recursively removes the node containing the parameter val from the LinkedList, and has a
        default parameter current that keeps track of the current node being checked"""

        #if statement to handle an empty LinkedList
        if self._head is None:
            return

        #if statement for case where the value to be removed is in the first node
        if self._head.data == val:

            #shift the node after the head node to be the new head node, thereby removing the node containing the val
            self._head = self._head.next

        #else statement handles cases where the val to be removed is not in the first node
        else:

            #create variables to hold the current node and the next node
            previous = current
            current = current.next

            #create base case for when the value is not in the LinkedList
            if previous.next == None:
                return

            #create base case that terminates the recursion when the current node holds the val parameter
            elif current.data == val:

                #splice out the current node
                previous.next = current.next

            else:
                #recursive step
                return self.rec_remove(val, current)

    def remove(self, val):
        """recursive remove helper method"""
        self.rec_remove(val, self._head)

    def rec_to_plain_list(self, current, result=None):
        """This method recursively returns a regular python list of the data in each Node of the LinkedList
        in correct order, with the current parameter signifying the current Node being added to a python
        regular list, which is a default argument called result"""

        #initialize a python list
        if result == None:
            result = []

        #create base case to terminate recursion
        if current == None:
            return result

        else:
            #add the current Node to the result python list
            result += [current.data]

            return self.rec_to_plain_list(current.next, result) #recursive step

    def to_plain_list(self):
        """recursive to_plain_list helper method"""
        return self.rec_to_plain_list(self._head)

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
link = LinkedList()
lst.add(0)
lst.add(1)
lst.add(2)
lst.add(3)
lst.add("beta")
lst.add(4)
lst.display()
lst.remove(4)
lst.display()
print(lst.to_plain_list())

