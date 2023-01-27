#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 1/20/23
#Description : This project is supposed to simulate a library, having multiple classes
#that inherit from each other to create a connected environment. The class LibraryItem is a superclass for
#the subclasses Book, Movie, and Album. This simultated library is able to store an item's location, the amount of time
#since it has been checked out, and all of its data members (see docstring under LibraryItem for complete explanation).
#This simulated library also is able to give fines out to members (patrons) for late items, allow members to pay their
#fine back, and also find relevant data members of different objects from their id, including a LibraryItem's title
#or the name of a patron.

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

    #create set methods
    def set_location(self, new_location):
        """this method sets the location data member of the LibraryItem object to a new passed in location"""
        self._location = new_location

    def set_requested_by(self, new_patron):
        """this methods sets the requested_by data member to a new_patron parameter"""
        self._requested_by = new_patron

    def set_checked_out_by(self, new_patron):
        """this methods sets the requested_by data member to a new_patron parameter"""
        self._checked_out_by = new_patron

    def set_date_checked_out(self, check_out_date):
        """this method sets the date_checked_out to a new_date parameter"""
        self._date_checked_out = check_out_date

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
    name, a dictionary of the Patron's checked_out_items (keys being the ids of checked out library items and the
    corresponding values being the attached libraryitems), and the amount of debt a Patron has, in the form of
    fine_amount."""

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._fine_amount = 0

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
        """this method removes a specified library item from the patron's checked_out_items dictionary and returns None
         if no such item exists in the patron's checked_out_items list"""

        if library_item.get_library_item_id() in self._checked_out_items:
            del self._checked_out_items[library_item.get_library_item_id()]

        else:
            return None

    def amend_fine(self, money):
        """this method allows changes to happen to the fine_amount (either pay it off or allow it to increase
        in debt)"""

        if money > 0 or money < 0:
            self._fine_amount = self._fine_amount + money
            return self._fine_amount

        else:
            return self._fine_amount

