# 9cards

**Introduction**

The goal of the project was intially rather vague and was basically make a playable version of of this game I learnt that we knew to be called 9-cards 
and I actually found the game with the exact rules I grew up playing called 9-card brag. 
The logic was to be written in python and the front-end aspect of it, is yet to be decided but currently I am leaning on using ReactJS to set up a 
website where the game can be played. 

**Rules**

The rules are as mentioned on this website https://ourpastimes.com/card-brag-rules-5369882.html barring the 4 pair and 4 of a kind rules which hane not been
implemented yet.

Each game can be played by 2-5 players. Each player is dealt 9 cards and has to sort their 9 cards into 3 sets of cards in descending order of rank, 
the program will sort the sets by rank anyway so a simple sorting into sets of 3 cards is enough but it should be kept in mind that when deciding a winner,
hands are sorted.

The ranks of each hand are as follows with the strongest appearing first: 3 of a kind, Straight Flush(Running/Running FLush), Straight(Run), Flush(Colour),
Pair, and finally Top Card.

For hands of the same rank the stronger set is determined by the cards with the higher values, a particular difference with poker is that a straight
consisting of A,2,3 is a stronger straight than K,Q,J due to the highest card being higher. For pairs the value of the pairs take precedent followed by the
backing card.


**Completed Tasks**
*   The basic logic has been implemented and tested i.e. the ranking of hands, deciding winners between 5 hands, a (rather several) working AI.
*   A method that creates player objects, which stores data about players during a game instance
*   A Command-line game which was used to test the logic and iron out bugs. (This is the All_encompassing_Game() method in the Command_Line_game.py file)
  
**Tasks remaining**
*   Create a rule Document
*   Implement the 4 card automatic win rule 
    * re-Program the AIs with this in mind  
    * Create logic that allows for a the comparison of two or more 4 of a kinds
*   Implementing the 4 pair automatic tie rule 
    * Change the card selection method
    * re-Program the AIs with this in mind 
*   Creating a method that converts the objects to JSON for a front-end application
*   The Actual front end playable game
*   Deploying the game on a website
*   Creating a live online multiplayer version of the game
