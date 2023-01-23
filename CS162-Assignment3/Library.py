#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 1/20/23
#Description : This project is supposed to simulate a library, having multiple classes
#that inherit from each other to create a connected environment. a

class LibraryItem:

    #initialize data members and privatize them
    def __init__(self, library_item_id, title, location, checked_out_by, requested_by, date_checked_out):
        self._library_item_id = library_item_id
        self._title = title
        self._location = location
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by
        self._date_checked_out = date_checked_out

        self._checked_out_by = None
        self._requested_by = None
        #somehow make it so a new libraryitem's location is on the shelf\

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

