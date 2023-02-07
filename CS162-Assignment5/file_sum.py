#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/6/23
#Description : this file is able to take a paremeter in the form of the name of a text file that
#contains a list of numbers (one per line) and write the sum of those numbers to a text file named sum.txt

def file_sum(txt_file_name):
    """this function takes as parameter the name of a text file containing a list of numbers (one per line),
    finds the sum of the values, then writes the sum of those values to a text file called sum.txt"""

    #initialize sum variable
    sum = 0

    #create with statement to read the contents of the file
    with open(txt_file_name, 'r') as infile:

        #create for loop to iterate through the lines of the file
        for line in infile:
            sum += float(line.strip()) #use float() to force contents of lines into float form that is operatable on


    #create with statement to write the sum to a text file called sum.txt
    with open('sum.txt', 'w') as outfile:
        outfile.write(str(sum)) #must use str() method to be able to use the write() method


