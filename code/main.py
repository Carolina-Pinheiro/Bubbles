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

#Check config
##########################

config=ggraph.init_window(config)
bubbles=ingame.init_board(config)
config.colors_list=ingame.load_colors(config)

bubble_in_play=[classes.bubble(config.r, config.height+ggraph.SIZE_BOARD-config.r, random.randrange(1,10) ),
                classes.bubble_moving(int(config.width/2), config.height+ggraph.SIZE_BOARD-config.r, random.randrange(1,10), 0, False)]

background = pygame.image.load('./images/fundo.jpg')
background2 = pygame.image.load('./images/fundo2.jpg')
background_sized= pygame.transform.scale(background, (config.width, config.height))
background2_sized = pygame.transform.scale(background2, (config.width, ggraph.SIZE_BOARD))
game= True
score=0
#Game Loop
while game:
    #White Background 
    config.screen.blit(background_sized, (0, ggraph.SIZE_BOARD))
    config.screen.blit(background2_sized, (0,0))

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
        bubbles=ingame.check_num_plays(config, bubbles)
        game, new_game=ingame.events(controls, config, bubble_in_play, alpha, bubbles)
        
        #Check if it is a game over
        if game == True:
            game=ingame.game_over(bubbles)
        
        #Check game over
        if new_game== True:
            bubbles=ingame.init_board(config)
            config.score=0
        
    else:
        #Ball is in movement
        ggraph.launch_bubble(config, bubble_in_play, bubbles)
    
    #Update Screen
    pygame.display.update()
    


#Game Over Screen
game_over=True
score=0
time.sleep(0.75)
name=''
background_sized= pygame.transform.scale(background, (config.width, config.height+ ggraph.SIZE_BOARD))

while game_over:
    config.screen.blit(background_sized, (0, 0))
    ggraph.game_over_screen(config, score)
    myfont = pygame.font.SysFont('lucidaconsole', int(ggraph.SIZE_BOARD))
    get_input=True

    for event in pygame.event.get():
        #Close Window
        if event.type == pygame.QUIT:
            game_over= False
        #Get input text
        if event.type == pygame.KEYDOWN:
            name, game_over=pap.text_input(event,name)
    
    #Text Box
    write_rect=pygame.Rect (int(0.09*config.width), int(0.69*config.height), int(0.85*config.width), int(1.1*ggraph.SIZE_BOARD) )
    pygame.draw.rect(config.screen, (255,255,255), write_rect)
    pygame.draw.rect(config.screen, (0,0,0), write_rect, 2)

    #Write Input
    surface= myfont.render(str(name), False, (0,0,0))
    config.screen.blit(surface,(int(0.10*config.width), int(0.7*config.height)) )
    pygame.display.update()

#Write in the results file
pap.write_results(name, config.score)