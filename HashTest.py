#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:55:24 2022

@author: cyrussafdar
"""
from Logic import *
from Display import *
import ast


#with open('Rank.txt') as f:
#    data=f.read()
#Rank=ast.literal_eval(data)
def simplerHash(i,j,k):
    nums=[i,j,k]
    nums.sort(reverse=True)
    return nums[2]*10000+nums[1]*100+nums[0]
def CardsToHash(Card_set):
    mult=1
    HashNumber=0
    for card in Card_set:
        HashNumber+=card.number*mult
        mult*=100
    return HashNumber
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
    
def RankPopulator():
    testset=dict()
    distinctHands=list()
    duplicateCount=0
    for i in range(52):
        for j in range(52):
            if(j==i):
                continue
            for k in range(52):
                if(k==i or k==j):
                    continue
                res=simplerHash(i,j,k)
                if(res in testset):
                    if(i in testset[res] and j in testset[res] and k in testset[res]):
                        continue
                    else:
                        #print(f"{res} is a duplicate")
                        #print(testset[res])
                        #print([i,j,k])
                        duplicateCount+=1
                else:
                    testset[res]=[i,j,k]
                    distinctHands.append([i,j,k])
    
   
    for key in testset.keys():
        testset[key]=Handrank_Orderless(Hashto3Cards(key))
    with open('Rank.txt','w') as data: 
      data.write(str(testset))    

def RankTest():
    for key in HashToNumbers.keys():
        print(Rank[key])