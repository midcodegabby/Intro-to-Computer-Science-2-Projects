#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/22/23
#Description : This program serves as a recursive LinkedList class, inwhich all of the LinkedList methods are
#done recursively. The LinkedList class uses Nodes with two data members: a Node's data, and a Node's next node, and
#connects those Nodes in order of addition. The methods included in this program are get_head and recursive versions of
#add, remove, contains, insert, reverse, and to_plain_list. The head node refers to the first node in the LinkedList.
#the add method adds a new node containing a value passed in to the end of the LinkedList and the remove method
#removes a node containing a passed in value from the LinkedList (by splicing it out). The to_plain_list method returns
#a regular python list of the data in each node in correct order, the contains method returns True if the value is in
#one of the node inside the LinkedList and False otherwise, the insert method inserts a node containing a value passed
#in at a specific point in the LinkedList, which is specified by a parameter. Lastly, the reverse method reverses the
#order of the LinkedList without changing any of the nodal data. This program allows the user to manipulate,
#create, and print out a LinkedList.

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

    def rec_add(self, val, current):
        """This method recursively adds a Node that contains val to the end of the LinkedList, using a current
        parameter that acts as the current node being checked"""

        #if statement to handle adding a Node to an empty LinkedList
        if self._head == None:
            self._head = Node(val)

        else:
            #create base case for recursion, where the recursion ends when the recursion gets to the last Node
            if current.next is None:
                current.next = Node(val)  #adds a node to the end of the LinkedList

            else:
                return self.rec_add(val, current.next)

    def add(self, val):
        """recursive add helper method"""
        self.rec_add(val, self._head)


    def rec_remove(self, val, current):
        """This method recursively removes the node containing the parameter val from the LinkedList, and has another
        parameter called current that keeps track of the current node being checked"""

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


    def rec_contains(self, val, current):
        """This method recursively takes a value as parameter and returns True if the value is in one of the Nodes in
        the LinkedList and False otherwise. This function also takes as parameter the current node being checked."""

        #create base cases to terminate recursion
        if current == None:
            return False

        elif current.data == val:
            return True

        else:
            #recursive step
            return self.rec_contains(val, current.next)

    def contains(self, val):
        """recursive contains helper method"""
        return self.rec_contains(val, self._head)


    def rec_insert(self, val, pos, node_num, current):
        """This recursive method takes as parameters a value and a position for that value to be inserted in the
        LinkedList as a node. pos = 0 means the value becomes the head node, pos greater than the length of the
        LinkedList means the value becomes a node at the end of the LinkedList, and pos in between means the value
        becomes a node at that position in the LinkedList. Additional parameters include the node_num (represents the
        place number of the node being checked), and current, which represents the current node being checked."""

        #define previous variable (signifies the current node being checked) and the node to be spliced into the list
        previous = current
        spliced_node = Node(val)

        #if statement so that the recursion does not keep going after the end of the LinkedList is reached
        if current != None:

            #move the current variable up by one node
            current = current.next

        #create base cases to terminate recursion
        #this base case handles a case where the LinkedList has zero Nodes in it or the end of the LinkedList is
        #reached
        if previous == None:
            self.add(val)

        #this base case handles a case where the position is zero
        elif pos == 0:

            #assign head node to be the spliced_node
            self._head = spliced_node
            self._head.next = previous

        #this base case handles a case where the insertion point is found inside the bounds of the LinkedList
        elif node_num + 1 == pos:

            #insert the spliced_node into the LinkedList
            previous.next = spliced_node
            spliced_node.next = current

        else:

            #recursive step
            return self.rec_insert(val, pos, node_num+1, current)

    def insert(self, val, pos):
        """recursive insert helper method"""
        self.rec_insert(val, pos, 0, self._head)


    def rec_reverse(self, current, previous=None):
        """This method recursively reverses the order of the LinkedList by modifying each Node's next data member and
        does not change the data values of any Nodes. The current parameter represents the current Node being operated
        on, and the default argument previous represents the node before the current node."""

        #create base case
        if current == None:

            #assign the first node to be the previous recursed current node (or previous node in this recursion)
            self._head = previous

        else:
            #define following variable, then set the current node's next node to be the previous node
            following = current.next

            current.next = previous

            #recursive step passes the next node in as the current node and the current node in as the previous node
            return self.rec_reverse(following, current)

    def reverse(self):
        """recursive reverse helper method"""
        self.rec_reverse(self._head)

