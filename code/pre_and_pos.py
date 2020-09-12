###Module Description###
#----------------------------------------------
# Function: Deals with things that happen before and after the game itself

import classes
from operator import itemgetter
import pygame

#----------------------------------------------
# Function: initializes the pre game
# Input: ---
# Output: ---
def pre_init():
    #Read config.txt
    data=config_data()
    specs=[]

    #Separate Text
    for i in range(len(data)):
        if '//' in data[i]:
            specs.append(data[i+1])

    return (initialize_specs(specs) )



#----------------------------------------------
# Function: fetches data from selected file
# Input: ---
# Output: data -> list with each line of the file
def config_data():
    config=open(r'C:\Users\cppin\Desktop\GitHub\Bubbles\config.txt')

    #Read File
    info=config.read()
    data= info.split('\n')
    
    config.close()
    return data



#----------------------------------------------
# Function: initializes the config class with the specs given
# Input: specs -> list of specs
# Output: initial_config -> config class filled
def initialize_specs(specs):
    width=int (specs[0].split()[0])
    height=int ( specs[0].split()[1]) 
    r=int (specs[1])
    dl=float( specs[2] )
    initial_lines= int (specs[3])
    N=int (specs[4])

    if isinstance(width/(2*r),int) == False:
        width= int(width/(2*r))*2*r

    screen=0 #just a placehold
    initial_config= classes.config(height, width, r, dl, initial_lines, N, screen)
    
    return initial_config



#----------------------------------------------
# Function: initializes the config class with the specs given
# Input: specs -> list of specs
# Output: initial_config -> config class filled
def write_results(players_name, players_score):
    print(players_name)
    #Open File and write
    results=open(r'C:\Users\cppin\Desktop\GitHub\Bubbles\results.txt', 'a')
    results.write(str(players_name) + ' '+ str(players_score) +'\n')
    results.close()
    
    #Open File and read
    results=open(r'C:\Users\cppin\Desktop\GitHub\Bubbles\results.txt')
    lines=results.readlines()
    results.close()
    results_list=[]
    for line in lines:
        info=line.split()
        name=info[0]
        score=int(info[1])
        results_list.append((name, score))
    results_list.sort(key=itemgetter(1), reverse=True)
    
    #Open File and write in order
    results=open(r'C:\Users\cppin\Desktop\GitHub\Bubbles\results.txt', 'w')
    for (name, score) in results_list:
        results.write(name +' ' + str(score) + '\n')



#----------------------------------------------
# Function: initializes the config class with the specs given
# Input: specs -> list of specs
# Output: initial_config -> config class filled
def text_input(event, name):
    flag=True
    if event.key == pygame.K_RETURN:
        flag=False
    elif event.key == pygame.K_BACKSPACE:
        name = name[:-1]
    elif event.key == pygame.K_SPACE:
        print('Espaço não, cara')
    else:
        name += event.unicode
    if flag == True:
        return name, True
    else:
        return name, False