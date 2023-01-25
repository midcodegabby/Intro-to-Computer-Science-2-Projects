#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 1/20/23
#Description : This project is supposed to simulate a library, having multiple classes
#that inherit from each other to create a connected environment. a big nose :)

#create exception for invalid library item:
class InvalidLibraryItemError(Exception):
    pass

class LibraryItem:
    """A LibraryItem object represents a library item that a Patron can check out of the library.
    its 6 data members are its (unique) library_item_id, its (non-unique) title, its location (ON_SHELF, ON_HOLD_SHELF,
    or CHECKED_OUT), checked_out_by, or the Patron who has checked it out, if any has, requested_by, or the Patron that
    has requested the LibraryItem (limit: 1), and the date_checked_out. When a LibraryItem is checked out, the day
    it was checked out will be set to the current_day of the Library."""

    #initialize data members and privatize them
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._checked_out_by = None
        self._requested_by = None

    def get_location(self):
        """This method retrieves the LibraryItem's location"""
        return self._location

    def get_library_item_id(self):
        """This method retrieves the LibraryItem's id"""
        return self._library_item_id

    def get_title(self):
        """This method retrieves the LibraryItem's title"""
        return self._title

    def get_requested_by(self):
        """This method retrieves the Patron that has requested the libraryitem"""
        return self._requested_by

    def get_checked_out_by(self):
        """This method retrieves the Patron that has checked out the libraryitem"""
        return self._checked_out_by

    def get_date_checked_out(self):
        """This method retrieves the LibraryItem's date of check out"""
        return self._date_checked_out

    #create set methods ASK IF ALLOWED
    def set_location(self, new_location):
        """this method sets the location data member of the LibraryItem object to a new passed in location"""
        self._location = new_location

    def set_requested_by(self, new_patron):
        """this methods sets the requested_by data member to a new_patron parameter"""
        self._requested_by = new_patron

    def set_checked_out_by(self, new_patron):
        """this methods sets the requested_by data member to a new_patron parameter"""
        self._checked_out_by = new_patron

#create 3 subclasses of LibraryItem:
class Book(LibraryItem):
    """This subclass of LibraryItem represents a Book LibraryItem, that has the same 6 data members as LibraryItem
    plus an author. A Book can be checked out for 21 days"""

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """retrieves the author of the book"""
        return self._author

    def get_check_out_length(self):
        """returns the amount of time that a book can be checked out for"""
        return 21

class Album(LibraryItem):
    """This subclass of LibraryItem represents an Album LibraryItem, that has the same 6 data members as LibraryItem
    plus an artist. An Album can be checked out for 14 days"""

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist =  artist

    def get_artist(self):
        """retrieves the artist of the album"""
        return self._artist

    def get_check_out_length(self):
        """returns the amount of time that an album can be checked out for"""
        return 14

class Movie(LibraryItem):
    """This subclass of LibraryItem represents a Movie LibraryItem, that has the same 6 data members as LibraryItem
    plus a director. A Movie can be checked out for 7 days"""

    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """retrieves the director of the movie"""
        return self._director

    def get_check_out_length(self):
        """returns the amount of time that a movie can be checked out for"""
        return 7

class Patron:
    """This class represents a Patron of the library that has 4 private data members: (unique) patron_id, (non_unique)
    name, a list of the Patron's checked_out_items, and the amount of debt a Patron has, in the form of fine_amount."""

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._fine_amount = 0

        #checked_out_items will be a list of LibraryItems
        #initialize a dictionary of checked_out_items
        self._checked_out_items = {}

    def get_fine_amount(self):
        """returns the fine_amount"""
        return self._fine_amount

    def get_name(self):
        """returns the name of the Patron"""
        return self._name

    def get_patron_id(self):
        """returns the Patron's id"""
        return self._patron_id

    def get_checked_out_items(self):
        """returns the library items that a patron has checked out"""
        return self._checked_out_items

    def add_library_item(self, library_item):
        """this method adds a specified library item to the checked_out_items dictionary, with the key being
        the library_item's id, and its corresponding value being the library_item object"""
        self._checked_out_items[library_item.get_library_item_id()] = library_item

    def remove_library_item(self, library_item):
        """this method removes a specified library item from the checked_out_items list and returns an InvalidLibraryItem
        error if no such item exists in the checked_out_items list"""
        if library_item.get_library_id in self._checked_out_items:
            del self._checked_out_items[library_item.get_library_id]

        else:
            raise InvalidLibraryItemError

    def amend_fine(self, money):
        """this method allows changes to happen to the fine_amount (either pay it off or allow it to increase in debt"""
        if money > 0:
            return self._fine_amount + money

        elif money < 0:
            return self._fine_amount + money

        else:
            return self._fine_amount

