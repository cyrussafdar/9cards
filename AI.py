#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:30:18 2022

@author: cyrussafdar
"""
from Logic import *
from Display import*
import random
def SimpleHandValue(Hand):
    value=0
    FirstHand_weight=1
    SecondHand_weight=1
    ThirdHand_weight=1
    
    FirstHandRank=HashedHandRank(Hand[0:3])
    SecondHandRank=HashedHandRank(Hand[3:6])
    ThirdHandRank=HashedHandRank(Hand[6:9])
    
    value+=FirstHandRank*FirstHand_weight
    value+=SecondHandRank*SecondHand_weight
    value+=ThirdHandRank*ThirdHand_weight
    return value
def BottomHeavyHandValue(Hand):
    value=0
    FirstHand_weight=1
    SecondHand_weight=1
    ThirdHand_weight=1.75
    
    FirstHandRank=HashedHandRank(Hand[0:3])
    SecondHandRank=HashedHandRank(Hand[3:6])
    ThirdHandRank=HashedHandRank(Hand[6:9])
    
    
    value+=FirstHandRank*FirstHand_weight
    value+=SecondHandRank*SecondHand_weight
    value+=ThirdHandRank*ThirdHand_weight
    return value
def TopHeavyHandValue(Hand):
    value=0
    FirstHand_weight=2
    SecondHand_weight=1.5
    ThirdHand_weight=1
    
    FirstHandRank=HashedHandRank(Hand[0:3])
    SecondHandRank=HashedHandRank(Hand[3:6])
    ThirdHandRank=HashedHandRank(Hand[6:9])
    
    
    value+=FirstHandRank*FirstHand_weight
    value+=SecondHandRank*SecondHand_weight
    value+=ThirdHandRank*ThirdHand_weight
    return value
def HandSorter(hashnumber):
    hashstring=str(hashnumber)[::-1]
    while(len(hashstring)<18):
        hashstring+="0"
    print(hashstring)
    return (int)(hashstring[::-1])

def RandomOrderGenerator():
    order=""
    indices=[0,1,2,3,4,5,6,7,8]
    random.shuffle(indices)
    for i in range(len(indices)):
        order+=str(indices[i])
        if(i!=len(indices)-1):
            order+=","
    return order
        
def RandomHandSorter(Hand,Value_function):
    BestHand=Set_Order_fixer(Hand)
    BestValue=Value_function(Hand)
    #takes in an unordered hand and returns a hand with some logic applied
    for i in range(200):
        current_hand=Hand_reorder(Hand,RandomOrderGenerator())
        current_hand=Set_Order_fixer(current_hand)
        current_val=Value_function(current_hand)
        if(BestValue<current_val):
            #print("Hand no: "+str(i))
            #Hand_print(current_hand)
            BestValue=current_val
            BestHand=current_hand
    return BestHand
def DoubleStratAI(Hand):
    Bottom=RandomHandSorter(Hand,BottomHeavyHandValue)
    Top=RandomHandSorter(Hand,TopHeavyHandValue)
    return winning_hand(Top,Bottom)
    
def RandomAItest():
    Hands=HandGenerator(1)
    Hand_print(Hands[0])
    print("Simple Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],SimpleHandValue))
    print("Bottom Heavy Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],BottomHeavyHandValue))
    print("Top Heavy Hand Value Function")
    Hand_print(RandomHandSorter(Hands[0],TopHeavyHandValue))
    print("Both Strategies")
    Hand_print(DoubleStratAI(Hands[0]))