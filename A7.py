# Hailee Julius
# Assignment 7
# June 20, 2025

'''nested dictionaries and custom functions to create an employee
database program that allows you to add and remove employee records'''

#creating the default nested dictionary with some employees in it already
dictEmployeeDataBase = {
    #including name, salary, and position
    "Employee 1" : {"keyName" : "Bob" , "keySalary" : 70000.0 , "keyPosition": "Manager"},
    "Employee 2" : {"keyName" : "John" , "keySalary" : 50000.0 , "keyPosition": "Staff"},
    "Employee 3" : {"keyName" : "Jenna", "keySalary" : 100000.0 , "keyPosition": "Regional Manager"}
}

#Now I am going to make the function for adding a new employee
def fct_add_employee(dictionary):

    #at first I didn't think to just have the user type in the ID number, and I was trying to do it within the function, but that got kinda confusing, so i decided to let the user do it
    new_employee_id = input("Please type in the new employee's ID number: ").strip()   #just asking for the number, then i will add it to the string "Employee "

    #asking for the employee name
    #used .title() here so if they game first and last name then they would be capitalized
    new_name = input("Please type in the employee's name: ").strip().title()

    #using a while true loop here (i'm using so many in this class which is interesting)
    #using this loop to make sure they input a valid number for the salary, and also remove a dollar sign or comma which are likey to be put
    while True:
        # inputting
        str_new_salary = input("Please type the employee's salary: ").strip()
        #taking off the comma if there is one
        if "," in str_new_salary:
            str_new_salary = str_new_salary.replace(",", "")
        #taking off the dollar sign if there is one
        if "$" in str_new_salary:
            str_new_salary = str_new_salary.replace("$", "")
        #taking off the decimal if there is one
        new_salary_no_decimal = str_new_salary.replace(".", "", 1)
        #checking if it's numeric
        if new_salary_no_decimal.isnumeric() == True:
            new_salary = float(str_new_salary)
            break #breaking the loop if the input is numeric
        #if it isn't numeric, then printing that it isn't and then the loop will restart
        else:
            print("You did not type in an acceptable value, please retry.")
            print()

    # asking the user for the position of the new employee
    new_position = input("Please type in the employee's position/title: ").strip().title()

    # creating a temporary dictionary that i can put in the overall nested dictionary database
    new_dict = {"keyName": new_name, "keySalary": new_salary, "keyPosition": new_position}

    # putting the temporary dictionary in the overall one
    dictionary[f"Employee {new_employee_id}"] = new_dict
    # printing to the user that the new employee was added
    print(f"{new_name} was added to the database.")
    print()




# creating a function to remove and employee
# this was the hardest part for me because i decided to do it based on the employee's name
def fct_remove_employee(dictionary):
    # get the name of the employee they want to remove
    employee_to_remove = input("What is the name of the employee you would like to remove: ").strip().title()
    # get a list of the employee numbers by using .keys() to get the keys of the dictionary
    list_employee_number = list(dictionary.keys())
    #creating a variable to track if the employee has been found in the database
    found = False

    #infinite while loop to be broken by "break"
    while True:

        #for loop that loops through each employee number each pass
        for employees in list_employee_number:
            #if the employee name that the user entered is the same as the employee name associated with the employee number for this loop pass
            if employee_to_remove == dictionary[employees]["keyName"]:
                # using .pop() to remove the employee's sub dictionary and put it in a variable
                dict_removed_employee = dictionary.pop(employees)
                # printing the name of the employee that was removed so that the user knows
                print(f"{dict_removed_employee["keyName"]} was removed.")
                print()
                #changing that found variable to true
                found = True
            #if the employee they want removed wasnt removed wasn't in this pass of the loop, continue to the next pass
            else:
                continue
        #if the employee was found after the for loop looped all of the way through, we break the loop
        if found == True:
            break
        #if the employee wasn't found, we print that the employee wasn't found in the database and break the loop
        else:
            print("Unable to find that employee. Please try again or stop.")
            print()
            break

#defining the function that shows all of the employees in the database
def funct_see_data(dictionary):
    print("Here is your data base: ")
    #for each key in the database, loop through the loop
    for key in dictEmployeeDataBase:
        # getting the name of the employee in a variable
        name = dictionary[key]["keyName"]
        # getting the salary
        salary = dictionary[key]["keySalary"]
        #getting the position
        position = dictionary[key]["keyPosition"]
        #printing all of the datapoints we just acquired in a line, and doing that for each employee
        print(10*" "+f"{key}: {name}    Salary: {salary}    Position: {position}")
    print()




################################ Now we get to the real code #########################################


# print(dictEmployeeDataBase["Employee 1"]["keyName"])

# infinite loop until we loop
while True:

    #run the function that shows all of the data
    funct_see_data(dictEmployeeDataBase)

    #ask the user what they want to do
    strAddOrRem = input('''Would you like to add or remove and employee? 
            1. Add an Employee
            2. Remove an Employee
            3. End Session
Type your answer: ''').strip().lower()

    # if statements for what the user chose that they wanted to do
    if strAddOrRem == "remove" or strAddOrRem == "2" or strAddOrRem == "r" or strAddOrRem == "2.":
        #if they want to remove an employee we run the remove function
        fct_remove_employee(dictEmployeeDataBase)
    elif strAddOrRem == "add" or strAddOrRem == "1" or strAddOrRem == "a" or strAddOrRem == "1.":
        #if they want to add we run the add function
        fct_add_employee(dictEmployeeDataBase)
    elif strAddOrRem == "3" or strAddOrRem == "3." or strAddOrRem == "end":
        # if they chose to end, we ask for confirmation that they want to end
        strContinue = input('Do you want to end? : ').strip().lower()
        if strContinue == "no" or strContinue =="n":
            #if they don't want to end, it restarts the while loop
            print()
        if strContinue =="yes" or strContinue == "y" or strContinue == "end":
            #if they don't want to continue, the loop breaks
            break

