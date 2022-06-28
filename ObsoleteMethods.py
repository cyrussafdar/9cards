#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:55:44 2022

@author: cyrussafdar
"""
from Test import*
def winning_hand(Hand_1,Hand_2):
    p1_points=0
    p2_points=0
    #Show cards
    i=0
    #This loop might be triggered by a mutual agreement to show or a timer
    while(i<7):
        if(betterSet(Hand_1[i:i+3],Hand_2[i:i+3])==1):
            p1_points+=1
        elif(betterSet(Hand_1[i:i+3],Hand_2[i:i+3])==2):
            p2_points+=1
        i+=3
    if(p1_points>p2_points):
        return Hand_1
    else:
        return Hand_2
def DoubleStratAI(Hand):
    Bottom=RandomHandSorter(Hand,BottomHeavyHandValue)
    Top=RandomHandSorter(Hand,TopHeavyHandValue)
    return winning_hand(Top,Bottom)
def FeaturePopulator(Rank):
    """Input: A float rank of the form x.0abcdef where x indicates what kind of a hand it is
    Outputs: Normalised vectors that indicate a broad range of features about the hand"""
    results=dict()
    for key in Rank.keys():
        val=HashedHandRank(Hashto3Cards(key))
        kindofHandMatrix=[0]*6
        positionalvalue=0
        if(val<1):
            kindofHandMatrix[0]=1
            positionalvalue=val
        elif(val<2):
            kindofHandMatrix[1]=1
            positionalvalue=val-1
        elif(val<3):
            kindofHandMatrix[2]=1
            positionalvalue=val-2
        elif(val<4):
            kindofHandMatrix[3]=1
            positionalvalue=val-3
        elif(val<5):
            kindofHandMatrix[4]=1
            positionalvalue=val-4
        else:
            kindofHandMatrix[5]=1
            positionalvalue=val-5
        #positionalvalue should range from 0.000001 to 0.0121212
        positionalvalue/=0.0121212
        results[val]= kindofHandMatrix,positionalvalue
    with open('Features.txt','w') as data: 
      data.write(str(results)) 
def ProbabilityPopulator():
    """Gets the probability of a rank winning"""
    results=dict()
    for key1 in Rank.keys():
        count=0
        val=HashedHandRank(Hashto3Cards(key1))
        for key2 in Rank.keys():
            if(key1!=key2):
                #if val 
                if(val>HashedHandRank(Hashto3Cards(key2))):
                    count+=1
        results[val]=count/len(Rank)
        
        #positionalvalue should range from 0.000001 to 0.0121212
        
    with open('HandWinProbability.txt','w') as data: 
      data.write(str(results))    
def TruncatedProbabilityPopulator():
    """Input: A float rank of the form x.0abcdef where x indicates what kind of a hand it is
    Outputs: Normalised vectors that indicate a broad range of features about the hand"""
    #Change it to pair and above
    results=dict()
    total_count=0
    for key1 in Rank.keys():
        count=0
        val=HashedHandRank(Hashto3Cards(key1))
        if(val<1):
            continue
        for key2 in Rank.keys():
            if(key1!=key2):
                #if val 
                val2=HashedHandRank(Hashto3Cards(key2))
                if(val2<1):
                    continue
                total_count+=1
                if(val>=val2):
                    count+=1
        results[val]=count/total_count
        
        #positionalvalue should range from 0.000001 to 0.0121212
        
    with open('PairandAboveHandWinProbability.txt','w') as data: 
      data.write(str(results))   
      
def Null_Hypothesis(series_length):
    scoreDict={"No strat 1":0,"No strat 2":0,"Ties":0}
    strat1=[]
    strat2=[]
    ties=[]
    gameNo=[]
    csvstring="No strat,"+"No strat 2"+","+"Ties"+"\n"
    for i in range(series_length):
        gameNo.append(i)
        print("game "+str(i)+ "started")
        Hands=HandGenerator(2)
        res,dum,dum=two_Player_winner(Set_Order_fixer_v2(Hands[0]),Set_Order_fixer_v2(Hands[1]))
        if(res==1):
            scoreDict["No strat 1"]+=1
        elif(res==2):
            scoreDict["No strat 2"]+=1
        else:
            scoreDict["Ties"]+=1
        print("game "+str(i)+ "done")
        csvstring+=str(scoreDict["No strat 1"])+","+str(scoreDict["No strat 2"])+","+str(scoreDict["Ties"])+"\n"
        strat1.append(scoreDict["No strat 1"]/len(gameNo))
        strat2.append(scoreDict["No strat 2"]/len(gameNo))
        ties.append(scoreDict["Ties"]/len(gameNo))
        #print(scoreDict)
    plt.plot(gameNo,ties, label = "Ties")
    plt.plot(gameNo,strat1, label = "No strat 1")
    plt.plot(gameNo,strat2, label = "No strat 2")
    plt.legend()
    plt.show()
    with open("No strat"+' v '+"No strat"+".csv",'a') as data: 
      data.write(str(csvstring))    
    return(scoreDict)

def StratAgainstNoStrat(Strategy,series_length):
    scoreDict={"No strat":0,Strategy.__name__:0,"Ties":0}
    strat1=[]
    strat2=[]
    ties=[]
    gameNo=[]
    csvstring="No strat,"+Strategy.__name__+","+"Ties"+"\n"
    for i in range(series_length):
        gameNo.append(i)
        print("game "+str(i)+ "started")
        Hands=HandGenerator(2)
        res,dum,dum=two_Player_winner(Set_Order_fixer_v2(Hands[0]),RandomHandSorter(Hands[1],Strategy))
        if(res==1):
            scoreDict["No strat"]+=1
        elif(res==2):
            scoreDict[Strategy.__name__]+=1
        else:
            scoreDict["Ties"]+=1
        print("game "+str(i)+ "done")
        csvstring+=str(scoreDict["No strat"])+","+str(scoreDict[Strategy.__name__])+","+str(scoreDict["Ties"])+"\n"
        strat1.append(scoreDict["No strat"]/len(gameNo))
        strat2.append(scoreDict[Strategy.__name__]/len(gameNo))
        ties.append(scoreDict["Ties"]/len(gameNo))
        #print(scoreDict)
    plt.plot(gameNo,ties, label = "Ties")
    plt.plot(gameNo,strat1, label = "No strat")
    plt.plot(gameNo,strat2, label = Strategy.__name__)
    plt.legend()
    plt.show()
    with open("No strat"+'_v_'+Strategy.__name__+".csv",'a') as data: 
      data.write(str(csvstring))    
    return(scoreDict)
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
                #print(Players[])
            else:
                p.hand=CardsToHash(DoubleStratAI(Hashto9Cards(p.hand)))
                print(p.name+"'s hand :")
                Hand_print(Hashto9Cards(p.hand))
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

def Two_player_game_v2():
    input("Press Enter to start game")
    #Generate hands
    Hands=HandGenerator(2)
    P1_hand=Player_input_prompt(Hands[0],1,2)
    for i in range(6):
        print()
    print("pass it to Player 2")
    for i in range(6):
        print()
    print("Player 2 press enter")
    input()
    P2_hand=Player_input_prompt(Hands[1],2,2)
    
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

def Handrank(Card_set):
        #Takes a set of 3 cards and returns its 
        Card_count=[0]*13
        Suit_count=[0]*4
        Comparing_Order=[]
        #Slight nuance for pairs the pair should be compared first for others a 
        #list sorted in descending order is fine
        colour=False
        straight=False
        for card in Card_set:
            Card_count[card.Card]+=1
            Comparing_Order.append(card.Card)  
            if(Card_count[card.Card]==3):
                #condition for it being three of a kind
                return 5, Comparing_Order
            Suit_count[card.Suit_num]+=1
            if(Suit_count[card.Suit_num]==3):
                colour=True
        
        Comparing_Order.sort(reverse=True)
        #print(Comparing_Order)
        #The case where two numbers are the same and sorted with the pair first
        if(Comparing_Order[0]==Comparing_Order[1]):
            return 1,Comparing_Order
        #The case where theres pairs and theyre sorted with the pair second
        if(Comparing_Order[1]==Comparing_Order[2]):
            return 1,[Comparing_Order[1],Comparing_Order[2],Comparing_Order[0]]
        
            
        if(Comparing_Order[0]-1==Comparing_Order[1] and 
           Comparing_Order[1]-1== Comparing_Order[2]):
            straight=True
        if(Comparing_Order[0]==12 and Comparing_Order[1]==1 and Comparing_Order[2]==0):
            straight=True
        
        if(straight and colour):
            return 4,Comparing_Order
        elif(straight):
            return 3,Comparing_Order
        elif(colour):
            return 2,Comparing_Order
        else:
            return 0,Comparing_Order
def Set_Order_fixer(Hand):
    """Input: Takes in a Hand and 
    Output: Hand sorted by sets largest rank """
    #using bubble sort because hands need to be compared to understand the value
    sets=list()
    for i in range(0,8,3):
        sets.append(Hand[i:i+3])
    swap_flag=True
    while(swap_flag):
        swap_flag=False
        for i in range(2):
            if(betterSet(sets[i],sets[i+1])!=1):
                temp=sets[i]
                sets[i]=sets[i+1]
                sets[i+1]=temp
                swap_flag=True
    
    sortedHand=sets[0]
    sortedHand.extend(sets[1])  
    sortedHand.extend(sets[2])      
    return sortedHand

def Handrank_v2(Card_set):
        #Takes a set of 3 cards and returns its 
        Card_count=[0]*13
        Suit_count=[0]*4
        Comparing_Order=[]
        #Slight nuance for pairs the pair should be compared first for others a 
        #list sorted in descending order is fine
        colour=False
        straight=False
        for card in Card_set:
            Card_count[card.Card]+=1
            Comparing_Order.append(card.Card)  
            if(Card_count[card.Card]==3):
                #condition for it being three of a kind
                return 5+CardsToHash([CARD(Comparing_Order[0]),CARD(Comparing_Order[1]),CARD(Comparing_Order[2])])/10000000
            Suit_count[card.Suit_num]+=1
            if(Suit_count[card.Suit_num]==3):
                colour=True
        
        Comparing_Order.sort(reverse=True)
        #print(Comparing_Order)
        #The case where two numbers are the same and sorted with the pair first
        if(Comparing_Order[0]==Comparing_Order[1]):
            return 1+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        #The case where theres pairs and theyre sorted with the pair second
        elif(Comparing_Order[1]==Comparing_Order[2]):
            return 1+CardsToHash([CARD(Comparing_Order[0]),CARD(Comparing_Order[1]),CARD(Comparing_Order[2])])/10000000
        
            
        if(Comparing_Order[0]-1==Comparing_Order[1] and 
           Comparing_Order[1]-1== Comparing_Order[2]):
            straight=True
        if(Comparing_Order[0]==12 and Comparing_Order[1]==1 and Comparing_Order[2]==0):
            straight=True
        
        if(straight and colour):
            return 4+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        elif(straight):
            return 3+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        elif(colour):
            return 2+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000
        else:
            return 0+CardsToHash([CARD(Comparing_Order[2]),CARD(Comparing_Order[1]),CARD(Comparing_Order[0])])/10000000

def DeckCreateandShuffle():
    Deck=list()
    #populate it
    for i in range(52):
        Deck.append(CARD(i))
    #shuffle tbhe deck
    random.shuffle(Deck)
    return Deck

def HandGenerator(player_num):  
    #List container for two hands
    Hands=list()
    #Create Deck
    Deck=DeckCreateandShuffle()
    
    for i in range(player_num):
        Hands.append(list())
        for j in range(9):
            #Dealing the hands one by one
            Hands[i].append(Deck[i+j*player_num])
        
    #Contains a list of 9 Card objects    
    return Hands

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