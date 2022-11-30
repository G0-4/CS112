#-------------------------------------------------------------------------------
# Name: Christopher Slavitt, Marcus Tate, Sanjeet Parajuli
# Lab 4
# Due Date: 9/17/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------

def cash_back(total, category):
    cashback = 0
    if total > 1000:
        cashback = total * .05
    elif category == 'online shopping':
        cashback = total * .03
    elif category == 'groceries' or category == 'dining':
        cashback = total * .02
    else:
        cashback = total * .01
    return cashback

