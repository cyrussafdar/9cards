#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:18:44 2021

@author: cyrussafdar
"""
import random
import colorama
import ast
from Cache import*
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
def has_four_of_a_kind(Hand):
    CardDict=dict()
    #IndicesDict=dict()
    highestFreq=0
    CardOfConcern=-1
    for i in range(len(Hand)):
        
        if Hand[i].Card not in CardDict:
            CardDict[Hand[i].Card]=1
            #IndicesDict[Hand[i].Card]=str(i)
        else:
            CardDict[Hand[i].Card ]+=1
            #IndicesDict[Hand[i].Card]+=","+str(i)
            if(CardDict[Hand[i].Card]>highestFreq):
                highestFreq=CardDict[Hand[i].Card]
            if(CardDict[Hand[i].Card]==4):
                if(CardOfConcern<Hand[i].Card):
                    CardOfConcern=Hand[i].Card
                
            
    #print(IndicesDict)
    return CardOfConcern
    
def hasFourPair(Hand):
    CardDict=dict()          
    Index_string=""
    for i in range(len(Hand)):
        if Hand[i].Card not in CardDict:
            CardDict[Hand[i].Card]=str(i)
        else:
            CardDict[Hand[i].Card]+=","+str(i)
            #indicates a pair
            if(len(CardDict[Hand[i].Card])==3):
                Index_string+=CardDict[Hand[i].Card]+','
    return Index_string
def HashedHandRank(Card_set):
    return Cache["Rank"][SortedCardsToHash(Card_set)]

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


def Set_Order_fixer_v2(Hand):
    """Takes in a hand and reorders them as per Handrank returns 
    the indices of the original hands in the order of highest rank """
    setDict={}
    Ranks=[]
    for i in range(0,len(Hand),3):
        #creating an inverse dictionary
        Card_set=Hand[i:i+3]
        rank=HashedHandRank(Card_set)
        #setDict[value]=
        
        if(rank in setDict):
            if(isinstance(setDict[rank], list)):
                setDict[rank].extend(Card_set)
            else:
                setDict[rank]=[Card_set,setDict[rank]]
        else:
            setDict[rank]=Card_set
        Ranks.append(rank)
        
    Ranks.sort(reverse=True)
    unique_ranks=set()
    Ordered_Sets=[]
    for r in Ranks:
        if(r not in unique_ranks):
            Ordered_Sets.extend(setDict[r])
            unique_ranks.add(r)
        
        
    return Ordered_Sets

def Sorted_Hands(Sets):
    """Takes in a list of sets and reorders them as per Handrank returns 
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