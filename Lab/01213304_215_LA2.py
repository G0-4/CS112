#Christopher Slavitt
#G:012213304
#Objective is to provide the volume of a four layer cake.

pi = 3.14159
radius1 = float(input('Radius of bottom layer in meters: '))
height1 = float(input('Height of bottom layer in meters: '))
volume1 = pi * (radius1 ** 2) * height1

radius2 = float(input('Radius of second layer in meters: '))
height2 = float(input('Height of second layer in meters: '))
volume2 = pi * (radius2 ** 2) * height2

radius3 = float(input('Radius of third layer in meters: '))
height3 = float(input('Height of third layer in meters: '))
volume3 = pi * (radius3 ** 2) * height3

radius4 = float(input('Radius of fourth layer in meters: '))
height4 = float(input('Height of fourth layer in meters: '))
volume4 = pi * (radius4 ** 2) * height4

print('The volume of the entire cake in square meters is:', volume1 + volume2 + volume3 + volume4)