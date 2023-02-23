#skeleton framework of the LinkedList code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None


    def rec_add(self, val, current=None):
        if self._head == None:
            self._head = Node(val)

        else:
            if current.next is None:
                current.next = Node(val)

            else:
                return self.rec_add(val, current.next)

    def add(self, val):
        self.rec_add(val, self._head)


    def rec_to_plain_list(self, current, result=None):
        if result == None:
            result = []
        if current == None:
            return result

        else:
            result += [current.data]

            return self.rec_to_plain_list(current.next, result)

    def to_plain_list(self):
        return self.rec_to_plain_list(self._head)

    def rec_insert(self, val, pos, node_num, current):
        """This recursive method takes as parameters a value and a position for that value to be inserted in the LinkedList as
        a node. pos = 0 means the value becomes the head node, pos greater than the length of the LinkedList means the
        value becomes a node at the end of the LinkedList, and pos in between means the value becomes a node at that
        position in the LinkedList."""

        # define previous and current and the node to be spliced variables for insertion
        previous = current
        spliced_node = Node(val)

        if previous != None:
            current = current.next

        # else:
        # self.add(val)

        # create base cases to terminate recursion
        # this base case handles a case where the LinkedList has zero Nodes in it
        if previous == None:
            self.add(val)

        # this base case handles a case where the position is zero
        elif pos == 0:

            # assign head node to the new Node
            self._head = spliced_node
            self._head.next = previous

        # this base case handles a case where the insertion point is found inside the bounds of the LinkedList
        elif node_num == pos:

            # insert the new node into the LinkedList
            previous.next = spliced_node
            spliced_node.next = current

        # this base case handles a case where the pos is outside the bounds of the LinkedList or at the end of it
        # if pos >= len(self.to_plain_list()):
        # self.add(val)

        else:

            # recursive step
            return self.rec_insert(val, pos, node_num + 1, current)

    def insert(self, val, pos):
        self.rec_insert(val, pos, 0, self._head)

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




pos_lst = LinkedList()
neg_lst = LinkedList()
pos_lst.add(0)
pos_lst.add(1)
pos_lst.add(2)
pos_lst.add(3)
pos_lst.add("beta")
pos_lst.add(4)
pos_lst.display()
#lst.remove(4)
pos_lst.insert(8,1)
pos_lst.display()
pos_lst.reverse()
pos_lst.display()


#neg_lst.add(0)
#neg_lst.add(-1)
#neg_lst.add(-42)
#neg_lst.add(-3)
#neg_lst.add("beta")
#neg_lst.add(-15)

#neg_lst.display()
#neg_lst.insert(4,45)
#neg_lst.display()