class Library:
    """This class represents a Library, which has 3 data members: holdings, or a list of LibraryItems that belong to
    the library, members, or a list of the Patrons that are members of the Library, and current_date, which is
    updated every time a LibraryItem or one of its sub-classes are checked out to the parameter date_checked_out"""

    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

        #initialize a compostional class to use elsewhere:


    def add_library_item(self, library_item):
        """"this method adds a LibraryItem to the holdings of the library"""
        self._holdings[library_item.get_library_item_id()] = library_item

    def add_patron(self, patron):
        """this method adds a patron to the members of the library"""
        self._members[patron.get_patron_id()] = patron

    def lookup_library_item_from_id(self, library_item_id):
        """this method returns the LibraryItem object corresponding to the passed in library_item_id, or None if
        the library_item_id does not exist in the holdings of the library"""
        if library_item_id in self._holdings:
            return self._holdings.get(library_item_id) #returns the value associated with the library_item_id key

        else:
            return None

    def lookup_patron_from_id(self, patron_id):
        """this method returns the Patron object corresponding to the passed in patron_id, or None if the patron_id
        does not exist in the members of the library"""
        if patron_id in self._members:
            return self._members.get(patron_id) #returns the value associated with the patron_id key

        else:
            return None

    def check_out_library_item(self, patron_id, library_item_id):
        """this method takes a patron_id and a library_id and returns "patron not found" if the patron is not
        in the library members dictionary, "item not found" if the libraryitem is not in the library holdings
        dictionary, "item already checked out" if the libraryitem is already checked out, or "item on hold by other
        patron" if the library item is already on hold. If none of the above situations apply, then this method
        updates the LibraryItem's checked_out_by, date_checked_out, and location data members. If the libraryitem was
        alreaady requested by the patron, then the libraryitem's requested_by data member is also updated. Lastly, this
        method will update the patron's dictionary of checked_out_items."""

        if patron_id not in self._members:
            return "patron not found"

        elif library_item_id not in self._holdings:
            return "item not found"

        elif patron_id in self._members and library_item_id in self._holdings:

            #check if any other patron has requested or checked out the library item:
            if self._holdings.get(library_item_id).get_checked_out_by() != None:
                return "item already checked out"

            elif self._holdings.get(library_item_id).get_requested_by() != None or self._holdings.get(patron_id):
                return "item on hold by other patron"

            #case for when no one has requested the library item:
            elif self._holdings.get(library_item_id).get_requested_by() == None or self._holdings.get(patron_id):

                #update location, checked_out_by, and date_checked_out
                patron_from_id = self._members.get(patron_id)
                checked_patron = self._holdings.get(library_item_id).get_checked_out_by()
                checked_patron = patron_from_id #maybe use composition to update the value of the data members:


                #update location somehow
                new_location = "CHECKED_OUT"

            #case for when the patron checking the libraryitem out already requested the libraryitem: must change
            #the requested_by data member in the libraryitem object to None, unless possible in the above case
            #elif self._holdings.get(library_item_id).get_requested_by() == self._holdings.get(patron_id):







lib = Library()

b1 = Book(123, "Great Gatsby", "richard")
a1 = Album(312, "blah", "mark")
m1 = Movie(436, "terminator", "dawkins")

p1 = Patron(967, "gabe")
p2 = Patron(926, "sasha")

lib.add_patron(p1)
lib.add_patron(p2)

lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_library_item(m1)

lib.lookup_patron_from_id(967)
lib.lookup_library_item_from_id(312)

lib.check_out_library_item(967, 312)

print(a1.get_checked_out_by())












