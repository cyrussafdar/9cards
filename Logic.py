#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:18:44 2021

@author: cyrussafdar
"""
import random
import colorama
import ast
from colorama import Fore

Suits=["♠","♥","♣","♦"]
Cards=["2","3","4","5", "6","7","8","9", "10", "J","Q","K","A"]

#Hashing methods
def CardToHash(Set_of_Cards):
    return HashKeyGenerator(Set_of_Cards[0].number,Set_of_Cards[1].number,Set_of_Cards[2].number)
def ListToCards(ListOfCardNumbers):
    return [CARD(ListOfCardNumbers[0]),CARD(ListOfCardNumbers[1]),CARD(ListOfCardNumbers[2])]
def HashKeyGenerator(i,j,k):
    return i**5+j**5+k**5+i**5*j**5*k**5
#Loading the hash values for each hand
with open('hash.txt') as f:
    data = f.read()
#Loading the dictionary
HashToNumbers = ast.literal_eval(data)
with open('Rank.txt') as f:
    data=f.read()
Rank=ast.literal_eval(data)
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



#Rankings
            #Three of a Kind =5
            #Straight flush/ Colour run=4
            #Straight/Run=3
            #Flush/Colour=2
            #Pair=1
            #Nothing=0


def betterSet(Set_1,Set_2):
    #returns 1 if Set_1 is stronger
    #returns 2 if Set_2 is stronger
    #returns 0 if tied
    Handrank_1,cards_1=HashedHandRank(Set_1)
    Handrank_2,cards_2=HashedHandRank(Set_2)
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
def HashedHandRank(Card_set):
    return Rank[CardToHash(Card_set)]
#This function is if I need to replace the bubble swap to make it more efficient
def Handrank_Orderless(Card_set):
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
            return 1
        #The case where theres pairs and theyre sorted with the pair second
        if(Comparing_Order[1]==Comparing_Order[2]):
            return 1
        
            
        if(Comparing_Order[0]-1==Comparing_Order[1] and 
           Comparing_Order[1]-1== Comparing_Order[2]):
            straight=True
        if(Comparing_Order[0]==12 and Comparing_Order[1]==1 and Comparing_Order[2]==0):
            straight=True
        
        if(straight and colour):
            return 4
        elif(straight):
            return 3
        elif(colour):
            return 2
        else:
            return 0

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
def Sorted_Hands(Sets):
    """Takes in hands and reorders them as per Handrank returns 
    the indices of the original hands in the order of highest rank """
    setDict={}
    swap_flag=True
    for i in range(len(Sets)):
        #creating an inverse dictionary
        setDict[CardToHash(Sets[i])]=i
    while(swap_flag):
        swap_flag=False
        for i in range(len(Sets)-1):
            if(betterSet(Sets[i],Sets[i+1])!=1):
                temp=Sets[i]
                Sets[i]=Sets[i+1]
                Sets[i+1]=temp
                swap_flag=True
    Ordered_Sets=[]
    for s in Sets:
        Ordered_Sets.append(setDict[CardToHash(s)])
    return Ordered_Sets
    