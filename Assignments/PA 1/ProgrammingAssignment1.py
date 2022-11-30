#-------------------------------------------------------------------------------
# Name: Christopher Slavitt
# Assignment 1
# Due Date: 9/6/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Blackboard, Zybooks, Internet for mathematic formulas and temporal conversions
#-------------------------------------------------------------------------------
# Comments and assumptions: These enough comments for ya?
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------


pi = 3.14159 #Defines pi for all later functions

def sec_to_time(seconds): #Defines function that converts total seconds to an output string with hours, minutes, and seconds
    hours = int(seconds // 3600) #Divides seconds into hours, discarding any remainder
    minutes = int((seconds % 3600) // 60) #Takes the remainder from hours and divides it into minutes, discarding the remaining seconds
    seconds = int((seconds % 3600) % 60) #Stores the remainder from minutes
    new_time = str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's' #Forms the variables into a cohesive string
    return new_time #returns the created variable back into the print line that called the function

def angles_from_12(seconds): #Defines a function that finds the degrees and radians of each hand given total seconds.
    hours = seconds / 3600 #Divides seconds into hours, keeping the remainder
    minutes = (seconds % 3600) / 60 #Divides the seconds into minutes, keeping the remainder
    seconds = (seconds % 3600) % 60 #Stores seconds, after being divided into hours and minutes
    hour_hand_deg = hours * 30 #Each hour notch on the clock is 30 degrees. This expression translates the hours to the exact number of degrees on the clock the hand is positioned at
    minute_hand_deg = minutes * 6 #Each minute notch on the clock is 6 degrees. This expression translates the minutes to the exact number of degrees on the clock the hand is positioned at
    second_hand_deg = seconds * 6 #Each second notch on the clock is 6 degrees. This expression translates the minutes to the exact number of degrees on the clock the hand is positioned at
    hour_hand_rad = hour_hand_deg * (pi/180) #Translates the hour hand's position from degrees to radians
    minute_hand_rad = minute_hand_deg * (pi/180) #Translates the minute hand's position from degrees to radians
    second_hand_rad = second_hand_deg * (pi/180) #Translates the second hand's position from degrees to radians
    total_angles = str(round(hour_hand_deg, 5)) + ' ' + str(round(minute_hand_deg, 5)) + ' ' + str(round(second_hand_deg)) + ' degrees or ' + str(round(hour_hand_rad, 5)) + ' ' + str(round(minute_hand_rad, 5)) + ' ' + str(round(second_hand_rad, 5)) + ' radians' #Rounds every value to the fifth decimal point, changes their types to a string, and structures them into an appropriate string
    return total_angles #returns  the created variable back into the print line that called the function

def hand_angles(seconds): #Defines a function that determines the angle in degrees and radians between the hour and minute hands
    hours = seconds / 3600 #Divides seconds into hours, keeping the remainder
    minutes = (seconds % 3600) / 60 #Divides the seconds into minutes, keeping the remainder
    hour_hand_deg = hours * 30 #Each hour notch on the clock is 30 degrees. This expression translates the hours to the exact number of degrees on the clock the hand is positioned at
    minute_hand_deg = minutes * 6 #Each minute notch on the clock is 6 degrees. This expression translates the minutes to the exact number of degrees on the clock the hand is positioned at
    hand_diff_deg = 360 - abs(hour_hand_deg - minute_hand_deg) #Defines a variable with an expression for if the absolute value of the angle between the hour and minute hands are smaller than the rest of the clock
    hand_diff_deg_alt = abs(hour_hand_deg - minute_hand_deg) #Defines a variable with an expression for if the absolute value of the angle between the hour and minute hands are larger than the rest of the clock
    hand_diff_deg_list = [hand_diff_deg, hand_diff_deg_alt] #Places both the hand difference variables into a list for future use
    hand_diff_deg_min = min(hand_diff_deg_list) #Chooses from the hand difference list the smallest value, which is equivalent to the smallest angle between the two hands.
    hand_diff_rad = hand_diff_deg_min * (pi/180) #Translates the hand difference to radians

    rounded_deg = round(hand_diff_deg_min, 5) #Rounds the smallest degree angle between the hour and minute hands to the fifth decimal place.
    rounded_rad = round(hand_diff_rad, 5) #Rounds the smallest radian angle between the hour and minute hands to the fifth decimal place.
    return str(rounded_deg) + ' degrees or ' + str(rounded_rad) + ' radians' #Forms the variables into a cohesive string and returns the string to the print line that called the function

def clock_slice(seconds, diameter): #Defines a function that determines the "slice" of a clock based off of its diameter in both inches and meters
    radius_inch = diameter / 2 #Takes the inputted diameter and converts it to the radius in inches
    radius_meter = (diameter * 0.0254) / 2 #Takes the inputted diameter and converts it to the radius in meters
    hours = seconds / 3600 #Divides seconds into hours, keeping the remainder
    minutes = (seconds % 3600) / 60 #Divides the seconds into minutes, keeping the remainder
    hour_hand_deg = hours * 30 #Each hour notch on the clock is 30 degrees. This expression translates the hours to the exact number of degrees on the clock the hand is positioned at
    minute_hand_deg = minutes * 6 #Each minute notch on the clock is 6 degrees. This expression translates the minutes to the exact number of degrees on the clock the hand is positioned at
    hand_diff_deg = 360 - abs(hour_hand_deg - minute_hand_deg) #Defines a variable with an expression for if the absolute value of the angle between the hour and minute hands are smaller than the rest of the clock
    hand_diff_deg_alt = abs(hour_hand_deg - minute_hand_deg) #Defines a variable with an expression for if the absolute value of the angle between the hour and minute hands are larger than the rest of the clock
    hand_diff_deg_list = [hand_diff_deg, hand_diff_deg_alt] #Places both the hand difference variables into a list for future use
    hand_diff_deg_min = min(hand_diff_deg_list) #Chooses from the hand difference list the smallest value, which is equivalent to the smallest angle between the two hands.

    sect_area_inches = round((hand_diff_deg_min / 360) * pi * (radius_inch ** 2), 5) #Uses the smallest hand difference in degrees to calculate the area of the sector created, and rounds to the fifth decimal place
    sect_area_meters = round((hand_diff_deg_min / 360) * pi * (radius_meter ** 2), 5) #Uses the smallest hand difference in radians to calculate the area of the sector created, and rounds to the fifth decimal place
    return str(sect_area_inches) + ' sq. inches or ' + str(sect_area_meters) + ' sq. meters' #Forms the variables into a cohesive string and returns the string to the print line that called the function

def new_angle(seconds, diameter):
    return 'FIXME: Yo numbnuts! You gotta finish defining the function here!'


print('Welcome to CS 112')
name = input('What\'s your name? ')
total_sec = float(input('What is the time in seconds? '))
print('The time is', sec_to_time(total_sec))
print('The angles of the three hands are', angles_from_12(total_sec))
print('The angle between the hour hand and the minutes hand is', hand_angles(total_sec))
first_diameter = float(input('What is the diameter of the clock in inches? '))
print('The area of the slice between the hour hand and the minutes hand is', clock_slice(total_sec, first_diameter))
second_diameter = float(input('What is the new diameter of the clock in inches? '))
print('The new angle between the hour hand and the minutes hand must be', new_angle(total_sec, second_diameter))
print('Have a good day', name + '!')
