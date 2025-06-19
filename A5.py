#Hailee
#Assignment 5
# June 16, 2025

# start with some $$
fltSavBal = 500.99
fltChkBal = 100.31

# Welcome UI Message
print("#"*80)

#i wasn't really sure where else to use the string.rjust() so i used it here
print("Welcome to the ATM".rjust(49))
print("#"*80)
print()

# create a loop for the program
#this will loop indefinitely, so we need something in the loop that will break it eventually
while (True):

    #Show the menu options
    #i separated these onto different lines so that I could use the .rjust() to make it look nicer
    print("Choose an option: ")
    print("1 - Deposit ".rjust(43))
    print("2 - Withdrawal ".rjust(46))
    print("3 - Check Balance".rjust(48))


    # Ask the user for their choice
    strMenu = input("what do you want to do? ").strip()


    ################################### Deposit ###########################################
    # simple if statement for is they choose the number associated with deposit
    if (strMenu == "1"):   # i kinda don't get why you put the parenthesis around the if condition Professor Moseley?

        #printing their choice back to them and adding .rjust() to make it look nicer
        print("You want to make a deposit.".rjust(53))


        #ask which account
        strDepAcc = input("Which account would you like to deposit into? (Savings or Checking): ").strip().lower()

        ################################### Savings Deposit ###########################################
        # if they wrote savings or s
        if strDepAcc == "savings" or strDepAcc == "s":

            #asking `1
            ''' i want to note that if i wasn't being so thorough as to check all of the 
            user inputs that i would only do this line once, but I want to accept both 
            "savings" and "s" in the if statement so i put this underneath the if statement.
             And because I want to make what the user sees more understandable, i.e. where 
             i'm typing "what do you want to put in your SAVINGS account. Maybe there is a 
             better way, but all of they data validation if pretty much copy paste'''
            strDepAmount = input("Please type how much you would like to deposit into your Savings account: ")
            # data validation part
            # take out decimal if there is one
            strDepAmount_NoDecimal = strDepAmount.replace(".", "", 1)
            # take off dollar sign if there is one
            #if it starts with $
            if strDepAmount.startswith("$") == True:
                #this new variable is equal to the input without the $
                strDepAmount_NoDollar_NoDecimal = strDepAmount_NoDecimal[1:].strip()
                #this line is just for taking off the dollar sign but leaving the decimal if there is one
                #will be for doing calculations
                strDepAmount_NoDollar = strDepAmount[1:].strip()
            #if there isn't a dollar sign
            else:
                #doing the same things above, just in the case there isn't a dollar sign, so we don't have to take off the first character
                strDepAmount_NoDollar_NoDecimal = strDepAmount_NoDecimal
                strDepAmount_NoDollar = strDepAmount

            #this is where we actually check that the user put in a valid number amount to deposit
            #if the input without dollar sign and without decimal is not numeric
            if strDepAmount_NoDollar_NoDecimal.isnumeric() == False:
                #print that they didn't type in a valid deposit amount
                #from here the code will go to the bottom of the while loop where it asks if they want to do another transaction
                print("You typed in an invalid dollar amount. Restarting now.".rjust(67))
                print()

            #otherwise it is a valid number
            else:
                #and we do the calculations
                #changing the user input string (without $) into a float so we can calculate
                fltDepAmount = float(strDepAmount_NoDollar)
                #adding it to the previous balance and redifining that as our new balance
                fltSavBal = fltSavBal + fltDepAmount
                #changing it back into a string that is rounded to the nearest hundredth so that we can print it to the user
                strfltSavBal = str(round(fltSavBal,2))
                #printing the new balance to the user of the savings account
                print(f"Your new savings account balance is ${strfltSavBal}.".rjust(63))

        ################################### Checking Deposit ##########################################
        #everything kinda repeats except its checking instead of savings now
        #if they type checking instead
        elif strDepAcc == "checking" or strDepAcc == "c":

            #ask how much they want to deposit
            strDepAmount = input("Please type how much you would like to deposit into your Checking account: ")
            #data validation part
            #take out decimal if there is one
            strDepAmount_NoDecimal = strDepAmount.replace(".", "", 1)
            #take off dollar sign if there is one
            if strDepAmount.startswith("$") == True:
                #remocing the first character
                strDepAmount_NoDollar_NoDecimal = strDepAmount_NoDecimal[1:].strip()
                #also making a string with the decimal but without the dollar sign so we can calculate later
                strDepAmount_NoDollar = strDepAmount[1:].strip()
            #if there isn't a dollar sign
            else:
                #this part seems redundant but we do it so that we can write out the equation later that will work regardless of if the user used a dollar sign or not
                strDepAmount_NoDollar_NoDecimal = strDepAmount_NoDecimal
                strDepAmount_NoDollar = strDepAmount

            #where we actually check that the user gave a valid deposit input
            if strDepAmount_NoDollar_NoDecimal.isnumeric() == False:
                    #if they didn't we tell them as such
                    print("You typed in an invalid dollar amount. Restarting now.".rjust(67))
                    print()
            # if they gave a valid value
            else:
                #change the input with the decimal, but without the dollar sign to a float so that we can do numerical calculations
                fltDepAmount = float(strDepAmount_NoDollar)
                #add the deposit amount the the previous balance and redefine the previous balance as that sum
                fltChkBal = fltChkBal + fltDepAmount
                #change the new balance back into a string so we can print
                #and round it to two decimal spaces as is typical with a dollar amount
                strDepAmount = str(round(fltChkBal, 2))
                #print the user their new checking account balance
                print(f"Your new Checking account balance is ${strDepAmount}.".rjust(63))

        #if they did not type in savings or checking
        else:
            #tell them they messed up
            #this will send them to the bottom of the loop and as them if they want to do another transaction after printing the following two lines
            print("You did not type in a correct account. Restarting now.".rjust(60))
            print()




    ################################### Withdrawal ###########################################
    #if the user typed in 2 in the initial menu
    elif (strMenu == "2"):
        #print to them that they chose to withdraw
        print("You want to make a withdrawal.".rjust(53))

        #ask them which account the want to withdraw from
        strWithAcc = input("Which account would you like to withdraw from? (Savings or Checking): ").strip().lower()

        ################################### Savings Withdrawal ###########################################
        #if they indicated they want money from their savings
        if strWithAcc == "savings" or strWithAcc == "s":
            #ask how much from their savings they want
            strWithAmount = input("Please type how much you would like to withdraw from your Savings account: ")
            # data validation part
            # take out decimal if there is one
            strWithAmount_NoDecimal = strWithAmount.replace(".", "", 1)
            # take off dollar sign if there is one
            #pretty much the same stuff here
            #can wait for functions :)
            if strWithAmount.startswith("$") == True:
                strWithAmount_NoDollar_NoDecimal = strWithAmount_NoDecimal[1:].strip()
                strWithAmount_NoDollar = strWithAmount[1:].strip()
            else:
                strWithAmount_NoDollar_NoDecimal = strWithAmount_NoDecimal
                strWithAmount_NoDollar = strWithAmount

            #checking if the input string (without a potential dollar sign or decimal) is numeric
            if strWithAmount_NoDollar_NoDecimal.isnumeric() == False:
                #telling the user they messed up if they didn't input a numeric value
                print("You typed in an invalid dollar amount. Restarting now.".rjust(67))
                print()
            else:
            #if they did enter a valid numeric value
                #making their input into a float to do calculations AND numerical comparisons with
                fltWithAmount = float(strWithAmount_NoDollar)

                # Extra step where we have to make sure our balance doesn't go below zero
                # this is an extra step i have to do for he case that we're withdrawing
                # we have to make sure the user doesn't withdraw more than is in their account
                if fltWithAmount > fltSavBal:
                    #if they typed too high of a number tell them they messed up
                    print("The number amount you typed is too high. Restarting now.".rjust(67))
                    print()

                else:
                # they typed in a low enough number

                    #subtract the withdrawal amount from the balance of their savings
                    fltSavBal = fltSavBal - fltWithAmount
                    #change the savings balance back to a string and round it so we can print
                    strSavBal = str(round(fltSavBal,2))
                    #printing the new balance
                    print(f"Your new Savings balance is ${strSavBal}.".rjust(63))

        ################################### Checking Withdrawal ###########################################
        elif strWithAcc == "checking" or strWithAcc == "c":

            #ask the user how much they want from checking
            strWithAmount = input("Please type how much you would like to withdraw from your Checking account: ")
            # data validation part
            # take out decimal if there is one
            strWithAmount_NoDecimal = strWithAmount.replace(".", "", 1)
            # checking if it starts with a dollar sign
            if strWithAmount.startswith("$") == True:
                #taking of the dollar sign if its there
                strWithAmount_NoDollar_NoDecimal = strWithAmount_NoDecimal[1:].strip()
                strWithAmount_NoDollar = strWithAmount[1:].strip()
            #if there's not a dollar sign, still using the same variables in the previous statement so we can put it into the lines later
            else:
                strWithAmount_NoDollar_NoDecimal = strWithAmount_NoDecimal
                strWithAmount_NoDollar = strWithAmount

            #if the value isn't numeric, telling the user they input a wrong value
            if strWithAmount_NoDollar_NoDecimal.isnumeric() == False:
                print("You typed in an invalid dollar amount. Restarting now.".rjust(67))
                print()
            # otherwise they gave a valid number
            else:
                #changing it to a float so we can do calculations
                fltWithAmount = float(strWithAmount_NoDollar)
                # Extra step where we have to make sure our balance doesn't go below zero
                if fltWithAmount > fltChkBal:
                    #if they typed in too high of a withdrawal amount
                    print("The number amount you typed is too high. Restarting now.".rjust(67))
                    print()

                #if the gave a small enough amount to be withdrawn
                else:
                    #doing the calculation for the new balance of the checking account
                    fltChkBal = fltChkBal - fltWithAmount
                    #rounding and changing new balance to string so it can be printed
                    strChkBal = str(round(fltChkBal,2))
                    #printing using an f string
                    print(f"Your new Checking balance is ${strChkBal}".rjust(63))

        #if they didn't type in checking or savings
        else:
            #telling them they messed up and it will go to the end of the loop
            print("You did not type in a correct account. Restarting now.".rjust(70))
            print()




    ################################### Check Balance ###########################################
    #this is the easiest one, we just have to get one input
    elif (strMenu == "3"):
        #print to them what they chose
        print("You want to check a balance.")

        #ask them which account they want to know the balance of and taking it as input
        strBalAcc = input("Which account would you like to check the balance of? (Savings or Checking): ").strip().lower()

        ################################### Savings Check ###########################################
        #if they chose savings
        if strBalAcc == "savings" or strBalAcc == "s":
            #round the savings and change it to a string
            strSavBal = str(round(fltSavBal, 2))
            #print the balance using an f string
            print(f"The balance of your savings account is ${strSavBal}.".rjust(65))

        ################################### Checking Check ###########################################
        #otherwise if they chose chekcing
        elif strBalAcc == "checking" or strBalAcc == "c":
            #round and change to string
            strChkBal = str(round(fltChkBal, 2))
            #print the balance
            print(f"The balance of you checking account is ${strChkBal}.".rjust(65))
        #inclunclusive which account
        else:
            #print that they didn;t type in a valid account
            print("You did not type in a correct account. Restarting now.")
            print()


    #if they didn't type in a value number in the first menu
    else:
        #print that they didn't choose a valid number
        print ("Sorry - that's not a valid choice".rjust(55))

    #this is where we ask if the user wants to repeat the loop and if not we break
    print("")
    #get their answer as input
    strMore = input("Would you like another transaction? (yes or no) ").strip()

    #if they didn't type yes or y
    if strMore.lower() != "y" and strMore.lower() != "yes":
        #we break the loop and the program is basically done
        break
    #otherwise the loop begins again

#the loop has been broken and i put this to tell the user it's over
print("Your session has now ended.".rjust(52))