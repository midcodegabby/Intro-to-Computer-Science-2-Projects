#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 1/30/23
#Description : This program is a modification of the basic insertion sort function, in which the function sorts a list
#of strings instead of numbers. This sorting will ignore capital letters, and will sort the strings in alphabetical
#order, in which strings starting with the letter z come after a-y (for example), and should sort strings with the
#same first letter the same way in regards to their second letter and etcetera for even more matching letters in
#different strings.

#basic insertion sort function:
def string_sort(string_list):
    """This function takes as a parameter a list of strings and sorts the strings in alphabetical order using insertion
    sort. If the first two letters of two strings are the same, then the function will sort them alphabetically with
    their following letters. To ignore case, this function uses the built-in method str.casefold(), which returns a
    lowercase form of the string, therefore trivializing the use of cases."""

    #create for loop to loop through the indices of the string_list, starting from index 1 instead of 0.
    for index in range(1, len(string_list)):

        #assign the string associated with the index in string_list to the variable 'value'
        value = string_list[index]

        #create an index for the value to the left of the string being pulled
        pos = index - 1

        #create while loop to continue sorting the list in descending order, using the .casefold() method to trivialize
        #string cases
        while pos >= 0 and string_list[pos].casefold() > value.casefold():

            #reassigns the value of the left value to the 'value' index
            string_list[pos + 1] = string_list[pos]

            #the following two lines of code assign the lower 'value' to the left index
            pos -= 1

        string_list[pos + 1] = value
