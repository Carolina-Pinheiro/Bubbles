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
config=ggraph.init_window(config)
bubbles=ingame.init_board(config)
game= True
bubble_in_play = np.random.randint(1,10,2)
launched=False
attached=False

#Game Loop
while game:
    #White Background 
    config.screen.fill((255,255,255))

    #Draw Control Board
    controls=ggraph.control_board(config)

    #Draw Bubbles
    ggraph.draw_bubbles(config, bubbles)
    (x,y), alpha=ingame.line(config)
    ggraph.draw_line(config, (x,y), alpha)
    ggraph.draw_next_bubble(config,bubble_in_play)

    #If a bubble is not in movement
    if launched == False:
        #Center bubble coordinates
        bubble_x=int(config.width/2)
        bubble_y=config.height+ggraph.SIZE_BOARD-config.r
            #Draw bubble
        ggraph.draw_one_bubble(config,bubble_in_play[1],(int(config.width/2), config.height+ggraph.SIZE_BOARD-config.r))
        #Reset Variables, after a succesfull launch
        attached=False
        
        #Events
        game, new_game, launched=ingame.events(controls, alpha, config, bubble_in_play)
    else:
        [bubble_x,bubble_y], launched, bubble_in_play, bubbles, attached, game = ggraph.launch_bubble(config, alpha, bubble_in_play, [bubble_x,bubble_y], bubbles, attached)
    
    #New Game button was clicked
    if new_game == True:
        bubbles=ingame.init_board(config)
    
    #Update Screen
    pygame.display.update()


#Game Over Screen
game_over=True
score=0
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
