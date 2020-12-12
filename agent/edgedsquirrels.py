import random
import pygame
import sys

from agent.base_agent import BaseAgent
from agent.edgedsquirrels_func.func3 import *

#python3 arena.py --agent1 edgedsquirrels.MyAgent --agent2 base_agent.RandomAgent
class MyAgent(BaseAgent):
    stepnow=0  #0:starting point
    developdepth=4
    '''
    developnumlimit_small=6000
    developdepth_big=4
    developnumlimit_big=20000
    developdepth_big=5
    '''
    danger={(1,0),(0,1),(1,1),  (0,6),(1,7),(1,6),   (6,0),(7,1),(6,1),    (6,6),(7,6),(6,7)}
    safe={(0,0),(0,7),(7,0),(7,7)}
    good={
        (0,2),(0,3),(0,4),(0,5),
        (7,2),(7,3),(7,4),(7,5),
        (2,0),(3,0),(4,0),(5,0),
        (2,7),(3,7),(4,7),(5,7)
    }
                

    def negamax(self,board,a=-1000,b=1000,depth=0,Factor=0): #a:worst case  b:best case
        if (depth>self.developdepth):
            board.get_value()
            board.value+=Factor
            return board.value
        board.get_children()
        if board.children==[]:
            board.get_value()
            board.value+=Factor
            return board.value

        board.value =-1000
        for child in board.children:
            self.developnum+=1
            factor=Factor
            if (child[0],child[1]) in self.safe: factor+=80
            else:
                for kk in child[3]:
                    #print(kk, end=' ')
                    if kk in self.danger :
                        xx=0 if kk[0]<4 else 7
                        yy=0 if kk[1]<4 else 7
                        if board.obs[xx+8*yy]==0:
                            factor-=40
                        #print("danger!",board.myturn)
                    if kk in self.good:
                        factor+=2
            child=child[2]
            board.value = max(board.value, -(self.negamax(board=child, a=-b, b=-a,depth=depth+1,Factor=-factor)))
            a = max(a, board.value)
            if a >= b :
                break #(* cut-off *)
        return board.value





    def step(self,reward,obs):# call this func   rewrite the step function
        if self.color=='black': self.mycolor=-1
        else: self.mycolor=1
        self.obs=obs
        self.steps=[[] for i in range(self.developdepth+1)]
        self.developnum=0
        nowboard=MyBoard(self.obs,self.stepnow,self.mycolor)

        x=-1;y=-1
        bestv=self.negamax(board=nowboard,a=-1000,b=1000,depth=0)
        for i in range(len(nowboard.children)):

            if nowboard.children[i][2].value==-bestv:
                x=nowboard.children[i][0]
                y=nowboard.children[i][1]
                break

        return (self.col_offset + x * self.block_len, self.row_offset + y * self.block_len),pygame.USEREVENT

    
        
