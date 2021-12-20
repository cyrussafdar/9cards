#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:18:44 2021

@author: cyrussafdar
"""
import random
Suits=["Spades","Hearts","Clubs","Dice"]
Cards=["Two","Three","Four","Five", "Six","Seven","Eight","Nine", "Ten", "Jack","Queen","King","Ace"]

#takes in numbers from 0 to 51
class CARD(object):
    def __init__(self, number):
        self.number=number
    
    @property
    def Suit(self):
        return Suits[(int)(self.number/13)]

    @property
    def Card(self):
        return (int)(self.number%13)
    
    def Print(self):
        print(Cards[self.Card]+" of "+self.Suit)
    
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
            Hands[i].append(Deck[i+j*player_num])
        
    #Contains a list of 9 Card objects    
    return Hands
    
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
    
    

#def ThreePlayerGame():
    
    
#def FourPlayerGame():

    
#def FivePlayerGame():
    
