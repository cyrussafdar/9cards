#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:51:28 2022

@author: cyrussafdar
"""

#CommandLine Game
from Logic import *
from colorama import Fore
def Hand_print(Hand):
    print(Fore.BLACK+"______________________________________________")
    print(Fore.BLACK+"|    |    |    |    |    |    |    |    |    |")
    handstring=Fore.BLACK+"|"
    for card in Hand:
        #if(card.number!=10)
        handstring+=" "
        handstring+=card.text()
        if(card.Card==8):
            handstring+=Fore.BLACK+"|"
        else:
            handstring+=Fore.BLACK+" |"
    print(handstring)
    print(Fore.BLACK+"|____|____|____|____|____|____|____|____|____|")
def position_print():
    print(Fore.BLACK+" "+"  0  "+"  1  "+"  2  "+"  3  "+"  4  "+"  5  "+"  6  "+"  7  "+"  8  ")
    
def Hand_reorder(Hand,order_string):
   #Takes in a string with postions 0 to 8
   #in the form a,b,c,d,e,f,g,h,i
   order_string.strip()
   new_hand=list()
   for index in order_string.split(","):
       new_hand.append(Hand[(int)(index)])
   return new_hand
    
   
   
   
#Hands=HandGenerator(2)

#Hand_print(Hands[0])
#Hands[0]=Hand_reorder(Hands[0],"3,4,5,6,1,2,7,8,0")
#Hand_print(Hands[0])
def Computer_Game():
    #Generate hands
    Hands=HandGenerator(2)
    #set hand 
    Player_hand=Hands[0]
    print("Your hand: ")
    Hand_print(Player_hand)
    position_print()
    print("Input the Order you want your cards")
    order=input()
    Player_hand=Hand_reorder(Player_hand,order)
    print("Your reordered hand: ")
    Hand_print(Player_hand)
    print("Computer's hand: ")
    Computer_hand=Hands[1]
    #Computer reorder function
    Hand_print(Computer_hand)
    #result of 0 means a tie
    #result of 1 means the first hand won Player
    #result of 2 means the second hand won Computer
    result,p1_points,p2_points=two_Player_winner(Player_hand,Computer_hand)
    if(result==0):
        print("Kitty")
        return result,p1_points,p2_points
    elif(result==1):
        print("Player wins")
        print(str(p1_points)+" hands to "+ str(p2_points))
        return result,p1_points,p2_points
    else:
        print("Computer wins")
        print(str(p2_points)+" hands to "+ str(p1_points))
        return result,p1_points,p2_points

def Two_player_game():
    print("Press Enter to start game")
    input()
    #Generate hands
    Hands=HandGenerator(2)
    #set hand 
    Player_hand=Hands[0]
    print("Player 1's hand: ")
    Hand_print(Player_hand)
    position_print()
    print("Input the Order you want your cards")
    order=input()
    Player_hand=Hand_reorder(Player_hand,order)
    print("Player 1's reordered hand: ")
    Hand_print(Player_hand)
    #printing 12 spaces to make sure the cards cannot be seen
    for i in range(12):
        print()
    print("pass it to Player 2")
    print("Player 2 press enter")
    input()
    Player2_hand=Hands[1]
    print("Player 2's hand: ")
    Hand_print(Player2_hand)
    position_print()
    print("Input the Order you want your cards")
    order=input()
    Player2_hand=Hand_reorder(Player2_hand,order)
    print("Player 2's reordered hand: ")
    #Computer reorder function
    Hand_print(Player2_hand)
    
    print("Player 1's reordered hand: ")
    Hand_print(Player_hand)
    #result of 0 means a tie
    #result of 1 means the first hand won Player
    #result of 2 means the second hand won Computer
    result,p1_points,p2_points=two_Player_winner(Player_hand,Player2_hand)
    if(result==0):
        print("Kitty")
        return result,p1_points,p2_points
    elif(result==1):
        print("Player 1 wins")
        print(str(p1_points)+" hands to "+ str(p2_points))
        return result,p1_points,p2_points
    else:
        print("Player 2 wins")
        print(str(p2_points)+" hands to "+ str(p1_points))
        return result,p1_points,p2_points   

def Best_to(Game_no):
    P1_wins=0
    P1_hands_won=0
    P2_wins=0
    P2_hands_won=0
    #a Kitty increases the payout by 1
    win_payout=1
    #Game number
    game_no=1
    while(P1_wins<Game_no and P2_wins<Game_no):
        print("Game "+str(game_no)+": ")
        result,P1_set,P2_set=Two_player_game()
        P1_hands_won+=P1_set
        P2_hands_won+=P2_set
        if(result==0):
            win_payout+=1
        else:
            if(result==1):
                P1_wins+=win_payout
            if(result==2):
                P2_wins+=win_payout
            win_payout=1
        print("Player 1 score: "+str(P1_wins))
        print("Player 2 score: "+str(P2_wins))
        print()
        print("Total hands won by Player 1: " +str(P1_hands_won))
        print("Total hands won by Player 2: " +str(P2_hands_won))
    if(P1_wins>P2_wins):
        print("Player 1 wins series")
        print(str(P1_wins)+" to "+str(P2_wins))
    else:
        print("Player 2 wins series")
        print(str(P2_wins)+" to "+str(P1_wins))
        #incrementing the game number
        game_no+=1

#while(True):
    
    