###Module Description###
#----------------------------------------------
# Function: Deals with all things game-related

import classes 
import numpy as np
import pygame
import game_graphics as ggraph
import random
import math
import time

launched= False
#----------------------------------------------
# Function: initializes a game board, randomly generating bubbles
# Input: config -> class that contains the info from the config file
# Output: bubbles -> matrix with the bubbles generated
def init_board(config):
    #Generate game board
    n_bubbles = int (config.width / (2*config.r))
    print(config.initial_lines, n_bubbles )
    bubbles= np.random.randint(1,10,(config.initial_lines, n_bubbles ))

    #Calculate the max number of lines
    max_lines= int(config.height/(2*config.r) ) -config.initial_lines -2
    newrow= np.zeros(n_bubbles) 
    
    for i in range(max_lines):
        bubbles = np.vstack([bubbles, newrow])
    
    print(bubbles)
    return bubbles



#----------------------------------------------
# Function: handles the pygame events
# Input: controls -> list that contains the button's position in a rect object
# Output: game-> True while game is running, new_game-> True when a new game is created
def events(controls, alpha, config, bubble_in_play, screen):
    game=True
    new_game= False
    launched = False

    #Wait for an event
    for event in pygame.event.get():
        #Close Window
        if event.type == pygame.QUIT:
            game= False
        #Right Click
        if pygame.mouse.get_pressed()==(True,False,False):
            pos = pygame.mouse.get_pos()
            #Check if any buttons were pressed
            game, new_game= ggraph.check_buttons(controls, pos)
            if pos[1]>ggraph.SIZE_BOARD:
                launched= True
                return game, new_game, launched
    
    return game, new_game, launched



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



#----------------------------------------------
# Function: 
# Input:
# Output: 
def bubble_in_play(bubble_in_play):
    bubble_in_play[1]= bubble_in_play[0]
    bubble_in_play[0]=random.randrange(1,10)



#----------------------------------------------
# Function: 
# Input:
# Output: 
def line(config):
    y_base= config.height + ggraph.SIZE_BOARD - config.r
    x_base=int(config.width/2)
    
    #Define the points
    p1=pygame.mouse.get_pos()
    p2=(x_base, y_base)
    p3=(x_base+10, y_base)
    
    #Calculate the angle
    v0 = np.array(p1) - np.array(p2)
    v1 = np.array(p3) - np.array(p2)
    angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
    alpha= np.degrees(angle)
    
    if alpha<0:
        p1=list(p1)
        p1[1]=y_base
        p1=tuple(p1)
        if alpha>-90:
            alpha=0
        else:
            alpha=180
    
    #Calculate the line size
    base=p1[0]-p2[0]
    perpend=p1[1]-p2[1]
    dist=math.hypot(base,perpend)
    line_size=4*config.r
    alpha_rad = np.radians(alpha)
    
    #Reduce the line size
    p4=(x_base + line_size*math.cos(alpha_rad), y_base - line_size*math.sin(alpha_rad) )
    
    return p4, alpha_rad



#----------------------------------------------
# Function: 
# Input:
# Output: 
def detect_collision(config, p, bubbles, bubble_in_play):
    x=p[0]
    y=p[1]
    n_bubbles = int (config.width / (2*config.r))
    max_lines= int(config.height/(2*config.r) ) -config.initial_lines -2 + config.initial_lines

    for i in range (len(bubbles[:,0])):
        for j in range (int (config.width / (2*config.r))):  
            b_x=j*2*config.r + config.r
            b_y=i*2*config.r + config.r + ggraph.SIZE_BOARD

            dist=calculate_distance([b_x,b_y], [x,y])
            if dist<config.dl*2*config.r and bubbles[i][j]!=0:
                
                print('centro'+ str([bubbles[i][j]]))
                if j+1<n_bubbles:
                    print('direita' +str(bubbles[i][j+1]))
                    #Direita
                    if  y>=(-x+b_x+b_y) and y<=(x-b_x+b_y) and bubbles[i][j+1]==0:
                        bubbles[i][j+1]= bubble_in_play[1]
                        flag_attach=False
                        print(bubbles)
                if i+1< max_lines:
                    print('baixo' +str(bubbles[i+1][j]))
                    #Baixo
                    if y>=(-x+b_x+b_y) and y>=(x-b_x+b_y)and bubbles[i+1][j]==0:
                        bubbles[i+1][j] = bubble_in_play[1]
                        flag_attach=False
                        print(bubbles)
                if j-1>=0:
                    print('esquerda' +str(bubbles[i][j-1]))
                    #Esquerda
                    if y<=(-x+b_x+b_y) and y>=(x-b_x+b_y)and bubbles[i][j-1]==0:
                        bubbles[i][j-1] = bubble_in_play[1]
                        flag_attach=False
                    print(bubbles)
                if i-1>=0:
                    print('cima' +str(bubbles[i-1][j]))
                    #Cima
                    if y<=(-x+b_x+b_y) and y<=(x-b_x+b_y)and bubbles[i-1][j]==0:
                        bubble_in_play[i-1][j] = bubble_in_play[1]
                
                #time.sleep(30)
                print(bubbles[0])
                return bubbles, flag_attach
    
    flag_attach=True
    return bubbles, flag_attach



#----------------------------------------------
# Function: 
# Input:
# Output: 
def calculate_distance(p1,p2):
    dist=math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2  )
    return dist
