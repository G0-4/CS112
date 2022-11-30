#-------------------------------------------------------------------------------
# Name: Christopher Slavitt
# Assignment 3
# Due Date: 10/4/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Blackboard, Zybooks
#-------------------------------------------------------------------------------
# Comments and assumptions: None
#-------------------------------------------------------------------------------

def replace_contraction(text):
    mystring = '' #Empty string to be assigned values
    character = 0

    while character < len(text): #Combs over each character in string "text", replacing "I'm" with "I am" by using multiple nested if statements to find the contraction
        if text[character] == 'I': 
            if text[character + 1] == '\'':
                if text[character + 2] == 'm':
                    mystring += 'I am'
                    character += 3
                else:
                    mystring += "I'"
                    character += 2
            else: 
                mystring += "I"
                character += 1


        elif text[character] == 'y': #Combs over each character in string "text", replacing "you're" with "you are" by using multiple nested if statements to find the contraction.
            if text[character + 1] == 'o':
                if text[character + 2] == 'u':
                    if text[character + 3] == '\'':
                        if text[character + 4] == 'r':
                            if text[character + 5] == 'e':
                                mystring += 'you are'
                                character += 6
                            else:
                                mystring += 'you\'r'
                                character += 5
                        else:
                            mystring += 'you\''
                            character += 4
                    else:
                        mystring += 'you'
                        character += 3
                else:
                    mystring += 'yo'
                    character += 2
            else:
                mystring += 'y'
                character += 1

        else: #Any other character is immediately added to the empty string.
            mystring += text[character]
            character += 1

    return mystring #Returns the string after all the values are added



def swap_adjacent(numbers): #Swaps every other adjacent value with the one before it
    value = 0 #Value assigned to variable for use as the beginning of the while loop
    while value < len(numbers) - 1: #Combs through every value in the list "numbers", stopping at the end of the list
        x = numbers[value] #Assigns the first value as a variable "x"
        numbers[value] = numbers[value + 1] #That initial value is then changed to its next value in sequence
        numbers[value + 1] = x #The value after the initial value is changed to the vale of "x"
        value += 2 #Value is then increased by two to skip the switched value, and onto the next one in sequence

    return numbers #returns the now editted list "numbers"

def within_1_sd(numbers): #Finds every number 1 standard deviation from the mean, and returns it
    mean = 0 #Empty mean variable to be assigned
    variance = 0 #Empty variance variable to be assigned
    standdev = 0 #Empty standard deviation varible to be assigned
    mylist = [] #Empty list to be appended with desired numbers
    value = 0 #Placeholder variable used to store values
    order = 0
    for num in range(len(numbers)): #Takes every value in the list "numbers" and combines them together into the "value" variable
        value += numbers[num]
        
    mean = value / len(numbers) #Divides the variable "value" by the length of the list, and assigns the quotient as the variable "mean"

    while order < float(len(numbers)) - 1: #Combs through every value in the list "numbers", using variable "order" to signify the first value in the list.
        if numbers[order] > mean: #If the value is larger than the mean, it is subtracted from the mean and squared. The resulting value is added to the variable "variance" and the order increased to bring the next value.
            difference = ((mean - numbers[order]) ** 2)
            variance += difference
            order += 1
        elif numbers[order] < mean: #If the value is smaller than the mean, the mean is subtracted from the value and squared. The resulting value is added to the variable "variance" and the order increased to bring the next value.
            difference = ((numbers[order] - mean) ** 2 )
            variance += difference
            order += 1
        else:
            order += 1

    variance = variance / len(numbers) #Variance is then divided by the number of values in the list.
    standdev = round(float(variance ** (1/2)), 2) #The variance is square rooted, left as a float value, and rounded to the nearest hundredth. The resulting standard deviation is assigned as the value "standdev"

    for num in range(len(numbers)): #Combs through every value in the list "numbers"
        if (numbers[num] <= (mean + standdev)) and (numbers[num] >= mean): #If the value is equal to or less than standard deviation plus mean AND the value is equal to or greater than the mean, it is appended to list "mylist"
            mylist.append(numbers[num])
        elif (numbers[num] >= (mean - standdev)) and (numbers[num] <= mean): #If the value is equal or greater than mean minues standard deviation AND the value is equal to or less than the mean, it is appended to list "mylist"
            mylist.append(numbers[num])
    
    return mylist

def equal_sum(numbers): #Takes a list and determines if the first value is equal to the next two values added together, and the next three values added together, and the next four, and so on
    sum_checker = 0 #Empty variable for use in a for loop
    value = numbers[0] #Variable set to the first value of the list

    for num in range(len(numbers)): #For loop that runs through each index in the list.
        if sum_checker == value: #Sets sum_checker to zero once it equals the first value
            sum_checker = 0
        
        if numbers[num] != value and sum_checker != value: #If the value being checked does not equal the first value AND the sum_checker variable does not equal the first value, the value is added to sum_checker
            sum_checker += numbers[num]
    
    if sum_checker > value or sum_checker < value: #Checks if sum_checker is greater than or less than the first value. If it is, then False is set as the variable "equality"
        equality = False
    else: #Checks if sum_checker equals the first value. If it is, then  True is set as the variable "equality"
        equality = True
    
    return equality #Returns the variable "equality"

        

def is_sequence(numbers): #Function used to determine if a list of numbers is in a sequence regardless of order
    lowestnum = numbers[0] #Sets the lowest number as the first value in the list by default.
    highestnum = numbers[0] #Sets the highest number as the first value in the list by default
    order = 0 #Empty variable for use in a while loop
    order2 = 0 #Empty variable for use in a while loop

    while order != len(numbers): #Loops as long as the order variable does not equal the length of the list, increments by one under every if statement
        if numbers[order] < lowestnum: #If a number in the list is lower than the first value, it is assigned as the "lowestnum". This number is then compared to the next values in the list
            lowestnum = numbers[order]
            order += 1
        elif numbers[order] > highestnum: #If a number in the list is higher than 0, it is assigned as the "highestnum". This number is then compared to the next values in the list.
            highestnum = numbers[order]
            order += 1
        else:
            order += 1

    for _ in numbers: #For loop that runs the later while loop and if statement for the entire string. Resets variable "order2" so I don't have to make new variables every time the while loop starts.
        order2 = 0
        while order2 < len(numbers):  #While loop that runs for each individual number, until the variable "order2" stops being less than the length of the list.
            if numbers[order2] == lowestnum + 1: #If statement to help compare the next value in the list with the variable "lowestnum" plus 1. If the equation is equivalent, the variable's assigned value is changed to that of the value in the list.
                lowestnum = numbers[order2]
            order2 += 1

    if lowestnum == highestnum: #Checks if the variable "lowestnum" is equal to "highestnum", assigns the resulting boolean.
        sequence = True
    else:
        sequence = False

    return(sequence) #Returns the boolean

