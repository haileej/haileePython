#Hailee Julius
# BC Class Assignment 2
# June 10, 2025



# This first line is Bill's text. Don't delete it unless you are making up your own mad libs.

#madlibstext = f"""I would like to say a few {adj1} words about the
#most important invention of the twentieth century. I am not
#referring to {invention1} or even the discovery of {noun1}.
#The most {adj2} invention, in my opinion, is the sneaker.
#If it were not for sneakers, our {bodypart1} would be dirty, cold,
#and {adj3}. Sneakers keep me from skidding if the {noun2} are slippery,
#and when I run, they keep me from stubbing my {noun3}."""

# Write your code below this line:

#Okay so since I am given the text of the mad libs,
#I have to define the variables that are written in the text

#I'm going to include str.strip() to ensure there aren't any weird spaces
# and str.lower() so that capitalizations don't mess up with the formatting of the finalized mad libs

# I need to use input() to get the input from the user
# but I have to use it in my definition of the variables because it returns the input

#Just printing an intro for the user
ready= input('''You are creating a Mad Libs about Sneakers. 
Please type your words after the following prompts. 
Press enter when ready.''')

#just printing a space for formatting reasons
print()

#okay this is defining all of the different words
#im using the same names as is in the given text prompt
adj1 = input("Please type an adjective: ").strip().lower()

invention1 = input("Please type an invention: ").strip().lower()

noun1 = input("Please type a food: ").strip().lower()

adj2 = input("Please type an adjective: ").strip().lower()

bodypart1 =  input("Please type a body part (plural): ").strip().lower()

adj3 = input("Please type an adjective: ").strip().lower()

noun2 = input("Please type a plural noun: ").strip().lower()

noun3 = input("Please type a plural noun: ").strip().lower()

print()
print("Your Mad Lib is now ready!")
print()

# I chose to do f strings method of formatting the string
# thus (as I realized while coding this) I have to define the f string after having defined the placeholder variables which im doing below
 # (it was giving me an error if I had madlibstext defined before the adjs, nouns, etc. were defined)
madlibstext = f"""I would like to say a few {adj1} words about the
most important invention of the twentieth century. I am not
referring to {invention1} or even the discovery of {noun1}.
The most {adj2} invention, in my opinion, is the sneaker.
If it were not for sneakers, our {bodypart1} would be dirty, cold,
and {adj3}. Sneakers keep me from skidding if the {noun2} are slippery,
and when I run, they keep me from stubbing my {noun3}."""

#now i just have to print the f string that now should contain the user given words
print(madlibstext)  #boom it works yay






### Decided I also wanted to try using the .format() way
# so this isn't relevant to my final submission of the assignment, but i wanted to do it to practice both ways and see the differences
'''
madlibstext = """I would like to say a few {adj1} words about the
most important invention of the twentieth century. I am not
referring to {invention1} or even the discovery of {noun1}.
The most {adj2} invention, in my opinion, is the sneaker.
If it were not for sneakers, our {bodypart1} would be dirty, cold,
and {adj3}. Sneakers keep me from skidding if the {noun2} are slippery,
and when I run, they keep me from stubbing my {noun3}."""


print(madlibstext.format(adj1=adj1, invention1=invention1, noun1=noun1, adj2=adj2, bodypart1=bodypart1, adj3=adj3, noun2=noun2, noun3=noun3))

'''
# it worked with this code but I do think the f string method worked more efficiently without having to type out all of those equalities in the print statement
# I used the named placeholder way
