#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:12:30 2022

@author: cyrussafdar
"""

from colorama import Fore

def Hand_Order_progress(unordered_hand,ordered_hand):
   print("Hand thus far :")
   Hand_print(ordered_hand)
   print()
   if(len(unordered_hand)!=0):
       print("Unordered Hand:")
       Hand_print(unordered_hand)
       print()
       
def Hand_print(Hand):
    top_border="_"+len(Hand)*("_")*5
    second_layer="|"+len(Hand)*"    |"
    last_layer="|"+len(Hand)*"____|"
    print(Fore.BLACK+top_border)
    print(Fore.BLACK+second_layer)
    handstring=Fore.BLACK+"|"
    for card in Hand:
        handstring+=" "
        handstring+=card.text()
        if(card.Card==8):
            handstring+=Fore.BLACK+"|"
        else:
            handstring+=Fore.BLACK+" |"
    print(handstring)
    print(Fore.BLACK+last_layer)
    position_print(len(Hand))

def position_print(number):
    print_string=Fore.BLACK+" "
    for i in range(number):
        print_string+="  "+str(i)+"  "
    print(print_string)