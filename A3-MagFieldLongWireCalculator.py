# Hailee Julius
# Assignment 3
# June 10, 2025


'''I am going to pull from my physics degree
and make a calculator for the magnetic field of
a long, straight, current carrying conductor (usually a wire).
This is an application of the Biot-Savart Law in
the approximation that current is traveling in a long (infinite), straight path.

Equation: B = mu * I/ 2 pi r ; where B is the magnetic field magnitude,
mu is the permeability of free space constant (4pi * (10^-7) N/A*m),
I is the current of the wire, and r is the perpendicular
distance from the wire to the point at which you want
 to determine the field magnitude. pi is 3.14159...
'''

#Going to print an intro that tells the user what we're calculating
# I'm going to mention the formula just because that's what I would like to see if I was the user
# (Using convention for the symbols of the variables in the formula)
print('''This code uses the Biot-Savart law to calculate 
the magnitude of the magnetic field a long, straight wire produces 
a perpendicular distance, r, away from the wire.
Equation: B = (mu_naught * I)/ (2 * pi * r)''')

#I just like to have some space separating the text in the terminal so I'm printing an empty line here
print()

# now I'm telling the user that they have to provide the code some of the values to calculate
print('''Please input the needed values when prompted in order to calculate.''')

# another empty line
print()

#okay so i got a little tripped up here at first because I forgot to change the inputted string to float
# so I had to add that float() to surround the input() function because I sillily forgot it would make the number a string
#But anyways this line is where i prompt the user to enter the current of the wire they are curious about
#the value has to be in amperes otherwise I would have to convert it to make the equation work
floatCurrent = float(input("Please input the current of the wire in amperes: "))

#again asking the user for a number which input() makes a string and then using float() to make it a float value so that i cal put it in the equation
floatRadialDistance = float(input('''Please input the perpendicular distance (in meters) from 
the wire at which you wish to know the magnetic field strength: '''))

print()

# writing in values for the constants that are needed for the equation
floatPi = 3.141592653589793  # Unitless

# permeability in free space constant
# gave myself some PEMDAS practice
floatMu = (4 * floatPi)*(10**(-1*7))  # Units: Newtons per Amperes squared

# okay this is the heart of this assignment right here
# this is where i use all of the variables to calculate the desired answer
fltMagField = (floatMu * floatCurrent) / (2*floatPi *floatRadialDistance)     # units of magnetic field are Tesla !!

#now im using a f-string with curly braces so that the string can just add in the calculated mag field magnitude
#i also decided to add in the distance value just to cement in the user's head what that value is for
#cuase i know when i learned this equation I sometimes got confused in thinking that the distance value was the radius of the wire (when it is NOT)
strFinishedStatement = f'''The magnitude of the magnetic field {floatRadialDistance} meters away from 
your straight, long wire is {fltMagField} Tesla.'''

#Now just printing that string which should now contain the solved-for mag field value
print(strFinishedStatement)
