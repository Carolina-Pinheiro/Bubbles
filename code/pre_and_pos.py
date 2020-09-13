###Module Description###
#----------------------------------------------
# Function: Deals with things that happen before and after the game itself

import classes

from operator import itemgetter

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
# Function: checks if the config info is within the limits to make the game playable
# Input: config -> config class that contains the grid info
# Output: ---
def check_config(config):
    #Width
    if (550<=config.width<=1300) == False:
        if config.width<550:
            config.width=550
        elif config.width >1300:
            config.width=1300
    
    #Height
    if (400<= config.height <= 650)== False:
        if config.height<400:
            config.height=400
        elif config.height >1300:
            config.height=1300
    
    #Radius
    if (15<= config.r<= 35 )== False: #20 recommended
        if config.r<15:
            config.r=15
        elif config.r >35:
            config.r=35
    
    #Coliding distance (percentage of diameter)
    if (1.1<= config.dl <= 1.2) == False: #1.1 recommended
        if config.dl<1.1:
            config.dl=1.1
        elif config.dl >1.2:
            config.dl=1.2
    
    #Initial lines
    if (0<= config.initial_lines<= 5) == False: #2 recommended
        if config.initial_lines<0:
            config.initial_lines=0
        elif config.initial_lines >5:
            config.initial_lines=5
    
    #Moves before adding a new line
    if (5<= config.N_moves <= 20 ) == False: #15 recommended
        if config.N_moves<5:
            config.N_moves=5
        elif config.N_moves >20:
            config.N_moves=20



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
# Function: 
# Input: 
# Output: 
def write_results(players_name, players_score):
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



