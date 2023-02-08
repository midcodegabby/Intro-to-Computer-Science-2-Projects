#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/7/23
#Description : This program contains a class (NobelData) that contains a method that should search through a json file
#of nobel prize data (that was previously initialized, read, and stored into a private data member in the class init
#method) given year and category parameters, and return an alphabetically sorted list of the surnames of the winners
#for that year and category.

import json

class NobelData:
    """This class reads a JSON file containing data on Nobel Prizes and allows the user to search that data. This class
    will have an init method that both reads the file and stores the data in a private data member and a
    search_nobel method that takes as parameters a year and a category, and then returns a sorted list (in alphabetical
    order) of the surnames for the winners in that category for that year (max 3 people). 
    Categories: "chemistry", "economics", "literature", "peace", "physics", and "medicine"""

    def __init__(self):
        """This method reads the nobels.json file and stores it to a dictionary."""

        #use with statement to open, read, and store the nobels.json data to a private data member:
        with open('nobels.json', 'r') as infile:
            self._nobel_file = json.load(infile)

    def search_nobel(self, year, category):
        """This method takes the year and category as string parameters and returns a sorted list (in alphabetical
        order) of the surnames of the winners in that category for that year."""

        #initialize list of laureate surnames
        surname_lst = []

        #iterate through the indices of the list of prizes
        for index in self._nobel_file["prizes"]:

            #create if statement to narrow down iteration to the specified year and category
            if index["year"] == year and index["category"] == category:

                #iterate through the indices of the list of laureates
                for idx in index["laureates"]:

                    #append the surname associated with each indexed laureate to the surname_lst
                    surname_lst.append(idx["surname"])

        return sorted(surname_lst)
