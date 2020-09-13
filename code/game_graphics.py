###Module Description###
#----------------------------------------------
# Function: Deals with all things game-graphics related

import classes
import pygame
import in_game as ingame
import math
import time

SIZE_BOARD = 40



#----------------------------------------------
# Function: initializes the game window
# Input: config -> class that contains the info from the config file
# Output: screen -> screen surface
def init_window(config):
    #Initialize pygame
    pygame.init()
    pygame.font.init()

    #Initialize window
    config.screen = pygame.display.set_mode((config.width, config.height+SIZE_BOARD))
    pygame.display.set_caption("Bubbles")
    icon = pygame.image.load("./images/icon.png")
    pygame.display.set_icon(icon)
    
    return config



#----------------------------------------------
# Function: draws the control board
# Input: config -> class that contains the info from the config file, screen -> screen surface
# Output: controls -> list of rectangles object that correspond to the buttons
def control_board( config):
    #Draw line to separate control board from game
    pygame.draw.line(config.screen, (0,0,0), [0,SIZE_BOARD-2], [config.width,SIZE_BOARD-2], 2)
    
    controls=[]
    surfaces=[]
    #Create rectangles
        #New Game
    controls.append( pygame.Rect (0.025*config.width, 0.1*SIZE_BOARD, 0.20*config.width, 0.8*SIZE_BOARD ) )
        #End
    controls.append(pygame.Rect (0.25*config.width, 0.1*SIZE_BOARD, 0.20*config.width, 0.8*SIZE_BOARD ) )
        #Score
    controls.append(pygame.Rect (0.70*config.width, 0.1*SIZE_BOARD, 0.28*config.width, 0.8*SIZE_BOARD ) )
    
    #TextSurface
    myfont = pygame.font.SysFont('lucidaconsole', int(SIZE_BOARD/2))
    surfaces.append( myfont.render('New Game', False, (0,0,0)) )
    surfaces.append( myfont.render('End Game', False, (0,0,0)) )
    surfaces.append( myfont.render('Score: '+ str(config.score), False, (0,0,0)) )
    
    #Draw Rectangles
    for button in controls:
        pygame.draw.rect(config.screen, (0,0,0), button, 2)

    #Draw Text
    config.screen.blit(surfaces[0],(0.04*config.width, 0.225*SIZE_BOARD) )
    config.screen.blit(surfaces[1],(0.265*config.width, 0.225*SIZE_BOARD) )
    config.screen.blit(surfaces[2],(0.715*config.width, 0.225*SIZE_BOARD) )
    
    return controls



#----------------------------------------------
# Function: checks if any button has been roessed
# Input: controls -> list of rectangles that correspond to the buttons, pos->mouse position (x,y)
# Output: game, new_game -> game= True while game is running, new_game= True when a new game is initialized
def check_buttons(controls, pos):
    for button in controls:
        if button.collidepoint(pos):
            #New Gane
            if button== controls[0]:
                print('new game')
                return True, True
            #End Game
            elif button == controls[1]:
                return False, False
    
    return True, False



#----------------------------------------------
# Function: draws the bubbles 
# Input: config -> class that contains the info from the config file, screen -> screen surface, bubbles -> matrix that contains the bubbles info
# Output: ---
def draw_bubbles(config, bubbles):
    for i in range (len(bubbles[:,0])):
        for j in range (int (config.width / (2*config.r))):  
            if bubbles[i][j].color!= 0:   
                draw_one_bubble(config,bubbles[i][j])





#----------------------------------------------
# Function:
# Input: 
# Output: ---
def draw_next_bubble(config,bubble_in_play):
    #Next bubble
    draw_one_bubble(config,bubble_in_play)
        #Draw box
    pygame.draw.rect(config.screen, (0,0,0), (0,config.height+SIZE_BOARD-2*config.r, 2*config.r, 2*config.r ), 2)



