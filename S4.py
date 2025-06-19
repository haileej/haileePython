import random
# the above line tells Python that we want to
# import and use the random module.

intSecretNumber = random.randint(1,10)
# The line above uses the random module's randint (random integer)
# function to generate a random int between 1 and 10.
# The random number is assigned to the variable "intSecretNumber"

intUserGuess = int(input("Guess a number between 1 and 10: "))
# this line of code asks the user to input a number between 1 and 10,
# converts their input string to an int,
# and then assigns it to "intUSerGuess".

if intUserGuess == intSecretNumber:
    print(f"You guessed the correct number: {intSecretNumber}")
else:
    print(f"Sorry you were incorrect. The correct number was {intSecretNumber}")