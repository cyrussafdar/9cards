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
  
def Player_input_prompt(Hand,Player_No,Total_Players):
    Handdict={}
    for i in range(len(Hand)):
        Handdict[Hand[i].number]=str(i)
    while(True):
        order=""
        print("Player "+str(Player_No)+"'s Hand: ")
        
        tentative_text=""
        while(not is_valid_order_input(tentative_text,9)):
            Hand_print(Hand)
            print("Enter indices of first set separated by a ,")
            print("Format: i,j,k")
            tentative_text=input()
        order+=tentative_text
        #resetting tentative text for the next loop
        tentative_text=""
        handleft,Ordered_hand=Hand_popper(Hand,order)
        
        #a temporary variable to convert the indices of the unordered hand to
        #the original hands
        while(not is_valid_order_input(tentative_text,6)):
            Hand_Order_progress(handleft,Ordered_hand)
            print("Enter indices of second set separated by a ,")
            print("Format: i,j,k")
            tentative_text=input()
        temp_indices=tentative_text
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
        if(yes_or_no=='y' or yes_or_no=='z'):
            break
    with open('PlayerHandData'+str(Total_Players)+'.txt','a') as data: 
      data.write(f"{CardsToHash(Hand)}:{CardsToHash(Ordered_hand)}\n")    
    return Ordered_hand
def Player_input_prompt_v2(Player,Total_Players):
    Hand=Hashto9Cards(Player.hand)
    Hand_print(Hand)
    FourOKCard=has_four_of_a_kind(Hand)
    FourPairIndices=hasFourPair(Hand)
    if(FourOKCard!=-1):
        #logic
        print("You have a four of a kind would you like to claim a win? Y/N")
        WinClaim=input().lower()
        if(WinClaim=='y' or WinClaim=='z'):
            Player.four_of_a_kind=FourOKCard
        else:
            #setting the number to -1
            Player.four_of_a_kind=-1
        
    elif(len(FourPairIndices)==16):
        #logic
        print("You have four pairs would you like to claim a tie? Y/N")
        TieClaim=input().lower()
        if(TieClaim=='y' or WinClaim=='z'):
            Player.pair_indices=FourPairIndices
        else:
            #setting the number to -1
            Player.pair_indices=""
    
    Handdict={}
    for i in range(len(Hand)):
        Handdict[Hand[i].number]=str(i)
    while(True):
        order=""
        print("Player "+str(Player_No)+"'s Hand: ")
        
        tentative_text=""
        while(not is_valid_order_input(tentative_text,9)):
            Hand_print(Hand)
            print("Enter indices of first set separated by a ,")
            print("Format: i,j,k")
            tentative_text=input()
        order+=tentative_text
        #resetting tentative text for the next loop
        tentative_text=""
        handleft,Ordered_hand=Hand_popper(Hand,order)
        
        #a temporary variable to convert the indices of the unordered hand to
        #the original hands
        while(not is_valid_order_input(tentative_text,6)):
            Hand_Order_progress(handleft,Ordered_hand)
            print("Enter indices of second set separated by a ,")
            print("Format: i,j,k")
            tentative_text=input()
        temp_indices=tentative_text
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
        if(yes_or_no=='y' or yes_or_no=='z'):
            break
    with open('PlayerHandData'+str(Total_Players)+'.txt','a') as data: 
      data.write(f"{CardsToHash(Hand)}:{CardsToHash(Ordered_hand)}\n")    
    return Ordered_hand
def is_valid_order_input(order_input,upper_bound):
    if(len(order_input)==0):
        return False
    if(len(order_input)!=5):
        print("input too long or short")
        return False
    #check if the commas are in the right spot
    if(order_input[1]!=',' or order_input[3]!=','):
        print("Comma(,) not in the right spot or no commas(,) at all")
        return False
    if((int)(order_input[0])>=upper_bound):
        print("index "+order_input[0]+" is out of bounds")
        return False
    if((int)(order_input[2])>=upper_bound):
        print("index "+order_input[2]+" is out of bounds")
        return False
    if((int)(order_input[4])>=upper_bound):
        print("index "+order_input[4]+" is out of bounds")
        return False
    
    return True

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
        self.four_of_a_kind=-1
        self.pair_indices=""
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
    TotalPlayers=PlayerNo+CompNo
    #Generate the list of Hashes for the Hands
    Hands=HandGeneratorHash(TotalPlayers)
    #how many hands won only relevant for a round
    HandsWon=[0]*(TotalPlayers)
    #Split up Computer processing before and after
    #if(CompNo)=2 then 1 and 1 if 3 then 2 and 1 if 4 then 3 and 1
    for j in range(PlayerNo,PlayerNo+CompNo-1):
        Players[j].hand=RandomHandSorter(Hashto9Cards(Hands[j]),MiddleHeavyHandValue)
    for j in range(0,PlayerNo):
        #Player_input_prompt #Player_input_no_2nd_guessing
        Players[j].hand=Player_input_prompt(Hashto9Cards(Hands[j]),Players[j].name,TotalPlayers)
        if(j!=PlayerNo-1):
            PassToNextPlayer()
    #the last element which is always untouched
    Players[-1].hand=RandomHandSorter(Hashto9Cards(Hands[-1]),MiddleHeavyHandValue)
    
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
        if(p.points!=0):
            print("Hands to points ratio of "+str(p.total_hands/p.points))
        print()
    

