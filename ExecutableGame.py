#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 04:14:31 2022

@author: cyrussafdar
"""

from Command_Line_game import *
print("Against Computer (C) or a Player (P)")
GameMode=input().lower()
print("How many games do you want to play")
number=(int)(input())
if(GameMode=="c"):
    Start_Series(number,Computer_game)
else:
    Start_Series(number,Two_player_game_v2)