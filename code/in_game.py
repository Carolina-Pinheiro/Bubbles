###Module Description###
#----------------------------------------------
# Function: Deals with all things game-related

import classes 
import numpy as np
import pygame
import game_graphics as ggprah



#----------------------------------------------
# Function: initializes a game board, randomly generating bubbles
# Input: config -> class that contains the info from the config file
# Output: bubbles -> matrix with the bubbles generated
def init_board(config):
    #Generate game board
    n_bubbles = int (config.width / (2*config.r))
    print(config.initial_lines, n_bubbles )
    bubbles= np.random.randint(1,10,(config.initial_lines, n_bubbles ))
    print(bubbles)

    return bubbles



#----------------------------------------------
# Function: handles the pygame events
# Input: controls -> list that contains the button's position in a rect object
# Output: game-> True while game is running, new_game-> True when a new game is created
def events(controls):
    game=True
    new_game= False
    #Wait for an event
    for event in pygame.event.get():
        #Close Window
        if event.type == pygame.QUIT:
            game= False
        
        #Right Click
        if pygame.mouse.get_pressed()==(True,False,False):
            pos = pygame.mouse.get_pos()
            #Check if any buttons were pressed
            game, new_game= ggprah.check_buttons(controls, pos)
    
    return game, new_game



#----------------------------------------------
# Function: matches the number to a color
# Input: bubble -> the corresponding number of the bubble
# Output: color -> (R,G,B)
def pick_color(bubble):
    #Colors
    # 1-red
    if bubble==1: 
        color = (255,0,0)
    # 2 purple
    elif bubble == 2:
        color = (200,0,220)
    # 3 blue
    elif bubble == 3:
        color = (0,0,255)
    # 4 cyan
    elif bubble == 4:
        color = (0,255,255)
    # 5 green
    elif bubble == 5:
        color = (0,200,0)
    # 6 yellow
    elif bubble == 6:
        color = (255,223,0)
    # 7 brown
    elif bubble == 7:
        color = (101,67,35)
    # 8 black
    elif bubble == 8:
        color = (0,0,0)
    # 9 white 
    elif bubble == 9:
        color = (255,255,255)
    # empty
    else:
        color= (255,255,255)
    
    return color