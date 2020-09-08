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
bubble_in_play = np.random.randint(1,10,2)
launched=False

#Game Loop
while game:
    #White Background 
    screen.fill((255,255,255))

    #Draw Control Board
    controls=ggraph.control_board(screen, config)

    #Draw Bubbles
    ggraph.draw_bubbles(screen, config, bubbles)
    (x,y), alpha=ingame.line(config)
    ggraph.draw_line(config, screen,(x,y), alpha)
    ggraph.draw_next_bubble(screen,config,bubble_in_play)

    if launched == False:
        bubble_x=int(config.width/2)
        bubble_y=config.height+ggraph.SIZE_BOARD-config.r
        ggraph.draw_play_bubble(screen,config,bubble_in_play)
        flag_attach=True

        #Events
        game, new_game, launched=ingame.events(controls, alpha, config, bubble_in_play, screen)
    else:
        [bubble_x,bubble_y], launched, bubble_in_play, bubbles, flag_attach = ggraph.launch_bubble(config, alpha, bubble_in_play, screen,[bubble_x,bubble_y], bubbles, flag_attach)
    
    if new_game == True:
        bubbles=ingame.init_board(config)
    
    #ingame.bubble_in_play(bubble_in_play)
    #Update
    pygame.display.update()

