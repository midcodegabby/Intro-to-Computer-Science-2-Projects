#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description : This program contains a function is_subsequence that takes as parameter two strings and returns True
#if the first string is a subsequence of the second string and False otherwise. A subsequence is defined as removing
#zero or more letters from a string (while not changing its order) to turn into another string, the subsequent string.

def is_subsequence(str1, str2, pos=0):
    """This recursive function takes two strings and returns True if the first string is a subsequence of the
    second string but False otherwise. The pos default argument tracks the position in string 1."""

    #define base case
    if pos == len(str1):
        return True

    #if statement for case for when the strings are equivalent, saving memory
    if str1 == str2:
        return True

    #if statement filters out letters that are not in the second string per recursion
    if str1[pos] in str2:

        #define the slice to be used in the next recursion
        slice = str2.index(str1[pos])
        return is_subsequence(str1, str2[slice:], pos+1) #recursive step, moving on to the next letter to be checked

    else:
        return False