class Library:
    """This class represents a Library, which has 3 data members: holdings, or a dictionary of LibraryItems that belong
    to the library (keys are LibraryItem ids, values are corresponding LibraryItem objects, members, or a dictionary
    of the Patrons that are members of the Library (keys being patron ids and values being corresponding patron
    objects), and current_date, which is updated every time a LibraryItem or one of its sub-classes are checked out
    to the parameter date_checked_out"""

    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def get_current_date(self):
        """this method returns the current date of the library"""
        return self._current_date

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
        method will update the patron's dictionary of checked_out_items and return "check out successful."""

        if patron_id not in self._members:
            return "patron not found"

        elif library_item_id not in self._holdings:
            return "item not found"

        elif patron_id in self._members and library_item_id in self._holdings:

            #check if any other patron has requested or checked out the library item:
            if self.lookup_library_item_from_id(library_item_id).get_checked_out_by() != None:
                return "item already checked out"

            #make if statements for handling a checkout in which the patron checking out the item is either the
            #patron that requested the item or is not the one that requested the item
            elif self.lookup_library_item_from_id(library_item_id).get_requested_by() != None:

                #this if statement handles the case where the item requester is the patron attempting check out
                if self.lookup_library_item_from_id(library_item_id).get_requested_by() == self.lookup_patron_from_id(patron_id):

                    # update requested_by LibraryItem data member to None (in the case of the patron checking the
                    # item out being the same patron that requested the item)
                    self.lookup_library_item_from_id(library_item_id).set_requested_by(None)

                    # update checked_out_by LibraryItem data member to the patron object
                    self.lookup_library_item_from_id(library_item_id).set_checked_out_by(self.lookup_patron_from_id(patron_id))

                    # update date_checked_out LibraryItem data member to the date of checkout
                    self.lookup_library_item_from_id(library_item_id).set_date_checked_out(self._current_date)

                    # update location LibraryItem data member to "CHECKED_OUT"
                    self.lookup_library_item_from_id(library_item_id).set_location("CHECKED_OUT")

                    # add library_item to patron's dictionary of checked out items
                    self.lookup_patron_from_id(patron_id).add_library_item(self.lookup_library_item_from_id(library_item_id))

                    return "check out successful"

                #this else statement handles cases where the patron trying to check the LibraryItem out is not
                #the patron that has requested the LibraryItem
                else:
                    return "item on hold by other patron"

            #case for when no one has requested the library item or the patron themself has requested the item:
            elif self.lookup_library_item_from_id(library_item_id).get_requested_by() == None:

                #update checked_out_by LibraryItem data member to the patron object
                self.lookup_library_item_from_id(library_item_id).set_checked_out_by(self.lookup_patron_from_id(patron_id))

                #update date_checked_out LibraryItem data member to the date of checkout
                self.lookup_library_item_from_id(library_item_id).set_date_checked_out(self._current_date)

                #update location LibraryItem data member to "CHECKED_OUT"
                self.lookup_library_item_from_id(library_item_id).set_location("CHECKED_OUT")

                #add library_item to patron's dictionary of checked out items
                self.lookup_patron_from_id(patron_id).add_library_item(self.lookup_library_item_from_id(library_item_id))

                return "check out successful"

    def return_library_item(self, library_item_id):
        """this method takes a library_item_id and returns the libraryitem associated with it back to the library.
        If the libraryitem does not exist in the library's holdings, then the method returns "item not found". If the
        libraryitem is not checked out, then the method returns "item already in library". If the library_item_id is
        checked out and exists, then the method updates the patron's (that is returning the libraryitem)
        checked_out_items dictionary. This method also updates the libraryitem's location depending on whether or not
        another patron has requested the item. This method also updates the libraryitem's checked_out_by data member,
        and finally returns "return successful"."""

        #create if statements to filter out invalid parameters
        if library_item_id not in self._holdings:
            return "item not found"

        #this if statement handles libaryitems that are not checked out:
        elif self.lookup_library_item_from_id(library_item_id).get_checked_out_by() == None:
            return "item already in library"

        #this if statement handles library items that are checked out and therefore will be returned:
        elif self.lookup_library_item_from_id(library_item_id).get_checked_out_by() != None:

            #update Patron's checked_out_items dictionary
            self.lookup_library_item_from_id(library_item_id).get_checked_out_by().remove_library_item(self.lookup_library_item_from_id(library_item_id))

            #update LibraryItem location depending on whether or not another patron has checked out the item
            if self.lookup_library_item_from_id(library_item_id).get_requested_by() == None:
                self.lookup_library_item_from_id(library_item_id).set_location("ON_SHELF")

            elif self.lookup_library_item_from_id(library_item_id).get_requested_by() != None:
                self.lookup_library_item_from_id(library_item_id).set_location("ON_HOLD_SHELF")

            #update the LibraryItem's checked_out_by data member
            self.lookup_library_item_from_id(library_item_id).set_checked_out_by(None)

            return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """this method allows a patron to request a LibraryItem by id. If the specified patron (by id) is not
          in the library's members, this method returns "patron not found". If the library_item_id has no LibraryItem
          attached to it or is not in the Library's holdings, then this method returns "item not found".
          This method allows only one patron to request a specific LibraryItem at a time; if a patron tries to request
          an item that has already been requested by another patron this method returns "item already on hold". If the
          above situations are not triggered and a LibraryItem is allowed to be requested, then this method sets the
          patron to the LibraryItem's requested_by data member, sets the LibraryItem's location to "ON_HOLD_SHELF"
          (only if the LibraryItem's location previously was "ON_SHELF"), and returns the string "request successful"
          """

        #create if statements to filter out invalid parameters
        if patron_id not in self._members:
            return "patron not found"

        elif library_item_id not in self._holdings:
            return "item not found"

        #if statement to handle situation where another patron has already requested the LibraryItem
        elif self.lookup_library_item_from_id(library_item_id).get_requested_by() != None:
            return "item already on hold"

        #this if statement handles a valid request
        elif self.lookup_library_item_from_id(library_item_id).get_requested_by() == None:

            #update LibraryItem's requested_by data member to the patron
            self.lookup_library_item_from_id(library_item_id).set_requested_by(self.lookup_patron_from_id(patron_id))

            #update LibraryItem's location
            if self.lookup_library_item_from_id(library_item_id).get_location() == "ON_SHELF":
                self.lookup_library_item_from_id(library_item_id).set_location("ON_HOLD_SHELF")

            elif self.lookup_library_item_from_id(library_item_id).get_location() == "CHECKED_OUT":
                self.lookup_library_item_from_id(library_item_id).set_location("CHECKED_OUT")

            return "request successful"

    def pay_fine(self, patron_id, payment):
        """this method takes a patron_id and a payment and changes the patron's fine_amount using the payment."""

        #use if statements to filter out invalid inputs
        if patron_id not in self._members:
            return "patron not found"

        #use if statement to deal with amending fines
        elif patron_id in self._members:
            self.lookup_patron_from_id(patron_id).amend_fine(payment)

            return "payment successful"

    def increment_current_date(self):
        """this method increments the current date and increases each Patron's fines by 10 cents for every overdue
        LibraryItem they have checked out"""

        #increment current date:
        self._current_date = self._current_date + 1

        #loop through all patrons in the Library's members dictionary
        for key in self._members:

            #create variable to be used in lower code/simplify lower code
            patron = self.lookup_patron_from_id(key)

            #loop through all LibraryItems in each patron's checked_out_items dictionary
            for key in self.lookup_patron_from_id(key).get_checked_out_items():

                #create if statements to handle fines for if the time since checking the LibraryItem out is
                #greater than the LibraryItem's checkout length
                if self._current_date - self.lookup_library_item_from_id(key).get_date_checked_out() > self.lookup_library_item_from_id(key).get_check_out_length():
                    patron.amend_fine(-0.10)
