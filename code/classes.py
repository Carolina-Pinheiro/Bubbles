#Config Class
class config:
    def __init__(self,height, width, r, dl, initial_lines, N_moves, screen ):
        self.height= height
        self.width= width
        self.r= r
        self.dl= dl
        self.initial_lines= initial_lines
        self.N_moves= N_moves
        self.screen= screen
        self.score=0
        self.number_plays=0
        self.colors_list=0

#Bubble Class
class bubble:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color= color 
        self.checked= False

#Bubble Moving Class
class bubble_moving:
    def __init__(self,x,y,color, angle, launched):
        self.x=x
        self.y=y
        self.color= color
        self.angle = angle
        self.launched = launched
        self.i=0
        self.j=0