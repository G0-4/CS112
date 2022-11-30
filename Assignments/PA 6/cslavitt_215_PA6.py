#-------------------------------------------------------------------------------
# Name: Christopher Slavitt
# Assignment 6
# Due Date: 10/11/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Blackboard, Zybooks
#-------------------------------------------------------------------------------
# Comments and assumptions: None
#-------------------------------------------------------------------------------

def mashup(lst):
    mystring = '' 
    mylist = []
    mylist2 = []
    value = 0
    for num in range(0, len(lst), 2): #cycles through indexes 0 to the end of the list, increasing by two
        if lst[num + 1] == '': #skips on an empty string
            pass
        elif lst[num] > len(lst[num + 1]): #skips on a number larger than the length of its next string
            pass
        else:
            mylist += lst[num + 1] #adds every character from the string into a list
            for character in range(0, lst[num]): #appends the values into a list
                mylist2.append(mylist[value])
                value += 1
        
            value = 0 #resets value of value
            mylist = [] #resets mylist to empty

    for element in mylist2: #Adds each element in mylist2 to a string
        mystring += element
        
    return mystring #returns final string
    
def expand(numbers, amount):
    spacer = 0
    spacer_count = 0
    index_count = 1
    for index in range(len(numbers)): #loops through each value of the range of "numbers"
        while spacer_count < amount: #Increases the number of spacers if less than the given "amount"
            numbers.insert(index + index_count, spacer)
            spacer_count += 1
            index_count += 1
        spacer_count = 0 #resets spacer count to be increased in the next loop
        
    for num in range(amount): #Adds the initial spacers
        numbers.insert(0, spacer)

def squarify(matrix):
    newlist1 = []
    num1 = 0

    while num1 < len(matrix):  #while loop to append the values into "newlist1"
        newlist1.append(matrix[num1]) 
        num1 += 1
    for lists in newlist1: #loops for each list in "newlist1"
        if len(lists) > len(newlist1): #deletes the end value if there are more individual values than number of lists
            del lists[-1:]
        if len(newlist1) > len(lists): #deletes the end list if there are more lists than number of individual values
            del newlist1[-1:]

    return newlist1

def apply(mask,matrix):
    matrixlist_counter = 0 #Empty variable for use in while loop
    matrixvalue_counter = 0 #Empty variable for use in while loop
    masklist = -1

    while matrixlist_counter < len(matrix): #Loops until "matrixlist_counter" value is no longer less than the length of "matrix"
        masklist += 1 #Increases "masklist" value to move to the next list in mask
        masklist %= 2 #Since "mask" only has two lists, modulates by 2 to keep "masklist" under the index limit
        maskvalue = -1
        while matrixvalue_counter < len(matrix[matrixlist_counter]): #Loops until "matrixvalue_counter" is no longer less than the length of values of the matrix list
            maskvalue += 1 #Increases "maskvalue" value to move to the next value in the mask list
            maskvalue %= 2 #Since the lists in "mask" only only have two values, modulates by 2 to keep "maskvalue" under the value limit
            matrix[matrixlist_counter][matrixvalue_counter] += mask[masklist][maskvalue] #Adds the mask list value to the matrix list value
            matrixvalue_counter += 1 #Increases "matrixvalue_counter" so loop does not continue indefinitely
        matrixlist_counter += 1 #Increases "matrixlist_counter" so loop does not continue indefinitely
        matrixvalue_counter = 0 #Resets "matrixvalue_counter" so it can be used again and eliminate the need for a new "counter" variable


ls = [[1,2],[3,4]]
apply([[1,1],[1,1]], ls) # nothing is returned!
print(ls) # prints [[2, 3], [4, 5]]
ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
apply([[1,1],[1,1]], ls) # nothing is returned!
print(ls) # prints [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
apply([[1,0],[0,1]], ls) # nothing is returned!
print(ls) # prints [[2, 2, 4], [4, 6, 6], [8, 8, 10], [10, 12, 12]]
