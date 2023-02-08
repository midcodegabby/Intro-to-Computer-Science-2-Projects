#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/6/23
#Description :

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
        """This method takes as parameter the name of a file and saves the file in JSON format with the name,
        file_name.json (saves the file as its name .json)"""

        #create with statement to write the file_name data into a json file with the same name
        with open(file_name.json, 'w') as outfile:
            json.dump(file_name)


    def read_json(self, file_name):
        """This method takes as parameter the name of a file to read and loads that file into the pet_dict, thereby
        replacing all current data in the pet_dict."""

        #use save_as_json method to


