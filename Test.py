#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:54:00 2022

@author: cyrussafdar
"""
from Logic import *
from Display import*
from Command_Line_game import*
from ObsoleteMethods import*
from AI import*
from Cache import*
import matplotlib.pyplot as plt
import numpy as np
import math
#A of hearts 2 of hearts 3 of hearts
StraightFlush=[CARD(12),CARD(0),CARD(1)]
differentSuitsameSFLUSH=[CARD(25),CARD(13),CARD(14)]
#2 of hearts 3 of hearts 4 of hearts
LowerStraightFlush=[CARD(2),CARD(0),CARD(1)]

#5 of spades, 5 of hearts, 5 of dice
ThreeofAkind=[CARD(3),CARD(16),CARD(29)]
#2 of spades, 2 of hearts, 2 of dice
LowerThreeofAkind=[CARD(0),CARD(13),CARD(26)]
#A of hearts 2 of spades 3 of spades
Straight=[CARD(25),CARD(0),CARD(1)]
# K of hearts Q of hearts J of spades
LowerStraight=[CARD(24),CARD(23),CARD(9)]
# 2 of spades, 2 of hearts, 4 of spades
Pair=[CARD(0),CARD(13),CARD(2)]
# K of spades, K of hearts, 4 of spades
Mid_pair=[CARD(11),CARD(24),CARD(2)]
# A of spades, A of hearts, 4 of spades
High_pair=[CARD(12),CARD(25),CARD(2)]
# A of spades, A of hearts, 6 of spades
Higher_pair_by_card=[CARD(12),CARD(25),CARD(4)]
Nothing=[CARD(0),CARD(16),CARD(2)]
Different_Suit_Nothing=[CARD(26),CARD(29),CARD(41)]

Player1Hand=ThreeofAkind+LowerThreeofAkind+Pair
Player2Hand=LowerThreeofAkind+High_pair+Mid_pair

#Testing code

def HandTest():
    for i in range(2,6):
        Hands=HandGenerator(i)
        print(f"Test for {i} hands")
        for hand in Hands:
            print("Hand:\n")
            for card in hand:
                card.Print()
            print()
        print()
#Testing the card generation
def GeneratedHandTest(Hands):
    for hand in Hands:
        print("Hand:\n")
        for card in hand:
            card.Print()
            print()
def PlayerTest():
    Players=Player_generate_prompt_v2()
    for p in Players:
        print(p.identifier())
# Command Line Tests    
def Round_loop_test():
    Players=[Player_v2("Computer","Cyrus"),Player_v2("Computer","Billy Gates 2"),Player_v2("Computer","Billy Gates 3"),Player_v2("Computer","Billy Gates 4"),Player_v2("Computer","Billy Gates 5")]
    PlayerNo=0
    CompNo=5
    Players,w=Round_loop(Players,PlayerNo,CompNo)
    if(w==None):
        print("Kitty")
    else:
        print(Players[w].name+" wins")
    for p in Players:
        print(p.name+" won "+str(p.total_hands)+ " hands")

#AI Tests
def AIheadtoheadSameHand(Strategy1,Strategy2,series_length):
    scoreDict={Strategy1.__name__+"1":0,Strategy2.__name__+"2":0,"Ties":0}
    for i in range(series_length):
        print("game "+str(i)+ "started")
        Hands=HandGenerator(1)
        res,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy1),RandomHandSorter(Hands[0],Strategy2))
        if(res==1):
            scoreDict[Strategy1.__name__+"1"]+=1
        elif(res==2):
            scoreDict[Strategy2.__name__+"2"]+=1
        else:
            scoreDict["Ties"]+=1
        print("game "+str(i)+ "done")
        print(scoreDict)
    return(scoreDict)

def AIheadtoheadVsMe(Strategy1,Strategy2,series_length):
    ##NOT COMPLETE YET
    scoreDict=dict()
    scoreDict[Strategy1.__name__+" Win"]=0
    scoreDict[Strategy1.__name__+" Ties"]=0
    scoreDict[Strategy2.__name__+" Win"]=0
    scoreDict[Strategy2.__name__+" Ties"]=0
    for i in range(series_length):
        #print("game "+str(i)+ "started")
        Hands=HandGenerator(2)
        Strategy3Hand=Player_input_prompt(Hands[1],"Cyrus",2)
        res,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy1),Strategy3Hand)
        res2,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy2),Strategy3Hand)
        if(res==1):
            scoreDict[Strategy1.__name__+" Win"]+=1
        elif(res==0):
            scoreDict[Strategy1.__name__+" Ties"]+=1
        
        if(res2==1):
            scoreDict[Strategy2.__name__+" Win"]+=1
        elif(res2==0):
            scoreDict[Strategy2.__name__+" Ties"]+=1
        print("game "+str(i)+ "done")
        #print(scoreDict)
    print(f"Out of {series_length} games")
    return(scoreDict)
#Best Test thusfar   
def AIheadtoheadBothHands(Strategy1,Strategy2,series_length):
    scoreDict=dict()
    scoreDict[Strategy1.__name__+" Win"]=0
    scoreDict[Strategy2.__name__+" Win"]=0
    scoreDict["Ties"]=0
    for i in range(series_length):
        #print("game "+str(i)+ "started")
        Hands=HandGenerator(2)
        res,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy1),RandomHandSorter(Hands[1],Strategy2))
        res2,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy2),RandomHandSorter(Hands[1],Strategy1))
        if(res==1):
            scoreDict[Strategy1.__name__+" Win"]+=1
        elif(res==2):
            scoreDict[Strategy2.__name__+" Win"]+=1
        elif(res==0):
            scoreDict["Ties"]+=1
        
        if(res2==1):
            scoreDict[Strategy2.__name__+" Win"]+=1
        elif(res2==2):
            scoreDict[Strategy1.__name__+" Win"]+=1
        elif(res2==0):
            scoreDict["Ties"]+=1
        if(res!=res2):
            if(res==1 and res2==2):
                print(Strategy1.__name__+ " wins with both hands")
            elif(res==2 and res2==1):
                print(Strategy2.__name__+ " wins with both hands")
            #elif(res==0 and res==1):
                #print(Strategy2.__name__+ " wins with both hands")
            #print(f"res= {res}")
            #print(f"res2= {res2}")
        #print("game "+str(i)+ "done")
        #print(scoreDict)
    #print(f"Out of {series_length} games")
    return(scoreDict)
def RandomAItest():
    Hands=HandGenerator(1)
    Hand_print(Hands[0])
    print("Simple Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],SimpleHandValue))
    print("Bottom Heavy Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],BottomHeavyHandValue))
    print("Middle Heavy Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],MiddleHeavyHandValue))
    print("Complex Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],ComplexValue))
    print("Top Heavy Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],TopHeavyHandValue))
    print("Prob ordering")
    Hand_print(RandomHandSorter(Hands[0],Hand_Win_prob))
    print("Smarter Prob ordering")
    Hand_print(RandomHandSorter(Hands[0],Smarter_Hand_Win_prob))
    print("ComplexHand_V2")
    Hand_print(RandomHandSorter(Hands[0],ComplexValue_v2))

#Order checker
def SetOrderchecker():
    Hands=HandGenerator(5)
    for hand in Hands:
        Hand_print(hand)
        print("version 1 :")
        Hand_print(Set_Order_fixer(hand))
        print("version 2 :")
        Hand_print(Set_Order_fixer(hand))