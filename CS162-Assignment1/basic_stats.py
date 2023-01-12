"""
Author: Gabriel Rodgers
GitHub Username: trashcoder8
Date: 1/11/23
Description:
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

    #question... does this method satisfy the requirement of initializing the data members?
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
#def basic_stats():




