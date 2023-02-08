#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/7/23
#Description :

import json

class SatData:
    """This class is able to read a JSON file containing data on 2010 SAT results in NYC and write that data
    to a text file in CSV format. The init method for this class will read and load the data onto a private
    data member, and the save_as_csv method will take as parameter a list of DBNs  and save that data to an output
    file called output.csv in ascending order of DBN."""

    def __init__(self):
        #create with statement to read and load the data on the JSON file onto a private data member
        with open('sat.json', 'r') as infile:
            self._sat_file = json.load(infile)

    def save_as_csv(self, dbn_list):
        """This method takes as a parameter a list of DBN (district bureau numbers) and writes the corresponding data
        associated with those DBNs to a new output file called output.csv in a format of including column headers
        and the DBN-specific information, in ascending DBN order."""

        #create with statement to write the data to the output.csv file
        with open('output.csv', 'w') as outfile:
            print()