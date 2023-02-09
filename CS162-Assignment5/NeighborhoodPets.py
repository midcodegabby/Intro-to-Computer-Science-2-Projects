#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/8/23
#Description : This program is able to use a class NeighborhoodPets to add pets with associated species and owners to
#a private data member (pet dictionary, pet_dict), delete pets off of that dictionary, raise an exception when the
#user tries to add a pet to the dictionary that already has that pet's name, write the pet_dict to a new JSON file
#with a specified file name, retrieve the owner of a specific pet in the pet_dict, load another JSON file containing
#pet information into the pet_dict, thereby replacing the previous pet_dict information with the loaded JSON file
#information, and return a python set of all the species of pets in the pet_dict.

import json

#define exception
class DuplicateNameError(Exception):
    pass

class NeighborhoodPets:
    """This class simulates the pets in a neighborhood, and contains methods to add a pet, delete a pet, search for
    the owner of a pet, save the data to a JSON file, load data from a JSON file, and get a set of all pet species.
    """

    def __init__(self):
        #initialize private data members
        self._pet_dict = {}


    def add_pet(self, pet_name, pet_species, pet_owner):
        """This method takes 3 parameters, the name of the pet, the species of the pet, and the name of the pet's
        owner, and adds that pet to a dictionary of pets. If the added pet has a name that is the same as a pet
        already in the pet dictionary, then method will raise a DuplicateNameError and not add the pet to the dict."""

        #initialize new list for pet_species and pet_owner:
        pet_list = [pet_species, pet_owner]

        #screen out duplicate pet names
        if pet_name in self._pet_dict:
            raise DuplicateNameError

        #else statement to add the parameters to the pet_dict
        else:
            self._pet_dict[pet_name] = pet_list

    def delete_pet(self, pet_name):
        """This method takes as parameter the name of a pet and deletes that pet and its information from the pet_dict
        """

        #use if statement to delete the pet and its data from the pet_dict and filter out invalid pet_names
        if pet_name in self._pet_dict:
            del self._pet_dict[pet_name]

    def get_owner(self, pet_name):
        """This method takes as parameter the name of a pet and returns the pet's owner (name)"""

        #create if statement to filter out pet_names that do not exist in the pet_dict and return the pet's owner
        if pet_name in self._pet_dict:

            #return the second index of the pet_list associated with the given pet_name in the pet_dict, which is the
            #pet's owner
            return self._pet_dict[pet_name][1]

    def save_as_json(self, file_name):
        """This method takes as parameter the name of a file, and writes the pet_dict to the newly created JSON file
        created with the file name."""

        #create with statement to write the pet_dict into a JSON file with the same name as the passed in file
        with open(file_name, 'w') as outfile:
            json.dump(self._pet_dict, outfile)


    def read_json(self, file_name):
        """This method takes as parameter the name of a file to read and loads that file into the pet_dict, thereby
        replacing all current data in the pet_dict."""

        #use with statement to load the file_name data into the pet_dict
        with open(file_name, 'r') as infile:
            self._pet_dict = json.load(infile)

    def get_all_species(self):
        """This method returns a python set of the species of all pets in the pet_dict."""

        #initialize empty python set
        pet_set = set()

        #loop through all pet_names in the pet_dict
        for key in self._pet_dict:

            #add the 0th indexed value (the pet species) of the list associated with the key in the pet_dict to the set
            pet_set.add(self._pet_dict[key][0])

        return pet_set
