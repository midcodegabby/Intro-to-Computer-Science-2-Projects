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

    #create first term in the sequence and an empty string to reassign to the num var
    num = '2'
    next_num = ''

    #initialize iterator
    index = 0

    #initialize number counters
    val= 0

    l = 0

    #create while loop
    while l < limit:

        #if statement for handling first term of sequence
        if num == '2':

            #create second term
            num = '1' + num

            yield num

        else:

            #while loop to iterate through the number without running out of indices
            while index + 1 != len(num):

                #if statement handles a case where the currently indexed value is the same as the next one
                if num[index] == num[index + 1]:

                    #add one to the counter val
                    val += 1

                    #if statement moves the index forward one if the current index is not the last index
                    if index + 1 != len(num):
                        index += 1

                    #if statement handles a case where the end of the string is reached or the next number in the
                    #string is not equal to the current number
                    if index + 1 == len(num) or num[index] != num[index + 1]:

                        #assign to the next term of the sequence the val (number of times the current number has been
                        #repeated concatenated with the current number
                        next_num += str(val) + num[index]

                        #reset the val to be zero
                        val = 0

                if num[index] != num[index + 1]:

                    #add one to the counter val
                    val += 1

                    #if statement moves the index forward one if the current index is not the last index
                    if index + 1 != len(num):
                        index += 1




    """
    #initalize an empty string to hold the next term
    new_num = ''

    #initialize number counters and iterator
    val_1 = 0
    val_2 = 0
    val_3 = 0
    index = 0
    l = 0

    while l < limit:
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

            num = new_num

            yield num
            l += 1
            """



# create first term in the sequence and an empty string to reassign to the num var
num = '1113122112'
next_num = ''

# initialize iterator
index = 0

# initialize number counters
val = 1

l = 0

# create while loop
while l < 5:

    # while loop to iterate through the number without running out of indices
    while index + 1 != len(num):

        # if statement handles a case where the currently indexed value is the same as the next one
        if num[index] == num[index + 1]:

            # add one to the counter val
            val += 1

            # if statement moves the index forward one if the current index is not the last index
            if index + 1 != len(num):
                index += 1

            # if statement handles a case where the end of the string is reached or the next number in the
            # string is not equal to the current number
            if index + 1 == len(num) or num[index] != num[index + 1]:
                # assign to the next term of the sequence the val (number of times the current number has been
                # repeated concatenated with the current number
                next_num += str(val) + num[index]

                # reset the val to be one
                val = 1

        if num[index] != num[index + 1]:


            #move the index forward one if the current index is not the last index
            if index + 1 != len(num):
                index += 1

            # if statement to handle case where the current index is the last index
            if index + 2 == len(num):
                next_num += str(val) + num[index + 1]

            else:
                next_num += str(val) + num[index]

            # reset the val to be one
            val = 1



    l += 1

    print(next_num)



