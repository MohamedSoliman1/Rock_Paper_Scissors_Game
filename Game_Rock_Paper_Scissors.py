
# coding: utf-8

# In[ ]:

#Hello, this code is an implementation of the famous game Rock, Paper, Scissors.
#The user can choose to play against the computer or against another player.

import random #To make the computer choose a random choice.
from getpass import getpass #If two friend are playing against eachother, then their inpur will be hidden as the password
                            #To avoid cheating! :D

    #This function is used to determine whether the user wants to exit the game or play another round!
def Continue_or_exit():
    while(1):
        print("Do you want to exit?")
        exit = input("Enter your choice: (Yes/No)? ")
        exit = exit.lower()
        if(exit == "yes"):
            print("\nBye bye!")
            exit = 0
            return exit
        elif(exit == 'no'):
            exit = 1
            return exit
        else:
            print("You can only enter yes or no!")

exit = 1  # When exit is 0 the game will end
while(exit):
    print("\nHi there! Do you want to play with the computer or with a friend?\n")
    
    Computer_or_two_players = input("Enter your choice (Computer/friend): ")
    Computer_or_two_players = Computer_or_two_players.lower() #I have transformed all the letters to small case, to make the
                                                              #user input case insensitive
    
    if(Computer_or_two_players == "computer"):
        Choice1 = input("Player1: Enter your choice(Rock/Paper/Scissors): ")
        computer_options = ['rock', 'scissors', 'paper']
        Choice2 = random.choice(computer_options) #The computer will choose a random choice.
        Second_player_name = "Computer" #To choose the name of the second player whether the computer or player 2
        PASS = 0 #If pass  = 0 then the user (computer/friend) input was correct
    elif(Computer_or_two_players == "friend"): 
        Choice1 = getpass("Player1: Enter your choice(Rock/Paper/Scissors): ") #The input will be hidden as the password
        Choice2 = getpass("Player2: Enter your choice(Rock/Paper/Scissors): ") #The input will be hidden as the password
        Second_player_name = "Player 2" #To choose the name of the second player whether the computer or player 2
        PASS = 0 #If pass  = 0 then the user (computer/friend) input was correct
    else:
        print("\nWell, you have to choose computer/friend only!")
        PASS = 1 #If pass = 1 then the user (computer/friend) input is not correct and will be asked to re-enter his choices.
    
    Choice1 = Choice1.lower()
    Choice2 = Choice2.lower()
##########################################
    if(PASS ==1):
        pass #The user (computer/friend) input was incorrect, the user will be asked to re-enter the correct choice.
    elif(Choice1 == "rock" and Choice2 == "scissors"):
        print("\nPlayer 1 chose rock " + f"- {Second_player_name} chose scissors") #Second_player_name = Computer/Player 2
        print("Player 1 wins")
        exit = Continue_or_exit()
    elif(Choice1 == "rock" and Choice2 == "paper"):
        print(f"\nPlayer 1 chose rock " + f"- {Second_player_name} chose paper")
        print(f"{Second_player_name} wins")
        exit = Continue_or_exit()
    elif(Choice1 == "rock" and Choice2 == "rock"):
        print(f"\nPlayer 1 chose rock " + f"- {Second_player_name} chose rock")
        print("TIE!")
        exit = Continue_or_exit()
##########################################
    elif(Choice1 == "scissors" and Choice2 == "scissors"):
        print(f"\nPlayer 1 chose scissors " + f"- {Second_player_name} chose scissors")
        print("TIE!")
        exit = Continue_or_exit()
    elif(Choice1 == "scissors" and Choice2 == "paper"):
        print(f"\nPlayer 1 chose scissors " + f"- {Second_player_name} chose paper")
        print("Player 1 wins")
        exit = Continue_or_exit()
    elif(Choice1 == "scissors" and Choice2 == "rock"):
        print(f"\nPlayer 1 chose scissors " + f"- {Second_player_name} chose rock")
        print(f"{Second_player_name} wins")
        exit = Continue_or_exit()
##########################################
    elif(Choice1 == "paper" and Choice2 == "scissors"):
        print(f"\nPlayer 1 chose paper " + f"- {Second_player_name} chose scissors")
        print(f"{Second_player_name} wins")
        exit = Continue_or_exit()
    elif(Choice1 == "paper" and Choice2 == "paper"):
        print(f"\nPlayer 1 chose paper " + f"- {Second_player_name} chose paper")
        print("TIE!")
        exit = Continue_or_exit()
    elif(Choice1 == "paper" and Choice2 == "rock"):
        print(f"\nPlayer 1 chose paper " + f"- {Second_player_name} chose rock")
        print("Player1 wins")
        exit = Continue_or_exit()
    else:
        print("\nWell, you have to choose Rock/Paper/Scissors only!\n") 
        #If the user entered invalid choice, not (rock/paper/scissors)

