#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 1/11/23
#Description : This program is a

class Box:
    """this class represents a box with parameters of length, width, and height of the box (this class
    privatizes these parameters). This class also has a method 'volume' that returns the volume of the
    box. This class also has get methods to retrieve each data member. """

    #initialize and privatize data members
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    #create get methods for the Box class
    def get_length(self):
        """"This method retrieves the length data member of the Box class."""
        return self._length

    def get_width(self):
        """"This method retrieves the width data member of the Box class."""
        return self._width

    def get_height(self):
        """"This method retrieves the height data member of the Box class."""
        return self._height

    def volume(self):
        """this method calculates and returns the volume of the Box object."""

        #calculate box volume
        box_vol = self._length * self._width * self._height

        return box_vol

#create sorting function
def box_sort(box_list):
    """This function takes as parameter a list of Box objects and sorts the objects from greatest
    volume to least volume using insertion sort."""

    #create for loop to loop through the indices of the box_list, starting from index 1 instead of 0.
    for index in range(1, len(box_list)):

        #assign the volume associated with the indexed box in box_list to the variable 'volume'
        value = box_list[index]

        #create an index for the value to the left of the volume being pulled
        pos = index - 1

        #create while loop to continue sorting the list in descending order
        while pos >= 0 and box_list[pos].volume() < value.volume():

            #reassigns the value of the left value to the volume's index
            box_list[pos + 1] = box_list[pos]

            #the following two lines of code assigns the higher 'value' to the left index
            pos -= 1

        box_list[pos + 1] = value