#----------------------------------------------
# Function:
# Input: 
# Output: ---
def draw_line(config, end_pos, alpha):
    y_base= config.height + SIZE_BOARD - config.r
    x_base=int(config.width/2)

    #draw line
    pygame.draw.line(config.screen, (0,0,0), (x_base, y_base), end_pos, 2)

    #Calculate Triangle Point
    size_arrow=int(config.r/2)
    beta=math.pi/4 - alpha

    x1=end_pos[0]-size_arrow*math.sin(beta)
    y1=end_pos[1]+size_arrow*math.cos(beta)
    
    x2=end_pos[0]-size_arrow*math.cos(beta)
    y2=end_pos[1]-size_arrow*math.sin(beta)
    
    #Draw Triangle
    pygame.draw.polygon(config.screen, (0,0,0), [end_pos, (x1,y1), (x2,y2)])
    



#----------------------------------------------
# Function:
# Input: 
# Output: ---
def draw_one_bubble( config, bubble):
    color= ingame.pick_color(bubble.color, config)
    config.screen.blit(color, (bubble.x-config.r,bubble.y-config.r))
    #Draw Circle
    #pygame.draw.circle(config.screen, color, (bubble.x,bubble.y), config.r)
    #Draws outline
    #pygame.draw.circle(config.screen, (0,0,0),(bubble.x,bubble.y), config.r, 1)



#----------------------------------------------
# Function:
# Input: 
# Output: ---
def launch_bubble(config,  bubble_in_play, bubbles):
    
    #Bubble is within the board
    if (bubble_in_play[1].x>0 and bubble_in_play[1].x<config.width and bubble_in_play[1].y>SIZE_BOARD+config.r and bubble_in_play[1].y<config.height+SIZE_BOARD):
        bounce_wall(bubble_in_play[1], config)
        
        bubble_in_play[1].x+= int(config.r*math.cos(bubble_in_play[1].angle))
        bubble_in_play[1].y-= int(config.r*math.sin(bubble_in_play[1].angle))
        time.sleep(0.001)

        draw_one_bubble(config,bubble_in_play[1])
        #collision
        if bubble_in_play[1].launched== True:
            ingame.is_first_line(config, bubbles, bubble_in_play[1])
            #Is not in the first line, detect collision
            if bubble_in_play[1].launched == True: 
                ingame.collision(bubbles, bubble_in_play[1], config)
        
        if bubble_in_play[1].launched == False:
            pop_list=[[bubble_in_play[1].i, bubble_in_play[1].j]]
            pop_list=ingame.pop_bubble(bubbles, bubble_in_play[1].color, bubble_in_play[1].i, bubble_in_play[1].j, pop_list)
            
            ingame.clean_board(bubbles, pop_list, config)
            pop_list=[]
            ingame.bubble_in_play(bubble_in_play, config)
            
        return 
    bubble_in_play[1].launched = False
    ingame.bubble_in_play(bubble_in_play, config)




#----------------------------------------------
# Function: 
# Input: 
# Output: 
def game_over_screen(config,score):
    surfaces=[]
    #TextSurface
    myfont = pygame.font.SysFont('lucidaconsole', int(SIZE_BOARD))
    surfaces.append( myfont.render('Score: '+ str(config.score), False, (0,0,0)) )
    surfaces.append( myfont.render('Insert Name:', False, (0,0,0)) )
    
    #Game Over graph (original: 250x100)
    factor=1.2
    game_over_graph = pygame.image.load('./images/game_over.png')
    game_over_graph=pygame.transform.rotozoom(game_over_graph,0,factor )
    config.screen.blit(game_over_graph, ((config.width - 250*factor)/2, 2*SIZE_BOARD))

    #Draw Text
    config.screen.blit(surfaces[0],(int(0.10*config.width), int(0.5*config.height) ))
    config.screen.blit(surfaces[1],(int(0.10*config.width), int(0.6*config.height) ))






#----------------------------------------------
# Function: 
# Input: 
# Output: 
def bounce_wall(bubble_in_play, config):
    position = bubble_in_play.x
    if (position>0 and position<config.r) or (position<config.width and position > config.width - config.r):
        bubble_in_play.angle= math.pi -bubble_in_play.angle

