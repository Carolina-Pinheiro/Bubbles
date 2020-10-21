####--------------------Bubbles--------------------###
#Carolina Pinheiro, 
#carolina.p.pinheiro@tecnico.ulisboa.pt  
#September 2020

#Modules
import pre_and_pos as pap
import game_graphics as ggraph
import in_game as ingame
import classes

import pygame
import numpy as np
import time

#######
#Main
#Get game configuration
config= pap.pre_init()

#Check config
pap.check_config(config)

#Initialize game
config=ggraph.init_window(config)

#Initialize Variables
bubbles, bubble_in_play, background_sized= ingame.initialize_variables(config)
rect = [pygame.Rect (int(0.3*config.width), int(0.4*config.height), int(0.4*config.width), int(0.25*config.height) ),
        pygame.Rect (int(0.3*config.width), int(0.7*config.height), int(0.4*config.width), int(0.25*config.height) )]
game= True
menu=0
flag=0
name=''
#Initial Menu
while game:
    if menu ==0:
        menu=ingame.menu(background_sized, config, rect)

    #Game Loop
    elif menu ==1:
        menu, bubbles = ingame.game_loop(background_sized, config,bubbles,bubble_in_play, menu)
        #Short Pause so the player can see the board before the game over screen
        #time.sleep(0.75) 
    
    elif menu==2:
        menu=ingame.results(background_sized, config)
    
    elif menu ==3:
        #Game Over Screen
        menu, name = ingame.game_over_loop(config, background_sized, menu, name)
        
    elif menu ==4:
        game=False
    
    elif menu==5:
        #Write in the results file
        pap.write_results(name, config.score)
        bubbles, bubble_in_play, background_sized= ingame.initialize_variables(config)
        config.score=0
        config.number_plays=0
        menu=0