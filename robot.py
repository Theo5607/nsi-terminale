from random import *

class Robot:
    def __init__(self,cor=[0,0],dir=None):
        self.cor=cor
        self.dir=dir
    def dep(self,dir):
        if dir=="N":
            self.cor[1]+=1
        elif dir=="S":
            self.cor[1]-=1
        elif dir=="E":
            self.cor[0]+=1
        elif dir=="W":
            self.cor[0]-=1
        
robot1=Robot([0,0],None)
for i in range (3):
    robot1.dep("N")

print(robot1.cor)
