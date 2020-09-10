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

#Main
config= pap.pre_init()
config=ggraph.init_window(config)
bubbles=ingame.init_board(config)

bubble_in_play=[classes.bubble(config.r, config.height+ggraph.SIZE_BOARD-config.r, random.randrange(1,10) ),
                classes.bubble_moving(int(config.width/2), config.height+ggraph.SIZE_BOARD-config.r, random.randrange(1,10), 0, False)]


game= True

#Game Loop
while game:
    #White Background 
    config.screen.fill((255,255,255))

    #Draw Control Board
    controls=ggraph.control_board(config)

    #Draw Bubbles
    ggraph.draw_bubbles(config, bubbles)
    ggraph.draw_next_bubble(config,bubble_in_play[0])

    #If a bubble is not in movement
    if bubble_in_play[1].launched == False:
        #Pointer
        (x,y), alpha=ingame.line(config)
        ggraph.draw_line(config, (x,y), alpha)
        
        #Draw bubble
        ggraph.draw_one_bubble(config,bubble_in_play[1])
        
        #Events
        game, bubbles=ingame.events(controls, config, bubble_in_play, alpha, bubbles)
        
        #Check if it is a game over
        if game == True:
            game=ingame.game_over(bubbles)
    else:
        #Ball is in movement
        bubble_in_play, bubbles= ggraph.launch_bubble(config, bubble_in_play, bubbles)
    
    #Update Screen
    pygame.display.update()


#Game Over Screen
game_over=True
score=0
time.sleep(0.75)
while game_over:
    config.screen.fill((255,255,255))
    ggraph.game_over_screen(config, score)
    pygame.display.update()
    for event in pygame.event.get():
        #Close Window
        if event.type == pygame.QUIT:
            game_over= False
        if pygame.mouse.get_pressed()==(True,False,False):
            game_over=False
