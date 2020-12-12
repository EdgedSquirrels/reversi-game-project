import random
import pygame
import sys

#from edgedsquirrels_func import *
from agent.base_agent import BaseAgent
#from base_agent import *
#import BaseAgent
from agent.edgedsquirrels_func.func0 import *

#python3 arena.py --agent1 edgedsquirrels.MyAgent --agent2 base_agent.RandomAgent
class MyAgent(BaseAgent):
    #x=0,y=0
    #ff=Findroute()
    stepnow=0

    def step(self,reward,obs):
        # override this function
        # strongly suggest: write a function to get valid actions
        """
        4GB file
        4GB memory usage
        4 threads
        30 seconds
        If you want to use third-party packages other than numpy, pygame, pytorch and tensorflow, report an issue. (We suggest using rule based algorithm)
        Parameters
        ----------
        reward : dict
            current_score - previous_score
            
            key: -1(black), 1(white)
            value: numbers
            
        obs    :  dict
            board status

            key: int 0 ~ 63
            value: [-1, 0 ,1]
                    -1 : black
                     0 : empty
                     1 : white

        Returns
        -------
        tuple:
            (x, y) represents position, where (0, 0) mean top left. 
                x: go right
                y: go down
        event_type:
            non human agent uses pygame.USEREVENT
        """
        #if len(obs)<64: return (-1,-1),0
        if self.color=='black': self.mycolor=-1
        else: self.mycolor=1
        self.obs=obs
        #print(self.obs)
        for i in range(64):
            if not -1<=obs[i]<=1:
                for i in range(8):
                    for j in range(8):
                        buf=obs[i*8+j]
                        if buf>=0:print('',buf,end='')
                        else:print(buf,end='')
                    print()
                print()
                print('\n\n')
                        


        A=MyBoard(obs=self.obs,step=self.stepnow,mycolor=self.mycolor)
        
        if A.avail_act==[]: return (self.col_offset + random.randint(0, self.cols_n-1) * self.block_len, self.row_offset + random.randint(0, self.rows_n-1) * self.block_len), pygame.USEREVENT
        '''
        print("Weeeeeeeeeee",'\n\n\n\n')
        for k in A.avail_act:
            print(f'x={k[0]},y={k[1]},point={k[3]}')
            for i in range(8):
                for j in range(8):
                    buf=k[2][i*8+j]
                    if buf>-1:print('',buf,end='')
                    else:print(buf,end='')
                print()
            print()
        print('\n\n')
        '''

        x=A.avail_act[0][0]; y=A.avail_act[0][1]
        self.stepnow+=1
        return (self.col_offset + x * self.block_len, self.row_offset + y * self.block_len),pygame.USEREVENT


        #return (-1, -1), pygame.USEREVENT