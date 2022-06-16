#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:54:00 2022

@author: cyrussafdar
"""
from Logic import *
#A of hearts 2 of hearts 3 of hearts
StraightFlush=[CARD(12),CARD(0),CARD(1)]
differentSuitsameSFLUSH=[CARD(25),CARD(13),CARD(14)]
#2 of hearts 3 of hearts 4 of hearts
LowerStraightFlush=[CARD(2),CARD(0),CARD(1)]

#5 of spades, 5 of hearts, 5 of dice
ThreeofAkind=[CARD(3),CARD(16),CARD(29)]
#2 of spades, 2 of hearts, 2 of dice
LowerThreeofAkind=[CARD(0),CARD(13),CARD(26)]
#A of hearts 2 of spades 3 of spades
Straight=[CARD(25),CARD(0),CARD(1)]
# K of hearts Q of hearts J of spades
LowerStraight=[CARD(24),CARD(23),CARD(9)]
# 2 of spades, 2 of hearts, 4 of spades
Pair=[CARD(0),CARD(13),CARD(2)]
# K of spades, K of hearts, 4 of spades
Mid_pair=[CARD(11),CARD(24),CARD(2)]
# A of spades, A of hearts, 4 of spades
High_pair=[CARD(12),CARD(25),CARD(2)]
# A of spades, A of hearts, 6 of spades
Higher_pair_by_card=[CARD(12),CARD(25),CARD(4)]
Nothing=[CARD(0),CARD(16),CARD(2)]
Different_Suit_Nothing=[CARD(26),CARD(29),CARD(41)]

Player1Hand=ThreeofAkind+LowerThreeofAkind+Pair
Player2Hand=LowerThreeofAkind+High_pair+Mid_pair

#Testing code

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
def GeneratedHandTest(Hands):
    for hand in Hands:
        print("Hand:\n")
        for card in hand:
            card.Print()
            print()
def PlayerTest():
    Players=Player_generate_prompt_v2()
    for p in Players:
        print(p.identifier())
        