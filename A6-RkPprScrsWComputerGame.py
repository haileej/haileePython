# Hailee Julius
# Assignment 6
# June 18, 2025

#using snake case for functions and their variables and camel case for the actual code

#inporting random library so we can have the computer choice a random choice later
import random

#defining the function that will have the computer choose
def computer_choice():
    #making a list for the computer to choose from
    comp_choice_list = ["rock", "paper", "scissors"]
    #computer randomly chooses an entry from the list
    comp_choice = random.choice(comp_choice_list)
    #printing the computer's choice so the player knows
    print(f"The computer chose {comp_choice}.".rjust(45))
    #returning the computer's choice (either "rock", "paper", or "scissors" will be returned from this function)
    return comp_choice

#defining the function that will have the computer choose
def plr_choice():
    #while loop that continuously runs until there is a break
    while True:
        #getting the user's choice as input
        user_input = input('Please type if you want to play paper, rock, or scissors ("p", "r", or "s"): ').lower().strip()
        #if statements for which options the player typed
        if user_input == "s" or user_input =="scissors":
            #printing their choice back
            print("You chose scissors.".rjust(40))
            #returning their choice as "scissors" (and breaking the while loop)
            return "scissors"
        #else if for the next option of paper
        elif user_input == "p" or user_input =="paper":
            #printing their choice of paper
            print("You chose paper.".rjust(40))
            #returning "paper"
            return "paper"
        #else if for the option of rock
        elif user_input == "r" or user_input == "rock":
            #printing their choice of rock
            print("You chose rock.".rjust(40))
            #returning "rock"
            return "rock"
        #otherwise they didn't input a valid option and the loop will run again
        else:
            #printing that they didn't type a valid option
            print("Invalid input. Please try again.".rjust(50))
            #not returning anything so the loop continues to run


#defining the function that will judge who won
#i have a feeling this will be able to be simplified as we learn more
#defining this function to have two nonoptional parameters (what the user chose and what the computer did)
def judge(choice_of_player, choice_of_computer):
    # if statements for all of the different permutations of choices
    #this part is repetitive but basically returning the winner or tie for each given scenario
    if choice_of_player == "paper" and choice_of_computer == "paper":
        return "tie"
    elif choice_of_player == "rock" and choice_of_computer == "rock":
        return "tie"
    elif choice_of_player == "scissors" and choice_of_computer == "scissors":
        return "tie"
    elif choice_of_player == "paper" and choice_of_computer == "rock":
        return "player wins"
    elif choice_of_player == "paper" and choice_of_computer == "scissors":
        return "computer wins"
    elif choice_of_player == "rock" and choice_of_computer == "paper":
        return "computer wins"
    elif choice_of_player == "rock" and choice_of_computer == "scissors":
        return "player wins"
    elif choice_of_player == "scissors" and choice_of_computer == "rock":
        return "computer wins"
    elif choice_of_player == "scissors" and choice_of_computer == "paper":
        return "player wins"
    else:
        #this line should never run
        #i just put it so that I would know if something very wrong happened, but I don't think anything ever did
        return "something is wrong"


################################# Actual Code (After Defining Functions) ##############################################

#setting two variables for each person's wins to zero
player_wins = 0
computer_wins = 0

#printing the opening Intro
print(" "*10+"#"*50)
print(" "*10+"#"*10 + " "*5 + "ROCK PAPER SCISSORS" +" "*5 +"#"*10)
print(" "*10+"#"*50)
print()

#a while loop that will run until a break or until the code quits
while True:

    # while neither player has two wins (which would mean they have won overall)
    while player_wins <2 and computer_wins < 2:

        #Running each function which will return the players choice here and put that string in PlayerChoice
        PlayerChoice = plr_choice()
        #Running the computer function and will put its choice string in CompChoice variable
        CompChoice = computer_choice()
        #running the judge function which will decide who wins and put the string saying it in the variable Winner
        Winner = judge(PlayerChoice, CompChoice)
        print()

        #Now we have if statements for which person won, or if it was a tie
        if Winner == "player wins":
            #if the player won the round we increment their overall score by 1
            player_wins += 1
            #print that the user won the round
            #the loop will then repeat unless player_wins is 2 or more
            print("You won this round.".rjust(40))
        #if the winner was the computer for the round
        elif Winner == "computer wins":
            #increment the computer win count by 1
            computer_wins += 1
            #print that the computer won the round so that the user knows
            print("The computer won this round.".rjust(45))
        #if there was a tie
        elif Winner == "tie":
            #we don't increment because neither player won, and the loop will repeat another round
            print("You tied with the computer. You will play another round.".rjust(60))

    #Now we are out of the while loop, so someone should have 2 wins
    #if the player has two wins
    if player_wins ==2:
        #we print them a win message
        print()
        print(" " * 9 + "#" * 50)
        print("You won best 2 of 3!!!!!".rjust(45))
        print(" " * 9 + "#" * 50)
    # If the computer has 2 wins
    elif computer_wins == 2:
        #print that the computer won
        print("The computer beat you best 2 of 3.".rjust(52))

    #now I will put a loop that asks the user whether they wish to play again
    while True:
        #asking the user for their input on whether they want to play again
        PlayAgain = input("Would you like to play again? ").lower().strip()
        #if they do want to play again
        if PlayAgain == "yes" or PlayAgain =="y":
            #reset the wins to zero so that the while loop from before will loop again until someone gets to 2 wins
            player_wins = 0
            computer_wins = 0
            #print that they will play another game
            print("Get ready for your new game.")
            print()
            #breaking this while loop (that is just for asking if they want to play again) and then the code will go back to running the biggest umbrella loop
            break
        #if they don't want to play again
        elif PlayAgain =="no" or PlayAgain =="n":
            #print that the code will stop running now
            print("Session ending.")
            #had to use the quit function here because break will just send this back to the start and keep asking if they want to play again
            quit()
        #otherwise they input something invalid and this loop asking if they want to play again will repeat
        else:
            #telling them they typed something invalid
            print("Invalid input. Please try again.")

