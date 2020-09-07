###Module Description###
#----------------------------------------------
# Function: Deals with all things game-graphics related

import classes
import pygame
import in_game as ingame

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
    screen = pygame.display.set_mode((config.width, config.height+SIZE_BOARD))
    pygame.display.set_caption("Bubbles")
    icon = pygame.image.load("./images/icon.png")
    pygame.display.set_icon(icon)
    
    return screen



#----------------------------------------------
# Function: draws the control board
# Input: config -> class that contains the info from the config file, screen -> screen surface
# Output: controls -> list of rectangles object that correspond to the buttons
def control_board(screen, config):
    #Draw line to separate control board from game
    pygame.draw.line(screen, (0,0,0), [0,SIZE_BOARD-2], [config.width,SIZE_BOARD-2], 2)
    
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
        pygame.draw.rect(screen, (0,0,0), button, 2)

    #Draw Text
    screen.blit(surfaces[0],(0.04*config.width, 0.225*SIZE_BOARD) )
    screen.blit(surfaces[1],(0.265*config.width, 0.225*SIZE_BOARD) )
    screen.blit(surfaces[2],(0.715*config.width, 0.225*SIZE_BOARD) )

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
def draw_bubbles(screen, config, bubbles):
    for i in range (config.initial_lines):
        for j in range (int (config.width / (2*config.r))):  
            if bubbles[i][j]!= 0:   
                #Fetches the respective RGB color code
                color= ingame.pick_color(bubbles[i][j])
                #circle(surface, color, center, radius)
                    #Draws circle
                pygame.draw.circle(screen, color, (j*2*config.r + config.r,i*2*config.r + config.r + SIZE_BOARD), config.r)
                    #Draws outline
                pygame.draw.circle(screen, (0,0,0), (j*2*config.r + config.r,i*2*config.r + config.r + SIZE_BOARD), config.r, 1)