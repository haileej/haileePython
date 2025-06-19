#Hailee
#Assignment 4
# June 12, 2025


# Show the UI
print("#" * 80)
print("#" * 9, " " * 60, "#"*9)
print("#" * 9, "Celsius/Fahrenheit Calculator".center(60), "#" * 9)
print("#" * 9, " " * 60, "#"*9)
print("#" * 80)

# Welcome the user
print('''Hello! This is a conversion calculator for temperature 
in Celsius to Fahrenheit or Fahrenheit to Celsius.''')

#just printing an empty space for readability
print()

#asking the user if they want the final units to be in F or C
strDecision = input('Please type the units you wish to convert your temperature to ("Celsius" or "Fahrenheit"): ').strip().lower()

#empty space
print()



# if the user typed that they want the final units to be in C
#im using an "or" here ("shhhh") because it's easier for testing, and i just also feel like the user might just type the letter
if strDecision == "celsius" or strDecision =="c":

    #have to get the user to type in the starting temp in F
    #this will be a STRING
    #also i'm stripping it just in case of spaces
    strStartingTemp = input("Please enter your starting temperature (in Fahrenheit): ").strip()


    #okay so i want to test that they entered an actual number
    #first I have to account for if they typed a decimal number so that i can verify if they put an actual number
    #this line will remove any decimal, if present, and put that altered string into strStartingTemp_NoDecimal
    strStartingTemp_NoDecimal = strStartingTemp.replace(".","", 1)

    #now this if statement will remove a dash if the number was negative
    #if the string starts with dash
    if strStartingTemp.startswith("-") == True:

         #the string is redefined as the same string minus the first character
         strStartingTemp_NoNegative_NoDecimal = strStartingTemp_NoDecimal[1:]

    #otherwise (if it isn't negative) we define it as this new variable just cause we need to have this same name from either of these two cases so that we can put it in the next if statement to test if its numeric
    else:

        #just defining it so it can be used in the next if statement whether it is neg (or in this case) isnt
        strStartingTemp_NoNegative_NoDecimal = strStartingTemp_NoDecimal


    #now this if statement will print to restart if the entry (without a decimal or negative) isn't numeric
    if strStartingTemp_NoNegative_NoDecimal.isnumeric() == False:

        #if it isn't numeric, it will tell the user to restart
        print("You typed an invalid number. Please restart and only type a number.")


    #otherwise if the user input IS a usable number, we then do the calculation and print the result for them
    else:


        #just have to convert the string of the user input number to a float before we can do the calculation
        fltStartingTemp = float(strStartingTemp)

        #now we do the calculation F to C
        fltCelsius = (fltStartingTemp - 32)*(5/9)

        #just spacing
        print()


        #and finally we do an f string to print out the final temperature to the user
        print(f"{fltStartingTemp} degrees Fahrenheit is {fltCelsius} degrees Celsius.")
        #now i have to do this all over with the other scenario (but luckily for the way I did it, its basically the same code just with the words switched)





#If the user typed that they want the final units in F
elif strDecision == "fahrenheit" or strDecision =="f":


    #okay asking the user to input their starting temperature
    #stripping it in case of spaces
    strStartingTemp = input("Please enter your starting temperature (in Celsius): ").strip()

    #now to take out the decimal (if there is one) so that I can test if they actually put in a number
    strStartingTemp_NoDecimal = strStartingTemp.replace(".", "", 1)


    #if it is negative
    if strStartingTemp.startswith("-") == True:

        #taking the dash out of the string to test if numeric later
         strStartingTemp_NoNegative_NoDecimal = strStartingTemp_NoDecimal[1:]

    #if not negative, just redefining it so i can put it in the equation
    else:

        #redefining
        strStartingTemp_NoNegative_NoDecimal = strStartingTemp_NoDecimal


    #now this if statement will print to restart if the entry (without a decimal or negative) isn't numeric
    if strStartingTemp_NoNegative_NoDecimal.isnumeric() == False:

        #if it isn't numeric, it will tell the user to restart
        print("You typed an invalid number. Please restart and only type a number.")

    #if we have an acceptable, numeric temp input
    else:

        #change the original input to float so we can do arithmetic
        fltStartingTemp = float(strStartingTemp)

        #the equation for C to F
        fltFahrenheit = ((9/5)*fltStartingTemp)+32

        #spacing
        print()

        #final statement C to F
        print(f"{fltStartingTemp} degrees Celsius is {fltFahrenheit} degrees Fahrenheit.")



#if the user typed in something other than Celsius or Fahrenheit (regardless of starting or ending spaces and capitalizations)
else:
    print("You entered an invalid entry for your desired conversion units. Please restart.")





''' I think if i were to redo this i could make it more efficient if i did the 
testing for the decimal and negative just once if i did it before the first if statement.

I just wanted to have the units in the question when i ask the user for their starting temperature
so that it is less confusing for the user. And the units in the final statement. I can think of ways I 
could've made it more efficient though. I just don't want to change it now, since I already got it to work.
But if i had more time i would.

'''