'''
    Project: Simple Bot (TEMPLATE)
    Name: Daniel Tetteh
    Date: 02-02-2026
    Course: CMSC 150 - Section 2
    Program Description:
'''
import random

####### GLOBAL VARIABLES #######

# DYNAMIC
user_name = ""                      # user's name input at the beginning
magic_word_ct = 0                   # number of times magic word is said
unlocked_password = False           # flag for whether or not the user said both passwords

# CONSTANTS
BOT_NAME = "Patrick"                       # your bot's name
EXIT_COMMAND = "goodbye"            # user input command to exit the program
MAGIC_WORD = "Star"                     # magic word to check for in user input
PASSWORD1 = "Bikini"                      # first password to check in user input
PASSWORD2 = "Bottom"                      # second password to check in user input
SECRET_MESSAGE = "Don't work at the Krusty Krab!"                 # message to show if the user unlocked it with both passwords


# Additional variables below (if needed) #




####### AI LOOP #######


# ask for the user's name and save it
# YOUR CODE HERE #

user_name = input("What's your name? ")

# enter user input loop
while True:
    # ask for user input
    user_input = input("> ")

    # check if the user wants to exit with the exit command
    # 'break' comes out of the while loop. the AI will continue infinitely until the command is said
    if user_input.lower() == EXIT_COMMAND:
        break

    # WRITE YOUR 9 CONDITIONAL STATEMENTS #

    if "Hi" in user_input:
        print(f"Hi, {user_name}!")
    elif "Hello" in user_input:
        print(f"Hello, {user_name}!")
    elif "name" in user_input:
        print("That's for me to know and you to find out")
    
    elif user_input == "Where are you?":
        print("I bet you'd like to know")
    elif user_input == "How are you?":
        print(f"I'm great! How are you, {user_name}?")
    elif user_input == "What are you?":
        print(f"I'm Patrick, duh!")
    elif "" in user_input:
        a = random.randint(1,4)
        if a == 1:
            print("Woah")
        elif a == 2:
            print("That's funny")
        elif a == 3:
            print("Is mayonnaise an instrument?")
        elif a == 4:
            print("Can you keep a secret?")
        
    if MAGIC_WORD in user_input:
        magic_word_ct += 1

    if (PASSWORD1 in user_input) and (PASSWORD2 in user_input):
        unlocked_password = True

# say goodbye to the user 
# print the magic phrase count if it was more than 0
# check whether the user entered the correct passwords, and print a secret message if so
# YOUR CODE HERE #

if "goodbye" in user_input:
    print(f"Bye, {user_name}. Nice talking to you!")
if magic_word_ct > 0:
    print(f"You said the magic word {magic_word_ct} times!")
if unlocked_password == True:
    print(SECRET_MESSAGE)
