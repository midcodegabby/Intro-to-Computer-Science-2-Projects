#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description : This program contains a generator function that generates a sequence of strings. This sequence of
#strings is in the following format: 2, 12, 1112, 3112, 132112, 1113122112, 31131122112, etc. To get the next value
#in the sequence, the function counts how many of each digit are in the previous term.

def count_seq(limit=1000):
    """This generator function takes no arguments and generates a sequence in the following format:
    2, 12, 1112, 3112, 132112, 1113122112, 31131122112, etc. To get the next value in the sequence, the function
    counts how many of each digit are in the previous term. The yielded sequence is a sequence of strings and not
    integers."""

    #create first term in the sequence
    num = '2'

    #initalize an empty string to hold the next term
    new_num = ''

    #initialize number counters and iterator
    val_1 = 0
    val_2 = 0
    val_3 = 0
    index = 0

    #create if statement for case where the number is the first term in the sequence
    if num == '2':

        num = '1' + num
        yield num

    else:

        while index + 1 != len(num):

            if num[index] == '1':
                val_1 += 1

                if index + 1 != len(num):
                    index += 1

                if index + 1 == len(num) or num[index] != '1':
                    new_num += str(val_1) + '1'
                    val_1 = 0

            if num[index] == '2':
                val_2 += 1

                if index + 1 != len(num):
                    index += 1

                if index + 1 == len(num) or num[index] != '2':
                    new_num += str(val_2) + '2'
                    val_2 = 0

            if num[index] == '3':
                val_3 += 1

                if index + 1 != len(num):
                    index += 1

                if index + 1 == len(num) or num[index] != '3':
                    new_num += str(val_3) + '3'
                    val_3 = 0

        yield new_num





