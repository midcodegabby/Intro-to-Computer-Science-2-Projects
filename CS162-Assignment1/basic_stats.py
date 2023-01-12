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

    #generate index values for iteration
    idx = range(len(data_list))

    #subtract 1 from idx to find the number of elements in the data_list
    n = len(data_list)

    #initialize a list with the same number of elements as the data_list
    b_list = [None]*n

    #use a for-loop to allocate the grade object of each 'student' class in the data_list to the list for later calculation
    for i in range(len(data_list)): #or remove the range len part and it gives another error

        b_list[i] = Student.get_grade(i)




    #define all 3 calculated variables using the imported statistics modules mean, median, and mode
    mean_students = mean(b_list)
    median_students = median(b_list)
    mode_students = mode(b_list)

    return mean_students, median_students, mode_students



s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values

print(s1._grade)





