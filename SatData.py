#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/7/23
#Description : This program contains a class SatData, which is able to read and load the data in a JSON file
#(containing data on 2010 SAT results in New York City) onto a private data member. The class SatData also has
#an additional method, save_as_csv that allows the user to input a list of DBNs (district bureau numbers), to which
#the program writes the corresponding DBN data found in the json file (but stored in the newly created private data
#member) to a new output.csv file with column headers.

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

        #create list for output.csv column headers
        column_header = ["DBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean",
        "Writing Mean"]

        #create a with statement to hardcode the column headers for the output.csv file
        with open('output.csv', 'w') as outfile:
            for column in column_header:
                outfile.write(column + ',')

            #create new outfile.write() statement to move to next line after inputting all relevant data
            outfile.write("\n")

        #create for loop to iterate through list of data in the sat_file
        for index in self._sat_file["data"]:

            #create if statement to focus on data with DBNs corresponding to the dbn_list parameter
            if index[8] in dbn_list: #where index represents a list of data associated with a single DBN

                #create with statement to append the specified data from the sat_file to the output.csv file
                with open('output.csv', 'a') as outfile:

                    #create for loop to iterate through the needed data in the specified DBN list
                    for idx in range(8, len(index)):
                        outfile.write(str(index[idx]) + ',')  #the ',' puts a comma between each written index value

                    #create new outfile.write() statement to move to next line after inputting all relevant data
                    outfile.write('\n')
