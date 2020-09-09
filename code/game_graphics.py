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
    score=0
    myfont = pygame.font.SysFont('lucidaconsole', int(SIZE_BOARD/2))
    surfaces.append( myfont.render('New Game', False, (0,0,0)) )
    surfaces.append( myfont.render('End Game', False, (0,0,0)) )
    surfaces.append( myfont.render('Score: '+ str(score), False, (0,0,0)) )
    
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
            if button== controls[0]:
                print('new game')
                return True, True
            elif button == controls[1]:
                print('end game')
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
    color= ingame.pick_color(bubble.color)
    #Draw Circle
    pygame.draw.circle(config.screen, color, (bubble.x,bubble.y), config.r)
    #Draws outline
    pygame.draw.circle(config.screen, (0,0,0),(bubble.x,bubble.y), config.r, 1)



#----------------------------------------------
# Function:
# Input: 
# Output: ---
def launch_bubble(config, alpha, bubble_in_play, bubbles, attached):
    launched=True
    
    #Bubble is within the board
    if (bubble_in_play[1].x>0 and bubble_in_play[1].x<config.width and bubble_in_play[1].y>SIZE_BOARD+config.r and bubble_in_play[1].y<config.height+SIZE_BOARD):
        alpha=bounce_wall(bubble_in_play[1].x, config, alpha)
        
        bubble_in_play[1].x+= int(config.r*math.cos(alpha))
        bubble_in_play[1].y-= int(config.r*math.sin(alpha))
        time.sleep(0.025)

        draw_one_bubble(config,bubble_in_play[1])
        #collision
        if attached== False:
            attached=ingame.is_first_line(config, bubbles, bubble_in_play[1])
            #Is not in the first line, detect collision
            if attached == False: 
                bubbles, launched=ingame.collision(bubbles, bubble_in_play[1], config)
        
        if launched == False:
            ingame.bubble_in_play(bubble_in_play)
        
        return launched, bubble_in_play, bubbles, attached,  alpha
    launched=False
    ingame.bubble_in_play(bubble_in_play)
    return  launched, bubble_in_play, bubbles, attached, alpha




#----------------------------------------------
# Function: 
# Input: 
# Output: 
def game_over_screen(config,score):
    surfaces=[]
    #TextSurface
    myfont = pygame.font.SysFont('lucidaconsole', int(SIZE_BOARD))
    surfaces.append( myfont.render('Game Over', False, (0,0,0)) )

    myfont = pygame.font.SysFont('lucidaconsole', int(0.75*SIZE_BOARD))
    surfaces.append( myfont.render('Score: '+ str(score), False, (0,0,0)) )
    surfaces.append( myfont.render('Click to close ', False, (0,0,0)) )
    
    #Draw Text
    config.screen.blit(surfaces[0],(0.10*config.width, 0.5*config.height) )
    config.screen.blit(surfaces[1],(0.10*config.width, 0.6*config.height) )
    config.screen.blit(surfaces[2],(0.10*config.width, 0.7*config.height) )



#----------------------------------------------
# Function: 
# Input: 
# Output: 
def bounce_wall(position, config, alpha):
    if position>0 and position<config.r:
        print(alpha)
        alpha= alpha- (math.pi/4)
        print(alpha)
    elif position<config.width and position > config.width - config.r:
        alpha= alpha + math.pi /4
    return alpha


