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
    SecondHand_weight=1.5
    ThirdHand_weight=2
    
    FirstHandRank=HashedHandRank(Hand[0:3])
    SecondHandRank=HashedHandRank(Hand[3:6])
    ThirdHandRank=HashedHandRank(Hand[6:9])
    
    
    value+=FirstHandRank*FirstHand_weight
    value+=SecondHandRank*SecondHand_weight
    value+=ThirdHandRank*ThirdHand_weight
    return value
def MiddleHeavyHandValue(Hand):
    value=0
    FirstHand_weight=1
    SecondHand_weight=1.5
    ThirdHand_weight=1
    
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
def Hashtostring(hashnumber):
    zerostring="0"
    hashstring=str(hashnumber)
    #optimised for the likely cases where hashstrings are 16 or 17 
    #
    while(len(hashstring)<18):
       hashstring=zerostring+hashstring
    
    return hashstring
def HandSorter(hashnumber):
    hashstring=Hashtostring(hashnumber)
    Cards=[]
    #0(9)
    for i in range(0,17,2):
        Cards.append(hashstring[i:i+2])
with open('Orders.txt') as f:
    data=f.read()
Orders=ast.literal_eval(data)
def RandomOrderGenerator():
    return Orders[random.randint(0,1680)]
def OrderPopulator():
    orders=[]
    indices=[0,1,2,3,4,5,6,7,8]
    used_indices=set()
    Hand_sets=set()
    for i1 in range(9):
        used_indices=set()
        used_indices.add(i1)
        for i2 in range(9):
            if(i2 in used_indices):
                continue
            used_indices.add(i2)
            for i3 in range(9):
                if(i3 in used_indices):
                    continue
                used_indices.add(i3)
                for i4 in range(9):
                    if(i4 in used_indices):
                        continue
                    used_indices.add(i4)
                    for i5 in range(9):
                        if(i5 in used_indices):
                            continue
                        used_indices.add(i5)
                        for i6 in range(9):
                            if(i6 in used_indices):
                                continue
                            used_indices.add(i6)
                            for i7 in range(9):
                                if(i7 in used_indices):
                                    continue
                                used_indices.add(i7)
                                for i8 in range(9):
                                    if(i8 in used_indices):
                                        continue
                                    used_indices.add(i8)
                                    for i9 in range(9):
                                        if(i9 in used_indices):
                                            continue
                                        
                                        HASH=SetAgnosticHashGenerator(i1,i2,i3,i4,i5,i6,i7,i8,i9)
                                        if(HASH not in Hand_sets):
                                            orders.append(f"{i1},{i2},{i3},{i4},{i5},{i6},{i7},{i8},{i9}")
                                            Hand_sets.add(HASH)
                                        else:
                                            continue
                                    used_indices.remove(i8)
                                used_indices.remove(i7)
                            used_indices.remove(i6)
                        used_indices.remove(i5)
                    used_indices.remove(i4)
                used_indices.remove(i3)
            used_indices.remove(i2)                            
        used_indices.remove(i1)
    orders_return={}
    for o in range(len(orders)):
        orders_return[o]=orders[o]
    with open('Orders.txt','w') as data: 
        data.write(str(orders_return))   
    return orders 
def OrderPopulatorTest():
    orders=[]
    indices=[0,1,2,3,4,5,6,7,8]
    used_indices=set()
    Hand_dict=dict()
    for i1 in range(9):
        used_indices=set()
        used_indices.add(i1)
        for i2 in range(9):
            if(i2 in used_indices):
                continue
            used_indices.add(i2)
            for i3 in range(9):
                if(i3 in used_indices):
                    continue
                used_indices.add(i3)
                for i4 in range(9):
                    if(i4 in used_indices):
                        continue
                    used_indices.add(i4)
                    for i5 in range(9):
                        if(i5 in used_indices):
                            continue
                        used_indices.add(i5)
                        for i6 in range(9):
                            if(i6 in used_indices):
                                continue
                            used_indices.add(i6)
                            for i7 in range(9):
                                if(i7 in used_indices):
                                    continue
                                used_indices.add(i7)
                                for i8 in range(9):
                                    if(i8 in used_indices):
                                        continue
                                    used_indices.add(i8)
                                    for i9 in range(9):
                                        if(i9 in used_indices):
                                            continue
                                        
                                        HASH=SetAgnosticHashGenerator(i1,i2,i3,i4,i5,i6,i7,i8,i9)
                                        
                                        if(HASH not in Hand_dict):
                                            orders.append(f"{i1},{i2},{i3},{i4},{i5},{i6},{i7},{i8},{i9}")
                                            Hand_dict[HASH]=f"{i1},{i2},{i3},{i4},{i5},{i6},{i7},{i8},{i9}"
                                        else:
                                                
                                            if(isinstance(Hand_dict[HASH], list)):
                                                Hand_dict[HASH].append(f"{i1},{i2},{i3},{i4},{i5},{i6},{i7},{i8},{i9}")
                                            else:
                                                Hand_dict[HASH]=[Hand_dict[HASH],f"{i1},{i2},{i3},{i4},{i5},{i6},{i7},{i8},{i9}"]
                                    used_indices.remove(i8)
                                used_indices.remove(i7)
                            used_indices.remove(i6)
                        used_indices.remove(i5)
                    used_indices.remove(i4)
                used_indices.remove(i3)
            used_indices.remove(i2)                            
        used_indices.remove(i1)
    orders_return={}
    for o in range(len(orders)):
        orders_return[o]=orders[o]
    with open('Test.txt','w') as data: 
        data.write(str(Hand_dict))   
    return orders 
def SetAgnosticHashGenerator(i1,i2,i3,i4,i5,i6,i7,i8,i9):
    """This uses the fact that regardless of how the sets are organised what matters is the association between elements"""
    Hash=0
    set1=[i1,i2,i3]
    set1.sort()
    mult=1
    set1num=0
    for i in set1:
        set1num+=mult*i
        mult*=10
    
    set2=[i4,i5,i6]
    set2.sort()
    set2num=0
    mult=1
    for i in set2:
        set2num+=mult*i
        mult*=10
    
    set3=[i7,i8,i9]
    set3.sort()
    set3num=0
    mult=1
    for i in set3:
        
        set3num+=mult*i
        mult*=10
    setlist=[set1num,set2num,set3num]
    setlist.sort
    
    mult=1
    for i in setlist:
        Hash+=i*mult
        mult*=1000
    return Hash
def RandomHandSorter(Hand,Value_function):
    BestHand=Set_Order_fixer_v2(Hand)
    BestValue=Value_function(Hand)
    #takes in an unordered hand and returns a hand with some logic applied
    for i in range(1680):
        current_hand=Hand_reorder(Hand,Orders[i])
        current_hand=Set_Order_fixer_v2(current_hand)
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

def AIheadtohead(Strategy1,Strategy2,series_length):
    scoreDict={Strategy1.__name__+"1":0,Strategy2.__name__+"2":0,"Ties":0}
    for i in range(series_length):
        print("game "+str(i)+ "started")
        Hands=HandGenerator(2)
        res,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy1),RandomHandSorter(Hands[1],Strategy2))
        if(res==1):
            scoreDict[Strategy1.__name__+"1"]+=1
        elif(res==2):
            scoreDict[Strategy2.__name__+"2"]+=1
        else:
            scoreDict["Ties"]+=1
        print("game "+str(i)+ "done")
        print(scoreDict)
    return(scoreDict)
    