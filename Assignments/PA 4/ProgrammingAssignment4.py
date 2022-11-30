#-------------------------------------------------------------------------------
# Name: Christopher Slavitt
# Assignment 4
# Due Date: 9/27/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Blackboard, Zybooks
#-------------------------------------------------------------------------------


def sum_divisors(n): #This function grabs every value from 1 to n as value "num". This is then divided together, and as long as the remainder is zero, adds that number to the result variable.
    result = 0
    for num in range(1, n + 1):
        if n % num == 0:
            result += num
    return result

def negative_product(nums): #Takes every number from the "nums" list, and so long as the value is less than 0, multiplies it by the result variable.
    result = 1
    for num in nums:
        if num < 0:
            result *= num
    return result

def heater(fuel, temp): #Runs an if statement for if the temperature is less than 80, calculates the tradeoff of fuel for temperature, and returns the appropriate result.
    result = ''
    if temp < 80: #Skipped if temperature is not less than 80
        while fuel > 0 and temp < 80: #Calculates using fuel for temperature
            fuel -= 1
            temp += 5
    succ = 'success, ' + str(fuel) + ' leftover fuel!' #This string's used twice, so I just added it to a variable to make it easier.
    if temp == 80 and fuel == 0:
        result = 'success, no leftover fuel!'
    elif temp == 80 and fuel != 0 or temp > 80: #Was originally two lines with "temp > 80" being by itself. This lowers the number of lines while keeping the same results the same.
        result = succ
    elif temp <= 80:
        result = 'failure, highest temp is ' + str(temp)
    return result

def analyze(activity, time_period): #Determines the total amount of time and desired activity time. Then calculates the percentage of their quotient.
    result = 0
    total = 0 
    multiplier = 0
    for value in time_period: #Uses a for loop to split up the string, and increases the variable "total" with the corresponding string value.
        if value == 'w':
            total += 20
        elif value == 'f':
            total += 15
        elif value == 'b':
            total += 10
        else:
            total += 60
        if value == activity: #if the condition value is the same as the activity parameter, then the multiplier value is increased by 1
            multiplier += 1
    #For the next set of if statements: Dependent on the "activity" parameter's chosen argument, a value is divided by the total, multiplied by 100 to return the percentage, and then multiplied by the multiplier. The product is then rounded to the hundreds place.
    if activity == 'w':
        result = round((float(20 / total) * 100) * multiplier, 2)
    elif activity == 'f':
        result = round((float(15 / total) * 100) * multiplier, 2)
    elif activity == 'b':
        result = round((float(10 / total) * 100) * multiplier, 2)
    else:
        result = round((float(60 / total) * 100) * multiplier, 2)
    return result

def travel(position, velocity, acceleration): #Manipulates position based off velocity, and manipulates velocity based off acceleration. Continues until position = 0 or 1000. 
    result = 0
    while 0 < position < 1000:
        result +=1 #Each repetition increases the result by 1, which is then returned after the while loop finishes.
        position += velocity
        velocity += acceleration
    return result
