#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:18:44 2021

@author: cyrussafdar
"""
import random
import colorama
from colorama import Fore
Suits=["♠","♥","♣","♦"]
Cards=["2","3","4","5", "6","7","8","9", "10", "J","Q","K","A"]

#takes in numbers from 0 to 51
class CARD(object):
    def __init__(self, number):
        self.number=number
    
    @property
    def Suit_num(self):
        return (int)(self.number/13)
    @property
    def Suit(self):
        return Suits[(int)(self.number/13)]
    @property
    def Card(self):
        return (int)(self.number%13)
    def text(self):
        if(self.Suit=="♥" or self.Suit=="♦"):
            return(Fore.RED+Cards[self.Card]+self.Suit)
        else:
            return(Fore.BLACK+Cards[self.Card]+self.Suit)
    def Print(self):
        if(self.Suit=="♥" or self.Suit=="♦"):
            print(Fore.RED+Cards[self.Card]+self.Suit)
        else:
            print(Fore.BLACK+Cards[self.Card]+self.Suit)
    
def DeckCreateandShuffle():
    Deck=list()
    #populate it
    for i in range(52):
        Deck.append(CARD(i))
    #shuffle tbhe deck
    random.shuffle(Deck)
    return Deck
def HandGenerator(player_num):  
    #List container for two hands
    Hands=list()
    #Create Deck
    Deck=DeckCreateandShuffle()
    
    for i in range(player_num):
        Hands.append(list())
        for j in range(9):
            #Dealing the hands one by one
            Hands[i].append(Deck[i+j*player_num])
        
    #Contains a list of 9 Card objects    
    return Hands
    

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



#Rankings
            #Three of a Kind =5
            #Straight flush/ Colour run=4
            #Straight/Run=3
            #Flush/Colour=2
            #Pair=1
            #Nothing=0
#A of hearts 2 of hearts 3 of hearts
StraightFlush=[CARD(12),CARD(0),CARD(1)]
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

def betterSet(Set_1,Set_2):
    #returns 1 if Set_1 is stronger
    #returns 2 if Set_2 is stronger
    #returns 0 if tied
    Handrank_1,cards_1=Handrank(Set_1)
    Handrank_2,cards_2=Handrank(Set_2)
    if(Handrank_1>Handrank_2):
        return 1
    elif(Handrank_1<Handrank_2):
        return 2
    else:
        for i in range(3):
            if(cards_1[i]>cards_2[i]):
                return 1
            if(cards_1[i]<cards_2[i]):
                return 2
    #if none of the other exit conditions are met return the final tied result
    return 0
def winning_hand(Hand_1,Hand_2):
    p1_points=0
    p2_points=0
    #Show cards
    i=0
    #This loop might be triggered by a mutual agreement to show or a timer
    while(i<7):
        if(betterSet(Hand_1[i:i+3],Hand_2[i:i+3])==1):
            p1_points+=1
        elif(betterSet(Hand_1[i:i+3],Hand_2[i:i+3])==2):
            p2_points+=1
        i+=3
    if(p1_points>p2_points):
        return Hand_1
    else:
        return Hand_2
    
def two_Player_winner(Hand_1,Hand_2):
    p1_points=0
    p2_points=0
    #Show cards
    i=0
    #This loop might be triggered by a mutual agreement to show or a timer
    while(i<7):
        if(betterSet(Hand_1[i:i+3],Hand_2[i:i+3])==1):
            p1_points+=1
        elif(betterSet(Hand_1[i:i+3],Hand_2[i:i+3])==2):
            p2_points+=1
        i+=3
    if(p1_points>p2_points):
        return 1,p1_points,p2_points
    elif(p1_points<p2_points):
        return 2,p1_points,p2_points
    else:
        return 0,p1_points,p2_points
    
def Handrank(Card_set):
        #Takes a set of 3 cards and returns its 
        Card_count=[0]*13
        Suit_count=[0]*4
        Comparing_Order=[]
        #Slight nuance for pairs the pair should be compared first for others a 
        #list sorted in descending order is fine
        colour=False
        straight=False
        for card in Card_set:
            Card_count[card.Card]+=1
            Comparing_Order.append(card.Card)  
            if(Card_count[card.Card]==3):
                #condition for it being three of a kind
                return 5, Comparing_Order
            Suit_count[card.Suit_num]+=1
            if(Suit_count[card.Suit_num]==3):
                colour=True
        
        Comparing_Order.sort(reverse=True)
        #print(Comparing_Order)
        #The case where two numbers are the same and sorted with the pair first
        if(Comparing_Order[0]==Comparing_Order[1]):
            return 1,Comparing_Order
        #The case where theres pairs and theyre sorted with the pair second
        if(Comparing_Order[1]==Comparing_Order[2]):
            return 1,[Comparing_Order[1],Comparing_Order[2],Comparing_Order[0]]
        
            
        if(Comparing_Order[0]-1==Comparing_Order[1] and 
           Comparing_Order[1]-1== Comparing_Order[2]):
            straight=True
        if(Comparing_Order[0]==12 and Comparing_Order[1]==1 and Comparing_Order[2]==0):
            straight=True
        
        if(straight and colour):
            return 4,Comparing_Order
        elif(straight):
            return 3,Comparing_Order
        elif(colour):
            return 2,Comparing_Order
        else:
            return 0,Comparing_Order

def Hand_reorder(Hand,order_string):
   #Takes in a string with postions 0 to 8
   #in the form a,b,c,d,e,f,g,h,i
   order_string.strip()
   new_hand=list()
   for index in order_string.split(","):
       new_hand.append(Hand[(int)(index)])
   return new_hand
    
def Hand_popper(Hand,indices):
   #Returns a string without the existing indices
   #makes the command line game simpler
   unordered_hand=list()
   ordered_hand=list()
   indices.strip()
   indices=indices.split(",")
   #doing it this way to retain the order that the user wants
   for i in indices:
       #print(i)
       ordered_hand.append(Hand[(int)(i)])
   indices=set(indices)
   for i in range(len(Hand)):
       if(str(i) not in indices):
           unordered_hand.append(Hand[i])

   return unordered_hand,ordered_hand   

def Set_Order_fixer(Hand):
    """Input: Takes in a Hand and 
    Output: Hand sorted by sets largest rank """
    #using bubble sort because hands need to be compared to understand the value
    sets=list()
    for i in range(0,8,3):
        sets.append(Hand[i:i+3])
    swap_flag=True
    while(swap_flag):
        swap_flag=False
        for i in range(2):
            if(betterSet(sets[i],sets[i+1])!=1):
                temp=sets[i]
                sets[i]=sets[i+1]
                sets[i+1]=temp
                swap_flag=True
    
    sortedHand=sets[0]
    sortedHand.extend(sets[1])  
    sortedHand.extend(sets[2])      
    return sortedHand
    