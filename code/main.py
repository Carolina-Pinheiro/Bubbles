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

#Main
config= pap.pre_init()
screen=ggraph.init_window(config)
bubbles=ingame.init_board(config)
game= True

#Game Loop
while game:
    #White Background 
    screen.fill((255,255,255))

    #Draw Control Board
    controls=ggraph.control_board(screen, config)

    #Draw Bubbles
    ggraph.draw_bubbles(screen, config, bubbles)

    #Events
    game, new_game=ingame.events(controls)

    if new_game == True:
        bubbles=ingame.init_board(config)
    #Update
    pygame.display.update()

