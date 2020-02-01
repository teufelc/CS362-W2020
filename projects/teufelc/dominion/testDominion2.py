# -*- coding: utf-8 -*-
"""
Created on Sun 1/19/2020

@author: teufelc, Christopher Teufel
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = ["*Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.BoxInit(nV)

supply_order = testUtility.GetSupplyOrder()

# get supply
supply = testUtility.SupplyInit(box, len(player_names), nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.PlayersInit(player_names)

#Play the game
turn  = 0


#while not Dominion.gameover(supply):
# BUG, chaning to infinite loop, no gameover condition checked
while True:
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


testUtility.PrintWinners(players)
