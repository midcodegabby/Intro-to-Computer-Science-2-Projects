#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 3/1/23
#Description :

import time, random, functools
from matplotlib import pyplot as plt

def sort_timer(func):
    """This decorator function times how many seconds it takes for the decorated function func (argument) to
    run. This function contains an inner function called wrapper that returns the elapsed time."""

    #use decorator on the wrap function to preserve the decorated function's metadata
    @functools.wraps(func)

    def wrapper(*args, **kwargs):
        """This wrapper function modifies the function passed into it by returning the time it takes to run the
        function. It does so by recording the time before the function call, then calling the  function, then recording
        the time after the function call, then returning the difference between those two times."""

        #define start time
        t_start = time.perf_counter()

        #call function
        func(*args, **kwargs)

        #define end time
        t_end = time.perf_counter()

        #return the elapsed time
        return t_end - t_start

    return wrapper

#copied code for bubble_sort with decoration
@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp

#copied code for insertion_sort with decoration
@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

def list_gen(limit):
    """This generator function creates a generator object with n = limit terms of randomly generated numbers between
    1 and 10000."""

    #initalize counter variable to use to terminate generation of random numbers
    num = 0

    #while loop to generate n = limit randomly generated values
    while num < limit:

        num += 1

        #yield a randomly generated integer between 1 and 10000
        yield random.randint(1,10000)


def compare_sorts(ins_sort, bub_sort):
    """This function takes two decorated functions (decorated versions of bubble_sort and insertion_sort) as
    parameters. The function then randomly generates a list of 1000 numbers by calling the list_gen function and
    iterating through that generator object and assigning each value in the generator to an index in a list.
    Then this function makes a separate copy of that
    list. Then this function assigns each list to a dictionary with key value pairs of 1,2,3,4, and lists containing
    1000, 2000, 3000, 4000, etc. random integers, resulting in two identical dictionaries to be used further.
    Then the function should call the decorated bubble_sort (bub_sort) to find the time it takes to sort one of
    the list copies, and then call the decorated insertion_sort (ins_sort) to find the time it takes to sort the
    other list copy. This function should then repeat this for lists of size 2000, 3000, all the way to 10000. All
    randomly generated numbers in the lists should be integers in the range of 1 <= num <= 10000. Each time value for
    each list size for each sort method should constitute a data point to be graphed. The function will end up with
    10 data points of (x = list size, y = time to run) for each sort method (total 20 data points). After all data
    points are gathered, this function will graph them."""

    #initialize dictionary to hold all generators containing 1000, 2000, ... 10000 random values
    gen_dict = {}

    #initalize dictionary to hold all lists containing 1000, 2000, ... 10000 random values and its copy dictionary
    list_dict_1 = {}
    list_dict_2 = {}

    #loop to generate generators
    for idx in range(1,11):

        #add a generator to each key in the generator dictionary, in which a key represents a number 1-10 and the value
        #associated with that key refers to the generator object with 1000*key random integers in it
        gen_dict[idx] = list_gen(1000*idx)

    #loop through all keys in the gen_dict
    for key in gen_dict:

        #initalize a list for the values in the generator to reside in
        rand_list_1 = []

        #loop to convert the generator associated with the currently iterated key into a list
        for index in gen_dict[key]:

            #add each value in the generator to the rand_list
            rand_list_1.append(index)

        #copy the rand_list_1
        rand_list_2 = list(rand_list_1)

        #add the newly created list of random numbers (rand_list) and its copy to the list_dict_1 and list_dict_2
        list_dict_1[key] = rand_list_1
        list_dict_2[key] = rand_list_2

    #initialize 3 lists: a list of the amount of values in each of the randomly generated lists, a list of the time
    #to sort each list (1000 val, 2000 val, etc.) using insertion sort, and a list of the time to sort each list
    #using bubble sort.
    num_list = [] #this will act as the graph's x axis
    ins_sort_time = []
    bub_sort_time = []

    #loop through keys of the list_dict_1 to record time to sort with insertion sort (ins_sort)
    for key in list_dict_1:

        #add the key*1000 to the num_list list
        num_list.append(key*1000)

        #add the time to sort the list paired with the key in the list_dict to the ins_sort_time list
        ins_sort_time.append(ins_sort(list_dict_1[key]))

    #loop through keys of the list_dict_2 to record time to sort with bubble sort (bub_sort)
    for key in list_dict_2:

        #add the time to sort the list paired with the key in the list_dict to the bub_sort_time list
        bub_sort_time.append(bub_sort(list_dict_2[key]))













