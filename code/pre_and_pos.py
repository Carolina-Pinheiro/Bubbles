###Module Description###
#----------------------------------------------
# Function: Deals with things that happen before and after the game itself

import classes



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

    initial_config= classes.config(height, width, r, dl, initial_lines, N)
    
    return initial_config