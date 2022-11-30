#-------------------------------------------------------------------------------
# Name: ANTHONY HUYNH AND CHRISTOPHER SLAVITT
# LAB Assignment 5
# Due Date: 09/24/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, assignments are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
#This lab assignment will involve the materials covered from all previous lectures.
 
#def multiplication_sum_odd(number_list):
 
#Description:
#For each integer item on a list, this function will compute the sum of all odd numbers
#from 0 (inclusive) to number_list(exclusive). After computing for each integer on the list, the summed-up
#results are then multiplied together, and the resultant product is returned.
 
#For example,
#Consider the list number_list = [4, 7, 11]
#1. The first integer on the example list is 4, so the function will add up all odd numbers from 0 to 4
#(excluding the 4)
#you will get 1 + 3 = 4
 
#2.The second integer is 7, so the output will be 9.
 
#3. The third integer is 11, so the output will be 25.
 
#4. Compute 4 * 9 * 25 = 900
 
#5. Return 900
 
#Note: zero is an even number.
 
#Parameters:
#number_list is a list with numbers in which every number is an integer that is greater than 1.
#You do not need to validate input. Assume the input numbers in the list are all > 1
#NO NEED TO USE INPUT
#Return value is an integer as stated in the desc above.
 
second_list = []
 
def multiplication_sum_odd(number_list):
    for n in number_list:
        for i in range(n):
            if (n / 2) % 2:
                i += 2
            final_variable = i * n
    return final_variable
 
 
test_list = [3, 5, 6, 12, 23, 87]
result = multiplication_sum_odd(test_list)
print(result)