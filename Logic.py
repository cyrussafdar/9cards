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
def CardsToHash(Card_set):
    mult=1
    HashNumber=0
    
    for card in Card_set:
        HashNumber+=card.number*mult
        mult*=100
    return HashNumber

def Hashto9Cards(hashnumber):
    Cards=list()
    div=1
    mod=100
    for i in range(9):
        Cards.append(CARD((hashnumber%mod)//div))
        div*=100
        mod*=100
    return Cards

def Hashto3Cards(hashnumber):
    Cards=list()
    div=1
    mod=100
    for i in range(3):
        Cards.append(CARD((hashnumber%mod)//div))
        div*=100
        mod*=100
    return Cards

def SortedCardsToHash(Card_set):
    """Only to be used with 3 cards as using this with more than that will 
    change the order and hence the value of cards"""
    mult=1
    HashNumber=0
    NumberList=list()
    for card in Card_set:
        NumberList.append(card.number)
    #Sorting by ascending
    NumberList.sort(reverse=True)
    for num in NumberList:
        HashNumber+=num*mult
        mult*=100
    return HashNumber    
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
def DeckCreateandShuffleHash():
    Deck=list()
    #populate it
    for i in range(52):
        Deck.append(i)
    #shuffle tbhe deck
    random.shuffle(Deck)
    return Deck
def HandGeneratorHash(player_num):  
    #List container for two hands
    Hands=[0]*player_num
    #Create Deck
    Deck=DeckCreateandShuffleHash()
    
    
    for i in range(player_num):
        mult=1
        for j in range(9):
            #Dealing the hands one by one
            Hands[i]+=Deck[i+j*player_num]*mult
            mult*=100
        
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
    Handrank_1=HashedHandRank(Set_1)
    Handrank_2=HashedHandRank(Set_2)
    
    if(Handrank_1>Handrank_2):
        return 1
    elif(Handrank_1<Handrank_2):
        return 2
    else:
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
    return Rank[SortedCardsToHash(Card_set)]
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
                return 5+CardsToHash([CARD(Comparing_Order[0]),CARD(Comparing_Order[1]),CARD(Comparing_Order[2])])/10000000
            Suit_count[card.Suit_num]+=1
            if(Suit_count[card.Suit_num]==3):
                colour=True
        
        Comparing_Order.sort(reverse=True)
        #print(Comparing_Order)
        #The case where two numbers are the same and sorted with the pair first
        if(Comparing_Order[0]==Comparing_Order[1]):
            return 1+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        #The case where theres pairs and theyre sorted with the pair second
        elif(Comparing_Order[1]==Comparing_Order[2]):
            return 1+CardsToHash([CARD(Comparing_Order[0]),CARD(Comparing_Order[1]),CARD(Comparing_Order[2])])/10000000
        
            
        if(Comparing_Order[0]-1==Comparing_Order[1] and 
           Comparing_Order[1]-1== Comparing_Order[2]):
            straight=True
        if(Comparing_Order[0]==12 and Comparing_Order[1]==1 and Comparing_Order[2]==0):
            straight=True
        
        if(straight and colour):
            return 4+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        elif(straight):
            return 3+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        elif(colour):
            return 2+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        else:
            return 0+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000

def Hand_reorder(Hand,order_string):
   #Takes in a string with postions 0 to 8
   #in the form a,b,c,d,e,f,g,h,i
   order_string.strip()
   new_hand=list()
   for index in order_string.split(","):
       #print(sys.getsizeof(index))
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
def Set_Order_fixer_v2(Sets):
    """Takes in hands and reorders them as per Handrank returns 
    the indices of the original hands in the order of highest rank """
    setDict={}
    Ranks=[]
    swap_flag=True
    for i in range(len(Sets)):
        #creating an inverse dictionary
        rank=HashedHandRank(Sets[i])
        CardHash=CardsToHash(Sets[i])
        #setDict[value]=
        if(isinstance(setDict[rank], list)):
            setDict[rank].append(i)
        if(rank in setDict):
            setDict[rank]=[i,setDict[rank]]
        else:
            setDict[rank]=i
        Ranks.append(rank)
        
    Ranks.sort(reverse=True)
    Ordered_Sets=[]
    for v in values:
        if(isinstance(setDict[v], int)):
            Ordered_Sets.append(setDict[v])
        else:
            Ordered_Sets.extend(setDict[v])
    return Ordered_Sets
def Sorted_Hands(Sets):
    """Takes in hands and reorders them as per Handrank returns 
    the indices of the original hands in the order of highest rank """
    setDict={}
    values=[]
    for i in range(len(Sets)):
        #creating an inverse dictionary
        value=HashedHandRank(Sets[i])
        if(value in setDict):
            setDict[value]=[i,setDict[value]]
        else:
            setDict[value]=i
        values.append(value)
        
    values.sort(reverse=True)
    Ordered_Sets=[]
    for i in range(2):
        if(isinstance(setDict[values[i]], int)):
            Ordered_Sets.append(setDict[values[i]])
        else:
            Ordered_Sets.extend(setDict[values[i]])
    return Ordered_Sets
def Sorted_Hands_v2(Sets):
    """Takes in hands and reorders them as per Handrank returns 
    the indices of the original hands in the order of highest rank but using a more efficient sort"""
#    if(len(Sets)==2):
#        #code
#        continue
#    if(len(Sets)==3):
#        continue
#    if(len(Sets)==4):
#        continue
#    if(len(Sets)==5):
#        continue
    return