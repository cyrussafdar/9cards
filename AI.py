#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:30:18 2022

@author: cyrussafdar
"""
from Logic import *
from Display import*
from Command_Line_game import*
import math
import random
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
with open('HandWinProbability.txt') as f:
    data=f.read()
probs=ast.literal_eval(data)
def Set_Win_prob(Card_set):
    return probs[HashedHandRank(Card_set)]
def Hand_Win_prob(Hand):
    #each probability represents the probability of each part of the hand winning
    prob_1=Set_Win_prob(Hand[0:3])
    prob_2=Set_Win_prob(Hand[3:6])
    prob_3=Set_Win_prob(Hand[6:9])
    
    return prob_1*prob_2+prob_1*prob_3+prob_2*prob_3-2*prob_1*prob_2*prob_3

def Smarter_Hand_Win_prob(Hand):
    #each probability represents the probability of each part of the hand winning
    first_hand_value=HashedHandRank(Hand[0:3])
    second_hand_value=HashedHandRank(Hand[3:6])
    if(first_hand_value not in Subjective_Hand.keys() or second_hand_value not in Subjective_Hand.keys()):
        prob_1=0
        prob_2=0
        prob_3=0
    else:   
        prob_1=Subjective_Hand[first_hand_value]
        prob_2=Subjective_Hand[second_hand_value]
        prob_3=Set_Win_prob(Hand[6:9])
    # -3 means clean sweeps are completely ignored -2 is the normal math
    #prob_1*prob_2+prob_1*prob_3+prob_2*prob_3-2*prob_1*prob_2*prob_3
    return prob_1+prob_2+prob_3

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

def RanktoNormalisedFeatures(Rank):
    """Input: A float rank of the form x.0abcdef where x indicates what kind of a hand it is
    Outputs: Normalised vectors that indicate a broad range of features about the hand"""
    kindofHandMatrix=[0]*6
    positionalvalue=0
    if(Rank<1):
        kindofHandMatrix[0]=1
        positionalvalue=Rank
    elif(Rank<2):
        kindofHandMatrix[1]=1
        positionalvalue=Rank
    elif(Rank<3):
        kindofHandMatrix[2]=1
        positionalvalue=Rank-2
    elif(Rank<4):
        kindofHandMatrix[3]=1
        positionalvalue=Rank-3
    elif(Rank<5):
        kindofHandMatrix[4]=1
        positionalvalue=Rank-4
    else:
        kindofHandMatrix[5]=1
        positionalvalue=Rank-5
    #positionalvalue should range from 0.000001 to 0.0121212
    positionalvalue=positionalvalue/0.0121212
    return kindofHandMatrix,positionalvalue

with open('SubjectiveHandWinProbability.txt') as f:
    data=f.read()    
Subjective_Hand=ast.literal_eval(data)
def TruncatedProbabilityFixer():
    for key in Subjective_Hand.keys():
        Subjective_Hand[key]=Subjective_Hand[key]/0.2560633484162896
    with open('SubjectiveHandWinProbability.txt','w') as data: 
      data.write(str(Subjective_Hand)) 
with open('Features.txt') as f:
    data=f.read()
Features=ast.literal_eval(data)
def RanktoNormalisedFeaturesCache(Rank):
    """Input: A float rank of the form x.0abcdef where x indicates what kind of a hand it is
    Outputs: Normalised vectors that indicate a broad range of features about the hand"""
    return Features[Rank]

def RanktoSimplerNormalisedFeatures(Rank):
    """Input: A float rank of the form x.0abcdef where x indicates what kind of a hand it is
    Outputs: Normalised vectors that indicate a broad range of features about the hand"""
    
    #positionalvalue should range from 0.000001 to 0.0121212
    positionalvalue=math.fmod(Rank,1)/0.0121212
    HandValue=(Rank-positionalvalue)/5
    return HandValue,positionalvalue    
def ComplexValue(Hand):
    #w1,w2,w3
    value=0
    ## [0] is weight of kindofHandMatrix
    ##[1] is weight of positionalvalue
    ##[2] is the weight of a Top Card
    ##[3] is a weight of a Pair
    ##[4] is a weight of a Flush
    ##[5] is the weight of a Straight
    ##[6] is the weight of a Straight Flush
    ##[7] is the weight of a Three of a kind
    w1=[0.999,0.001,0.0,0.02,0.1,0.21,0.28,0.36]
    w2=[0.999,0.001,0.0,0.06,0.13,0.2,0.26,0.33]
    w3=[0.5,0.0005,0.00,0.1,0.3,0.6,0,0]
    position_weight=[[1,1.5,2,1.4,1.2,1.1],[1.8,2,2.7,1.4,1,1],[2.3,3,2,1,0,0]]
    weights=[w1,w2,w3]
    
    kindofHandMatrix=[0]*3
    position=[0]*3
    for i in range(0,7,3):
        kindofHandMatrix[int(i/3)],position[int(i/3)]=RanktoNormalisedFeaturesCache(HashedHandRank(Hand[i:i+3]))
        
    for j in range(3):
        for i in range(2,8):
            value+=kindofHandMatrix[j][i-2]*weights[j][i]*weights[j][0]
        value+=position[j]*weights[j][1]
        
    return value
def SimplerComplexValue(Hand):
    #w1,w2,w3
    value=0
    ## [0] is weight of kindofHandMatrix
    ##[1] is weight of positionalvalue
    ##[2] is the weight of a Top Card
    ##[3] is a weight of a Pair
    ##[4] is a weight of a Flush
    ##[5] is the weight of a Straight
    ##[6] is the weight of a Straight Flush
    ##[7] is the weight of a Three of a kind
    w1=[0.99,0.01,0.0,0.05,0.1,0.15,0.3,0.4]
    w2=[0.99,0.01,0.0,0.05,0.1,0.15,0.3,0.4]
    w3=[0.99,0.01,0.0,0.05,0.1,0.15,0.3,0.4]
    weights=[w1,w2,w3]
    kindofHandMatrix_1,position_1=RanktoNormalisedFeatures(HashedHandRank(Hand[0:3]))
    kindofHandMatrix_2,position_2=RanktoNormalisedFeatures(HashedHandRank(Hand[3:6]))
    kindofHandMatrix_3,position_3=RanktoNormalisedFeatures(HashedHandRank(Hand[6:9]))
    
    kindofHandMatrix=[0]*3
    position=[0]*3
    for i in range(0,7,3):
        kindofHandMatrix[int(i/3)],position[int(i/3)]=RanktoNormalisedFeatures(HashedHandRank(Hand[i:i+3]))
        
    for j in range(3):
        for i in range(2,8):
            value+=kindofHandMatrix[j][i-2]*weights[j][i]*weights[j][0]
        value+=position[j]*weights[j][1]
        
    return value
def ComplexAI(Hand):
    #I will normalise all the decision values so the AI can identify what decision to make
    #the features that will be included will be IsThreeOfAKind, 
    BestHand=Set_Order_fixer_v2(Hand)
    BestValue=ComplexValueFunction(Hand)
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


def AIheadtohead(Strategy1,Strategy2,series_num,series_length):
    scoreDict=dict()
    for j in range(series_num):
        scoreDict[Strategy1.__name__+" "+str(j)]=0
        scoreDict[Strategy2.__name__+" "+str(j)+"'"]=0
        scoreDict["Ties "+str(j)]=0
#        strat1=[]
#        strat2=[]
#        ties=[]
#        gameNo=[]
        #csvstring=Strategy1.__name__+","+Strategy2.__name__+"2"+","+"Ties"+"\n"
        for i in range(series_length):
#            gameNo.append(i)
            print("game "+str(i)+ "started")
            Hands=HandGenerator(2)
            res,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy1),RandomHandSorter(Hands[1],Strategy2))
            #res,dum,dum=two_Player_winner(RandomHandSorter(Hands[0],Strategy1),Set_Order_fixer_v2(Hands[1]))
            if(res==1):
                scoreDict[Strategy1.__name__+" "+str(j)]+=1
            elif(res==2):
                scoreDict[Strategy2.__name__+" "+str(j)+"'"]+=1
            else:
                scoreDict["Ties "+str(j)]+=1
            print("game "+str(i)+ "done")
            #csvstring+=str(scoreDict[Strategy1.__name__+"1"])+","+str(scoreDict[Strategy2.__name__+"2"])+","+str(scoreDict["Ties"])+"\n"
#            strat1.append(scoreDict[Strategy1.__name__+"1"]/len(gameNo))
#            strat2.append(scoreDict[Strategy2.__name__+"2"]/len(gameNo))
#            ties.append(scoreDict["Ties"]/len(gameNo))
            #print(scoreDict)
        #Z score
#        Z=(np.mean(strat1)-np.mean(strat2))/math.sqrt(np.var(strat1)+np.var(strat2))
#        plt.plot(gameNo,ties, label = "Ties")
#        plt.plot(gameNo,strat1, label = Strategy1.__name__)
#        plt.plot(gameNo,strat2, label = Strategy2.__name__)
#        print(Z)
#        plt.legend()
#        plt.show()
        #with open(Strategy1.__name__+' v '+Strategy2.__name__+".csv",'a') as data: 
        #  data.write(str(csvstring))    
    return(scoreDict)

def AIheadtoheadagainstAnother(Strategy1,Strategy2,Strategy3,series_length):
    scoreDict=dict()
    scoreDict[Strategy1.__name__+" Win"]=0
    scoreDict[Strategy1.__name__+" Ties"]=0
    scoreDict[Strategy2.__name__+" Win"]=0
    scoreDict[Strategy2.__name__+" Ties"]=0
    for i in range(series_length):
        #print("game "+str(i)+ "started")
        Hands=HandGenerator(2)
        Strategy3Hand=RandomHandSorter(Hands[1],Strategy3)
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


StrategySuite=[]

        