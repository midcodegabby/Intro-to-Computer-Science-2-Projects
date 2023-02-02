#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/1/23
#Description : This program includes a modified version of the bubble_sort and insertion_sort functions from the week
#4 exploration, in which both modified versions sort integers in ascending order but also return a tuple of the amount
#of comparisons and exchanges the functions complete in their sorting processes.

def bubble_count(a_list):
    """Sorts a_list in ascending order, while also counting the number of comparisons and exchanges done (and returning
    both values) in the process of sorting the list."""

    #initialize comparison and exchange variables
    comparisons = 0
    exchanges = 0

    #for loop for iterating through the entire list
    for pass_num in range(len(a_list) - 1):

        #additional for loop for iterating through unsorted list inside the original list;
        #subtracting pass_num creates an iterable list containing all unsorted values
        for index in range(len(a_list) - 1 - pass_num):

            #add 1 to comparisons for every time this for loop is ran
            comparisons += 1

            #this if statement checks if the elements being compared are in order or not
            if a_list[index] > a_list[index + 1]:

                #add 1 to exchanges for every time the values in the list need to be swapped
                exchanges += 1

                #create variable to hold the higher value
                temp = a_list[index]

                #takes the lower value and assigns it to the lower value's index and the higher value's index
                a_list[index] = a_list[index + 1]

                #takes the higher value and assigns it to the lower value's index, thereby completing the exchange
                a_list[index + 1] = temp

    return comparisons, exchanges


def insertion_count(a_list):
    """This function takes as parameter a list of numbers and sorts them from greatest to smallest using insertion
    sort. This function will also count and return the number of comparisons and exchanges done to sort the list."""

    #initialize comparison and exchange variables
    comparisons = 0
    exchanges = 0

    #create for loop to loop through the indices of the list, starting from index 1 instead of 0.
    for index in range(1, len(a_list)):

        val = a_list[index]

        #create an index for the value to the left of val, which will be the value being compared with val
        pos = index - 1

        #create while loop to loop through the list for as long as there are values to the left of the index (or val)
        while pos >= 0:

            #adds 1 to comparisons every time the while loop is executed, which accounts for cases where no exchange is
            #done and cases where multiple exchanges are done
            comparisons += 1

            #create if statement for cases where val is less than the pos value (value to left of val),
            #and therefore need to be exchanged
            if a_list[pos] > val:

                #assigns the value associated with the pos index to the pos index and val's index
                a_list[pos + 1] = a_list[pos]

                #subtract 1 from pos, thereby moving the pointer of the insertion sort function an index lower
                pos -= 1

                #add 1 to exchanges for every time this if statement is iterated through
                exchanges += 1

                #assign the previously pointed to index value to be val, thereby completing the exchange and swapping
                #the indexed val with the value to its left
                a_list[pos + 1] = val

            #create else statement to end the while loop when no more exchanges need to be done for that index value
            else:
                break

    return comparisons, exchanges
