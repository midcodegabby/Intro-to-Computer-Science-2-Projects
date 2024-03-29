"""
Author : Gabriel Rodgers
GitHub Username : trashcoder8
Date : 1/11/23
Description :
This program is supposed to get me a passing grade on the first assignment in this CS 162 Class by
demonstrating competent use of classes and separating interface from implementation. For an overview,
this program should contain a function 'basic_stats' and a class 'Student' (containing 2 private data
members: a student's name and grade). The basic_stats function should take a list of 'Student'
objects as a parameter and return the mean, median, and mode of all the grades. Additionally, the
Student class data members should all be private and accessed via the (get_) method.
"""

#import the necessary component modules from the statistics module
from statistics import mean, median, mode

#create the Student class
class Student:
    """Represents a student with a specified name and grade, in which both are private data members"""

    def __init__(self, name, grade):
        """Creates a new student with the name and grade parameters passed in by the user and
        ensures they are private"""
        self._name = name
        self._grade = grade

    #create the retrieval method for a private data member (name)
    def get_name(self):
        """retrieves the name value passed into the class by the user (privately) while keeping
        it distinct from the parameter 'name' """
        return self._name

    #create the retrieval method for a private data member (grade)
    def get_grade(self):
        """retrieves the grade value passed into the class by the user (privately), while keeping
        it distinct from the parameter 'grade' """
        return self._grade

#create the basic_stats function
def basic_stats(data_list):
    """This function takes a list of different student Class objects in class form, calculates the mean,
    median, and mode of the student's grades, and returns all three calculated values. This is done via the statistics module.
    However, first, the function initializes a list for the class 'student' values to be inputted into, and only uses 'student'
    grades as data in the calculations.

    Parameters:
    data_list : list of all student Classes information

    Returns:
    mean_students : mean of all student grades
    median_students : median of all student grades
    mode_students : mode of all student grades
    """

    #initialize an empty list for grade allocation in the for-loop
    grades = []

    #use a for-loop to allocate the grade object of each 'student' class in the data_list to the list 'grades' for later calculation
    for i in data_list:

        """Comment below in the code line below retrieves the grade data member for each instance 'i' in the list of 
        'Student' classes. The grades.append() part then appends this grade data member to the pre-initialized list 'grades'"""
        #i.get_grade()

        grades.append(i.get_grade())


    #define all 3 calculated variables using the imported statistics modules mean, median, and mode
    #mean() calculates the mean of the list 'grades', median() calculates the median of the list 'grades',
    #and mode() calculates the mode of the list 'grades'. Then these values are assigned to 3 different variables to be returned.
    mean_students = mean(grades)
    median_students = median(grades)
    mode_students = mode(grades)

    return mean_students, median_students, mode_students






