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
config= pap.pre_init()

#Check config
##########################

#Initialize game
config=ggraph.init_window(config)
bubbles=ingame.init_board(config)
config.colors_list=ingame.load_colors(config)

#Initialize Variables
bubble_in_play=[classes.bubble(config.r, config.height+ggraph.SIZE_BOARD-config.r, random.randrange(1,10) ),
                classes.bubble_moving(int(config.width/2), config.height+ggraph.SIZE_BOARD-config.r, random.randrange(1,10), 0, False)]

background = pygame.image.load('./images/fundo.jpg')
background2 = pygame.image.load('./images/fundo2.jpg')

background_sized= [pygame.transform.scale(background, (config.width, config.height))]
background_sized.append(pygame.transform.scale(background2, (config.width, ggraph.SIZE_BOARD)))
game= True

#Game Loop
while game:
    game, bubbles=ingame.game_loop(background_sized, config,bubbles,bubble_in_play, game)

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