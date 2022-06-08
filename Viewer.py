#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 01:21:51 2022

@author: cyrussafdar
"""

import pygame, sys
from pygame.locals import *
from Logic import *
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
        
# Setting up color objects
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE= (255,255,255)

Screenwidth=500
Screenheight=750
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((Screenwidth,Screenheight))
DISPLAYSURF.fill(WHITE)
# Display background Image
pygame.display.set_caption("Example")
Card_width=Screenwidth/300*32

def displayCard(card_number,x_pos,y_pos,width,height):
    #returns loaded image
    filename=str(card_number)+".png"
    picture = pygame.image.load(filename)
    picture=pygame.transform.smoothscale(picture,((int)(width),(int)(height)))
    Temp_rect=picture.get_rect()
    Temp_rect.center=x_pos,y_pos
    DISPLAYSURF.blit(picture,Temp_rect)
def displayBackofCard(x_pos,y_pos,width,height):
    #returns loaded image
    filename="back.png"
    picture = pygame.image.load(filename)
    picture=pygame.transform.smoothscale(picture,((int)(width),(int)(height)))
    Temp_rect=picture.get_rect()
    Temp_rect.center=x_pos,y_pos
    DISPLAYSURF.blit(picture,Temp_rect)
    #images.append((picture,Temp_rect))
def Handdisplay(Hand,x_pos,y_pos,width):
    for c in range(9):
        displayCard(Hand[c].number,x_pos+(width+1)*c,y_pos,width,width*1.3)
def ObscuredHanddisplay(x_pos,y_pos,width):
    for c in range(9):
        displayBackofCard(x_pos+(width+1)*c,y_pos,width,width*1.3)

Hands=HandGenerator(2)
#Displaying opponents hands backwards
ObscuredHanddisplay(Screenwidth*20/300,Screenheight*1/3,Card_width)
Handdisplay(Hands[0],Screenwidth*20/300,Screenheight*1/3+1.4*Card_width,Card_width)
Handdisplay(Hands[1],Screenwidth*20/300,Screenheight*2.2/3,Card_width)

# Beginning Game Loop
while True:
    pygame.display.update()
    #for picture,rect in images:
        #DISPLAYSURF.blit(picture,rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)
