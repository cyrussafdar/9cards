#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:55:24 2022

@author: cyrussafdar
"""
from Logic import *
from Display import *
import ast
with open('hash.txt') as f:
    data = f.read()

#Loading the dictionary
HashToNumbers = ast.literal_eval(data)

with open('Rank.txt') as f:
    data=f.read()
Rank=ast.literal_eval(data)
def CardToHash(Set_of_Cards):
    HashKeyGenerator(Set_of_Cards[0],Set_of_Cards[1],Set_of_Cards[2])
def ListToCards(ListOfCardNumbers):
    return [CARD(ListOfCardNumbers[0]),CARD(ListOfCardNumbers[1]),CARD(ListOfCardNumbers[2])]
def HashKeyGenerator(i,j,k):
    return i**5+j**5+k**5+i**5*j**5*k**5
def simplerHash(i,j,k):
    return i*10000+j*100+k
def HashtoCards(hashnumber):
    Cards=list()
    Cards.append(CARD(hashnumber//10000))
    Cards.append(CARD((hashnumber%10000)//100))
    Cards.append(CARD(hashnumber%100))
    return Cards
    
def HashTest(HashFunction):
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
                res=HashFunction(i,j,k)
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
    print(duplicateCount)
    
#    
#    for key in testset.keys():
#        testset[key]=Handrank(ListToCards(testset[key]))
#    with open('Rank.txt','w') as data: 
#      data.write(str(testset))    

def RankTest():
    for key in HashToNumbers.keys():
        print(Rank[key])