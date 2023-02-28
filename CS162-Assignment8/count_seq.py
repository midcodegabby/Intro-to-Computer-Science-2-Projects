#Author : Gabriel Rodgers
#GitHub Username : trashcoder8
#Date : 2/13/23
#Description : This program contains a generator function that generates a sequence of strings. This sequence of
#strings is in the following format: 2, 12, 1112, 3112, 132112, 1113122112, 31131122112, etc. To get the next value
#in the sequence, the function counts how many of each digit are in the previous term.

def count_seq():
    """This generator function takes no arguments and generates a sequence in the following format:
    2, 12, 1112, 3112, 132112, 1113122112, 31131122112, etc. To get the next value in the sequence, the function
    counts how many of each digit are in the previous term. The yielded sequence is a sequence of strings and not
    integers."""


    num = ''
    next_num = ''

    #initialize iterator and number counter
    index = 0
    val = 1

    l = 0

    #create indefinite while loop
    while l < 30:

        #if statement for first term
        if num == '':

            #create first term and assign it to num, then yield
            num = '2'
            yield num

        #if statement for second term
        elif num == '2':

            #create second term and assign it to num, then yield
            num = '1' + num
            yield num

        else:

            #while loop to iterate through num without raising IndexError
            while index + 1 != len(num):

                #if statement handles a case where the currently indexed value is the same as the next one
                if num[index] == num[index + 1]:

                    #add one to the counter val
                    val += 1

                    #if statement moves the index forward one if the current index is not the last index
                    if index + 1 != len(num):
                        index += 1


                #if statement handles a case where the currently indexed value is not the same as the next one or
                #the currently indexed value is the last value in num
                if num[index] != num[index + 1] or index + 1 == len(num):

                    #assign to the next term of the sequence itself concatenated with the val (number of times the
                    #current number has been repeated) concatenated with the current value indexed
                    next_num += str(val) + num[index]

                    #reset the val to be one
                    val = 1

                    #if statement moves the index up by one if the current index is not the last index in the string
                    if index + 1 != len(num):
                        index +=1

                    #if statement handles a case where the new index from above is the last index in the string
                    if index + 1 == len(num):
                        next_num += str(val) + num[index]



            #assign the next term to the current term, then yield
            num = next_num
            yield num

            #set next_num to be empty string, index to be zero
            next_num = ''
            index = 0

            l +=1


seq = count_seq()
for i in seq:
    print(i)
"""
num = ''
next_num = ''

#initialize iterator and number counter
index = 0
val = 1

l = 0

#create indefinite while loop
while l < 10:
    # if statement for first term
    if num == '':
        # create first term and assign it to num, then yield
        num = '2'
        print(num)

    #if statement for first term
    elif num == '2':

        #create second term and assign it to num
        num = '1' + num

        print(num)

        

    else:

        #while loop to iterate through num without raising IndexError
        while index + 1 != len(num):

            #if statement handles a case where the currently indexed value is the same as the next one
            if num[index] == num[index + 1]:

                #add one to the counter val
                val += 1

                #if statement moves the index forward one if the current index is not the last index
                if index + 1 != len(num):
                    index += 1


            #if statement handles a case where the currently indexed value is not the same as the next one or
            #the currently indexed value is the last value in num
            if num[index] != num[index + 1] or index + 1 == len(num):

                #assign to the next term of the sequence itself concatenated with the val (number of times the
                #current number has been repeated) concatenated with the current value indexed
                next_num += str(val) + num[index]

                #reset the val to be one
                val = 1

                #if statement moves the index up by one if the current index is not the last index in the string
                if index + 1 != len(num):
                    index +=1

                #if statement handles a case where the new index from above is the last index in the string
                if index + 1 == len(num):
                    next_num += str(val) + num[index]



        num = next_num
        print(num)
        index = 0
        next_num = ''
        val = 1

        l +=1
"""