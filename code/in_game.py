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
    game= True
    flag_attach=True
    around=True
    #Goes through the matrix
    for i in range (len(bubbles[:,0])):
        for j in range (int (config.width / (2*config.r))):  
            #Center bubble coordinates
            b_x=j*2*config.r + config.r
            b_y=i*2*config.r + config.r + ggraph.SIZE_BOARD

            #Calculate distance between one given bubble and the bubble that was launched
            dist=calculate_distance([b_x,b_y], p)

            #If it's close enough, let's check where it will land
            if dist<config.dl*2*config.r and bubbles[i][j]!=0:
                #Check Around the bubble
                flag_attach, bubbles=check_around(bubbles,i,j,p,[b_x,b_y], bubble_in_play)
                
                #The bubble can't attach around, game ends
                if flag_attach == True:
                    around=False
                    break
                return bubbles, flag_attach, game
    
    #Checks if it can attach to the top of the board
    if p[1]>ggraph.SIZE_BOARD and p[1] <ggraph.SIZE_BOARD+config.r and flag_attach==True:
        x=int (round((p[0]/(2*config.r)),0))
        if bubbles[0][x]==0:
            bubbles[0][x]= bubble_in_play[1]
    elif around==False:
        game=False
    #It isn't close enough to any bubble
    return bubbles, flag_attach, game



#----------------------------------------------
# Function: 
# Input:
# Output: 
def calculate_distance(p1,p2):
    dist=math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2  )
    return dist



#----------------------------------------------
# Function: 
# Input:
# Output: 
def check_around(bubbles,i,j,z,b, bubble_in_play):
    flag_attach=True
    #To the right
    if j+1<len(bubbles[0]) and flag_attach and  z[1]>=(-z[0]+b[0]+b[1]) and z[1]<=(z[0]-b[0]+b[1]) and bubbles[i][j+1]==0:
            bubbles[i][j+1]= bubble_in_play[1]
            flag_attach=False

    #Below
    if i+1<len(bubbles[:,0]) and flag_attach and z[1]>=(-z[0]+b[0]+b[1]) and z[1]>=(z[0]-b[0]+b[1])and bubbles[i+1][j]==0:
            bubbles[i+1][j] = bubble_in_play[1]
            flag_attach=False

    #To the left
    if j-1>=0 and flag_attach and z[1]<=(-z[0]+b[0]+b[1]) and z[1]>=(z[0]-b[0]+b[1])and bubbles[i][j-1]==0:
            bubbles[i][j-1] = bubble_in_play[1]
            flag_attach=False

    #Above
    if i-1>=0 and flag_attach and  z[1]<=(-z[0]+b[0]+b[1]) and z[1]<=(z[0]-b[0]+b[1])and bubbles[i-1][j]==0:
            bubble_in_play[i-1][j] = bubble_in_play[1]
            flag_attach=False
    
    return flag_attach, bubbles