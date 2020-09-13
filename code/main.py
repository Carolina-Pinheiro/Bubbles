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
import random
import time

#######
#Main
#Get game configuration
config= pap.pre_init()

#Check config
##########################

#Initialize game
config=ggraph.init_window(config)

#Initialize Variables
bubbles, bubble_in_play, background_sized= ingame.initialize_variables(config)
game= True

#Game Loop
while game:
    game, bubbles = ingame.game_loop(background_sized, config,bubbles,bubble_in_play, game)

#Short Pause so the player can see the board before the game over screen
time.sleep(0.75) 

#Game Over Screen
game_over=True
background_sized= pygame.transform.scale(pygame.image.load('./images/fundo.jpg'), (config.width, config.height+ ggraph.SIZE_BOARD))
name=''
while game_over:
    game_over, name = ingame.game_over_loop(config, background_sized, game_over, name)

#Write in the results file
pap.write_results(name, config.score)