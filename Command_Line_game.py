#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:51:28 2022

@author: cyrussafdar
"""

#CommandLine Game
from Logic import *
from Display import *
from AI import*

from memory_profiler import profile   
   
#Hands=HandGenerator(2)

#Hand_print(Hands[0])
#Hands[0]=Hand_reorder(Hands[0],"3,4,5,6,1,2,7,8,0")
#Hand_print(Hands[0])
def Player_input_no_2nd_guessing(Hand,Player_No):
    #used for storing the original 
    Handdict={}
    for i in range(len(Hand)):
        Handdict[Hand[i].number]=str(i)
        order=""
    print("Player "+str(Player_No)+"'s Hand: ")
    Hand_print(Hand)
    print("Enter indices of first set separated by a ,")
    order+=input()
    handleft,Ordered_hand=Hand_popper(Hand,order)
    Hand_Order_progress(handleft,Ordered_hand)
        #a temporary variable to convert the indices of the unordered hand to
        #the original hands
    print("Enter indices of second set separated by a ,")
    temp_indices=input()
    temp_indices.strip()
    for i in temp_indices.split(","):
            #getting the original index of the card pointed to by the user
        order+=","
        order+=Handdict[handleft[(int)(i)].number]
        
    handleft,Ordered_hand=Hand_popper(Hand,order)
    Hand_Order_progress(handleft,Ordered_hand)
        
    for i in range(3):
            #getting the original index of the card pointed to by the user
        order+=","
        order+=Handdict[handleft[(int)(i)].number]
            
        
    handleft,Ordered_hand=Hand_popper(Hand,order)
    Ordered_hand=Set_Order_fixer_v2(Ordered_hand)
    Hand_Order_progress(handleft,Ordered_hand)
       
    return Ordered_hand
def Player_input_prompt(Hand,Player_No):
    
    #used for storing the original 
    Handdict={}
    for i in range(len(Hand)):
        Handdict[Hand[i].number]=str(i)
    while(True):
        order=""
        print("Player "+str(Player_No)+"'s Hand: ")
        Hand_print(Hand)
        print("Enter indices of first set separated by a ,")
        order+=input()
        handleft,Ordered_hand=Hand_popper(Hand,order)
        Hand_Order_progress(handleft,Ordered_hand)
        #a temporary variable to convert the indices of the unordered hand to
        #the original hands
        print("Enter indices of second set separated by a ,")
        temp_indices=input()
        temp_indices.strip()
        for i in temp_indices.split(","):
            #getting the original index of the card pointed to by the user
            order+=","
            order+=Handdict[handleft[(int)(i)].number]
        
        handleft,Ordered_hand=Hand_popper(Hand,order)
        Hand_Order_progress(handleft,Ordered_hand)
        
        for i in range(3):
            #getting the original index of the card pointed to by the user
            order+=","
            order+=Handdict[handleft[(int)(i)].number]
            
        
        handleft,Ordered_hand=Hand_popper(Hand,order)
        Ordered_hand=Set_Order_fixer_v2(Ordered_hand)
        Hand_Order_progress(handleft,Ordered_hand)
        print("Are you happy with hand thus far Y/N")
        yes_or_no=input().lower()
        print(dir())
        if(yes_or_no=='y' or yes_or_no=='z'):
            break
    return Ordered_hand

def Two_player_game_v2():
    input("Press Enter to start game")
    #Generate hands
    Hands=HandGenerator(2)
    P1_hand=Player_input_prompt(Hands[0],1)
    for i in range(6):
        print()
    print("pass it to Player 2")
    for i in range(6):
        print()
    print("Player 2 press enter")
    input()
    P2_hand=Player_input_prompt(Hands[1],2)
    
    print()
    print("Player 1's reordered hand: ")
    Hand_print(P1_hand)
    print()
    print("Player 2's reordered hand: ")
    Hand_print(P2_hand)
    
    #Result Print
    result,p1_points,p2_points=two_Player_winner(P1_hand,P2_hand)
    if(result==0):
        print("Kitty")
        return result,p1_points,p2_points
    elif(result==1):
        print("Player 1 wins")
        print(str(p1_points)+" hands to "+ str(p2_points))
        return result,p1_points,p2_points
    else:
        print("Player 2 wins")
        print(str(p2_points)+" hands to "+ str(p1_points))
        return result,p1_points,p2_points 
    
def Two_player_game():
    print("Press Enter to start game")
    input()
    #Generate hands
    Hands=HandGenerator(2)
    #set hand 
    Player_hand=Hands[0]
    print("Player 1's hand: ")
    Hand_print(Player_hand)
    position_print(9)
    print("Input the Order you want your cards")
    order=input()
    Player_hand=Hand_reorder(Player_hand,order)
    print("Player 1's reordered hand: ")
    Hand_print(Player_hand)
    #printing 12 spaces to make sure the cards cannot be seen
    for i in range(12):
        print()
    print("pass it to Player 2")
    print("Player 2 press enter")
    input()
    Player2_hand=Hands[1]
    print("Player 2's hand: ")
    Hand_print(Player2_hand)
    position_print()
    print("Input the Order you want your cards")
    order=input()
    Player2_hand=Hand_reorder(Player2_hand,order)
    print("Player 2's reordered hand: ")
    #Computer reorder function
    Hand_print(Player2_hand)
    
    print("Player 1's reordered hand: ")
    Hand_print(Player_hand)
    #result of 0 means a tie
    #result of 1 means the first hand won Player
    #result of 2 means the second hand won Computer
    result,p1_points,p2_points=two_Player_winner(Player_hand,Player2_hand)
    if(result==0):
        print("Kitty")
        return result,p1_points,p2_points
    elif(result==1):
        print("Player 1 wins")
        print(str(p1_points)+" hands to "+ str(p2_points))
        return result,p1_points,p2_points
    else:
        print("Player 2 wins")
        print(s7tr(p2_points)+" hands to "+ str(p1_points))
        return result,p1_points,p2_points   

def Computer_game():
    input("Press Enter to start game")
    #Generate hands
    Hands=HandGenerator(2)
    P1_hand=Player_input_no_2nd_guessing(Hands[0],1)
    for i in range(6):
        print()
    Computer_hand=DoubleStratAI(Hands[1])
    print("Player's hand")
    Hand_print(P1_hand)
    print("Computer's hand")
    Hand_print(Computer_hand)
    #Result Print
    result,p1_points,p2_points=two_Player_winner(P1_hand,Computer_hand)
    if(result==0):
        print("Kitty")
        return result,p1_points,p2_points
    elif(result==1):
        print("Player 1 wins")
        print(str(p1_points)+" hands to "+ str(p2_points))
        return result,p1_points,p2_points
    else:
        print("Player 2 wins")
        print(str(p2_points)+" hands to "+ str(p1_points))
        return result,p1_points,p2_points 

def Computer_V_Computer_game():
    input("Press Enter to start game")
    #Generate hands
    Hands=HandGenerator(2)
    P1_hand=DoubleStratAI(Hands[0])
    for i in range(6):
        print()
    Computer_hand=DoubleStratAI(Hands[1])
    print("Computer 1's hand")
    Hand_print(P1_hand)
    print("Computer 2's hand")
    Hand_print(Computer_hand)
    #Result Print
    result,p1_points,p2_points=two_Player_winner(P1_hand,Computer_hand)
    if(result==0):
        print("Kitty")
        return result,p1_points,p2_points
    elif(result==1):
        print("Computer 1 wins")
        print(str(p1_points)+" hands to "+ str(p2_points))
        return result,p1_points,p2_points
    else:
        print("Computer 2 wins")
        print(str(p2_points)+" hands to "+ str(p1_points))
        return result,p1_points,p2_points 

class Player(object):
    def __init__(self, hand, player_type,name):
        self.hand=hand
        self.player_type=player_type
        self.name=name
        self.hands=0
        self.total_hands=0
        self.points=0
        
    def identifier(self):
        return self.name+ " ("+self.player_type+")"
def PassToNextPlayer():
    for i in range(8):
        print()
    print("Pass it to the next Player")
    for i in range(2):
        print()
    print("Next player press Enter if ready")
    input()
    return
class Player_v2(object):
    def __init__(self,player_type,name):
        self.hand=122538112437102336
        self.player_type=player_type
        self.name=name
        self.total_hands=0
        self.points=0
        
    def identifier(self):
        return self.name+ " ("+self.player_type+")"
def Player_generate_prompt_v2():    
    default_Names=["Bill Gates","CEO of WB","Ratan Tata","Amitabh Bachhan","Bill Gates' son in law", "President of WB"] 
    print("How many Human players?")
    PlayerNo=(int)(input())
    print("How many computers?")
    CompNo=(int)(input())
    TotalPlayers=PlayerNo+CompNo
    print("Manually Enter names for Computer Y/N")
    if(input().lower()=='n'):
        not_confirm=False
        #Shuffling the default names
        random.shuffle(default_Names)                    
    else:
        not_confirm=True
    #list of player objects
    Players=list()
    #Creating players and populating their hands
    for i in range(TotalPlayers):
        if(i<PlayerNo):
            not_confirm=True
            while(not_confirm):
                print("Enter name for Player "+str(i+1))
                name=input()
                print(f"Happy with {name} Y/N")
                yesorno=input().lower()
                not_confirm=yesorno!="y"
            Players.append(Player_v2("Human",name))
        
        if(i<PlayerNo+CompNo and i>=PlayerNo):
            name=default_Names[i]
            Players.append(Player_v2("Computer",name))
    return Players,PlayerNo,CompNo
def Round_loop(Players,PlayerNo,CompNo):
    #Generate the list of Hashes for the Hands
    Hands=HandGeneratorHash(PlayerNo+CompNo)
    #how many hands won only relevant for a round
    HandsWon=[0]*(PlayerNo+CompNo)
    #Split up Computer processing before and after
    #if(CompNo)=2 then 1 and 1 if 3 then 2 and 1 if 4 then 3 and 1
    for j in range(PlayerNo,PlayerNo+CompNo-1):
        Players[j].hand=DoubleStratAI(Hashto9Cards(Hands[j]))
    for j in range(0,PlayerNo):
        #Player_input_prompt #Player_input_no_2nd_guessing
        Players[j].hand=Player_input_prompt(Hashto9Cards(Hands[j]),Players[j].name)
        if(j!=PlayerNo-1):
            PassToNextPlayer()
    #the last element which is always untouched
    Players[-1].hand=DoubleStratAI(Hashto9Cards(Hands[-1]))
    
    #Checking who wins the overall round
    for i in range(0,7,3):
        #For each 3 cards who wins
        HandList=[]
        for p in Players:
            #Prior to the Hand related text print out the hand
            if(i<3):
                print(p.name+" 's hand:")
                Hand_print(p.hand)
            HandList.append(p.hand[i:i+3])
            #Sort the hands by strength
        Order=Sorted_Hands(HandList)
        #print(HandList)
        #print(Order)
        if(betterSet(HandList[Order[0]],HandList[Order[1]])==0):
            print("Hand Tied")
        else:
            HandsWon[Order[0]]+=1
            print(Players[Order[0]].name+" wins hand "+str(int(i/3+1))+" with :")
            Hand_print(HandList[Order[0]])
            print()
            
    #At the end of it all
    windex=None
    for h in range(len(HandsWon)):
        if(HandsWon[h]>=2):
            windex=h
        Players[h].total_hands+=HandsWon[h]
    #winner
    return Players,windex
def Round_loop_test():
    Players=[Player_v2("Player","Cyrus"),Player_v2("Computer","Billy Gates 2"),Player_v2("Computer","Billy Gates 3"),Player_v2("Computer","Billy Gates 4"),Player_v2("Computer","Billy Gates 5")]
    PlayerNo=1
    CompNo=4
    Players=Round_loop(Players,PlayerNo,CompNo)
    for p in Players:
        print(p.name+" won "+str(p.total_hands)+ " hands")

def All_encompassing_Game():
    Players,PlayerNo,CompNo=Player_generate_prompt_v2()
    #To store the highest score so the exit condition can quickly be triggered
    highest_score=0
    #Keep Track of Player with highest score
    highest_score_index=0
    #To implement kitty scoring
    win_payout=1
    print("Best to ?")
    Best_to=(int)(input())
    Game_count=0
    while(highest_score<Best_to):
        Game_count+=1
        Players,windex=Round_loop(Players,PlayerNo,CompNo)
        if(windex==None):
            print("Kitty")
            win_payout+=1
        else:
            print(Players[windex].name+" wins")
            Players[windex].points+=win_payout
            #sets the highest
            if(Players[windex].points>highest_score):
                highest_score=Players[windex].points
                highest_score_index=windex
                
            win_payout=1
        
        #To add a break in between
        if(highest_score>=Best_to):
            print()
            print(Players[highest_score_index].name+ " wins with " + str(Players[highest_score_index].points)+" points")
            print("Press Enter to see a summary")
            input()
            print()
            print()
        else:
            print()
            print(Players[highest_score_index].name+" is leading, points: "+ str(Players[highest_score_index].points))
            print("Press Enter to continue")
            input()
        
    for p in Players:
        print(p.identifier()+" won "+str(p.points)+" points out of a total "+str(Game_count)+" and a total of "+str(p.total_hands)+" hands")
        print("Hands won percentage of "+ str(int(p.total_hands*100/(Game_count*3)))+"%")
        print("Points won percentage of "+ str(int(p.points*100/Game_count))+"%")
        print("Hands to points ratio of "+str(p.total_hands/p.points))
        print()
    
def Player_generate_prompt():
    default_Names=["Bill Gates","CEO of WB","Ratan Tata","Amitabh Bachhan","Bill Gates' son in law", "President of WB"] 
    print("How many Human players?")
    PlayerNo=(int)(input())
    print("How many computers?")
    CompNo=(int)(input())
    TotalPlayers=PlayerNo+CompNo
    Hands=HandGenerator(TotalPlayers)
    #list of player objects
    Players=list()
    
    print("Manually Enter names for Computer Y/N")
    if(input().lower()=='n'):
        not_confirm=False
        #Shuffling the default names
        random.shuffle(default_Names)                    
    else:
        not_confirm=True
    #Creating players and populating their hands
    for i in range(TotalPlayers):
        if(i<PlayerNo):
            not_confirm=True
            while(not_confirm):
                print("Enter name for Player "+str(i+1))
                name=input()
                print(f"Happy with {name} Y/N")
                yesorno=input().lower()
                not_confirm=yesorno!="y"
            Players.append(Player(Hands[i],"Human",name))
        
        if(i<PlayerNo+CompNo and i>=PlayerNo):
            name=default_Names[i]
            while(not_confirm):
                print("Enter name for Computer "+str(i-PlayerNo+2))
                name=input()
                print(f"Happy with {name} Y/N")
                yesorno=input().lower()
                not_confirm=yesorno!="y"
            Players.append(Player(Hands[i],"Computer",name))
    return Players
       
def Player_generate(PlayerNo,CompNo):
    default_Names=["Bill Gates","CEO of WB","Ratan Tata","Amitabh Bachhan","Bill Gates' son in law", "President of WB","Nibri Gaa's Husband"] 
    random.shuffle(default_Names)
    TotalPlayers=PlayerNo+CompNo
    Hands=HandGeneratorHash(TotalPlayers)
    #list of player objects
    Players=list()
    #Creating players and populating their hands
    for i in range(TotalPlayers):
        if(i<PlayerNo):
            not_confirm=True
            while(not_confirm):
                print("Enter name for Player "+str(i+1))
                name=input()
                print(f"Happy with {name} Y/N")
                yesorno=input().lower()
                not_confirm=yesorno!="y"
            
            Players.append(Player(Hands[i],"Human",name))
        if(i>=PlayerNo and i<PlayerNo+CompNo):
            name=default_Names[i]
            Players.append(Player(Hands[i],"Computer",name))
    return Players
def CustomisableGame():
    Players=Player_generate(1,4)
    
    print()
    print("Best to how many games?")
    Games=(int)(input())
    gameNo=0
    
    continueCondition=True
    #how much one gets for a win
    win_payout=1
    
    while(continueCondition):
        gameNo+=1
        for p in Players:
            if(p.player_type=='Human'):
                
                p.hand=CardsToHash(Player_input_no_2nd_guessing(Hashto9Cards(p.hand),p.name))
                print(dir())
                #print(Players[])
            else:
                p.hand=CardsToHash(DoubleStratAI(Hashto9Cards(p.hand)))
                print(p.name+"'s hand :")
                Hand_print(Hashto9Cards(p.hand))
                print(dir())
        #First hand logic
        for p in Players:
            #resetting hands won
            p.hands=0
        for i in range(0,7,3):
            HandList=[]
            for p in Players:
                HandList.append(Hashto9Cards(p.hand)[i:i+3])
            #Sort the hands by strength
            Order=Sorted_Hands(HandList)
            if(betterSet(HandList[Order[0]],HandList[Order[1]])==0):
                print("Hand Tied")
            else:
                Players[Order[0]].hands+=1
                Players[Order[0]].total_hands+=1
                print(Players[Order[0]].name+" wins hand")
        isThereWinner=False
        winner=None
        Hands=HandGeneratorHash(len(Players))
        j=0
        for p in Players:
            #allocating the new hands to the players
            p.hand=Hands[j]
            if(p.hands>=2):
                isThereWinner=True
                winner=p
            j+=1
            
        if(isThereWinner):
            print(winner.name+" wins Game number "+(str)(gameNo))
            winner.points+=win_payout
            win_payout=1
        else:
            print("Kitty")
            win_payout+=1
        #Checks if any player has surpassed the point threshold
        for p in Players:
            continueCondition= continueCondition and (p.points<Games)
    #print("reaches end of loop")
    for p in Players:
        print("Gets here")
        if(p.points>=Games):
            print(p.name+ "wins with " +(str)(p.points)+" points")
                
def Start_Series(Game_no,GameType):
    P1_wins=0
    P1_hands_won=0
    P2_wins=0
    P2_hands_won=0
    #a Kitty increases the payout by 1
    win_payout=1
    #Game number
    game_no=1
    while(P1_wins<Game_no and P2_wins<Game_no):
        print("Game "+str(game_no)+": ")
        result,P1_set,P2_set=GameType()
        P1_hands_won+=P1_set
        P2_hands_won+=P2_set
        if(result==0):
            win_payout+=1
        else:
            if(result==1):
                P1_wins+=win_payout
            if(result==2):
                P2_wins+=win_payout
            win_payout=1
        print("Player 1 score: "+str(P1_wins))
        print("Player 2 score: "+str(P2_wins))
        print()
        print("Total hands won by Player 1: " +str(P1_hands_won))
        print("Total hands won by Player 2: " +str(P2_hands_won))
        #incrementing the game number
        game_no+=1
    if(P1_wins>P2_wins):
        print("Player 1 wins series")
        print(str(P1_wins)+" to "+str(P2_wins))
    else:
        print("Player 2 wins series")
        print(str(P2_wins)+" to "+str(P1_wins))
        
    


    