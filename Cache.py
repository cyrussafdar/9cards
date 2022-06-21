#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:38:46 2022

@author: cyrussafdar
"""
import ast
Cache={
       "Rank":{},
       "Orders":{},
       "probs":{},
       "Features":{},
       "Subjective_Hand":{}
       }
with open('Rank.txt') as f:
    data=f.read()
Cache["Rank"]=ast.literal_eval(data)

with open('Orders.txt') as f:
    data=f.read()
Cache["Orders"]=ast.literal_eval(data)

with open('HandWinProbability.txt') as f:
    data=f.read()
Cache["probs"]=ast.literal_eval(data)

with open('Features.txt') as f:
    data=f.read()
Cache["Features"]=ast.literal_eval(data)

with open('SubjectiveHandWinProbability.txt') as f:
    data=f.read()
Cache["Subjective_Hand"]=ast.literal_eval(data)


