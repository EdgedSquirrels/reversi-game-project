import random
import pygame
import sys

from agent.base_agent import BaseAgent
from agent.edgedsquirrels_func.func2 import *

#python3 arena.py --agent1 edgedsquirrels.MyAgent --agent2 base_agent.RandomAgent
class MyAgent(BaseAgent):
    #x=0,y=0
    #Route=MyRoute()
    #stepnow=0
    
    def step2(self,reward,obs):
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
        if self.color=='black': self.mycolor=-1
        else: self.mycolor=1
        self.obs=obs
        #print(self.obs)
        A=MyBoard(obs=self.obs,step=0,mycolor=self.mycolor)
        A.available_action()
        if A.avail_act==[]: return (self.col_offset + random.randint(0, self.cols_n-1) * self.block_len, self.row_offset + random.randint(0, self.rows_n-1) * self.block_len), pygame.USEREVENT
        #print("Weeeeeeeeeee",'\n\n\n\n')
        """
        for k in A.avail_act:
            print(f'x={k[0]},y={k[1]},point={k[3]}')
            for i in range(8):
                for j in range(8):
                    buf=k[2][i*8+j]
                    if buf>-1:print('',buf,end='')
                    else:print(buf,end='')
                print()
            print()
        """
        #print('\n\n')
        
        x=A.avail_act[0][0]; y=A.avail_act[0][1]
        return (self.col_offset + x * self.block_len, self.row_offset + y * self.block_len),pygame.USEREVENT


        #return (-1, -1), pygame.USEREVENT
    



    
    
    '''
    def __init__(self,obs,step,mycolor,myturn=1,lastboard=0):
        self.nextsteps=[]
    '''
    stepnow=0  #0:starting point
    stepdeveloped=0
    developdepth=3
    steps=[]
    #[[myboard1-1,myboard1-2...](step1), [myboard2-1,myboard2-2,...](step2),...]


        
    def develop(self,step,board):
        if step-self.stepnow>self.developdepth: return
        steps=self.steps
        mycolor=self.mycolor
        '''if board.avail_act:
            k=None
            if len(steps)>step-self.stepnow+1:
                k=findindex(newboard.id,steps[step-self.stepnow+1])
            if k==None:
                nowboard.avail_availabel_action()
                steps[step-self.stepnow+1].append(nowboard)
                board.children.append(newboard)
            else: newboard=steps[step-self.stepnow+1]][k]
            newboard.used=True
            continue'''
        if board.avail_act==[]:
            newboard=MyBoard(obs=board.obs,step=board.step+1,mycolor=self.mycolor,myturn=-board.myturn,parents=[board])
            k=None
            if len(steps)>step-self.stepnow+1:
                k=findindex(newboard.id,steps[step-self.stepnow+1])
                if k!=None and findindex(board.id,steps[step-self.stepnow+1][k].parents)!=None:
                    steps[step-self.stepnow+1][k].parents.append(board)
            if k==None:
                newboard.available_action()
                steps[step-self.stepnow+1].append(newboard)
                board.children.append(newboard)
                self.develop(step=step+1,board=newboard)
        else:    
            for act in board.avail_act:
                if len(self.steps)<step-self.stepnow+2: self.steps.append([])
                newboard=MyBoard(obs=act[2],step=board.step+1,mycolor=self.mycolor,myturn=-board.myturn,parents=[board])
                k=None
                if len(steps)>step-self.stepnow+1:
                    k=findindex(newboard.id,steps[step-self.stepnow+1])
                    if k!=None and findindex(board.id,steps[step-self.stepnow+1][k].parents)!=None:
                        steps[step-self.stepnow+1][k].parents.append(board)
                if k==None:
                    newboard.available_action()
                    steps[step-self.stepnow+1].append(newboard)
                    board.children.append(newboard)
                    self.develop(step=step+1,board=newboard)
                '''else: newboard=steps[step-self.stepnow+1]][k]
                newboard.used=True'''
                
    def del_unused(self):
        steps=self.steps
        for boards in steps:
            i=0
            while i<len(boards):
                if boards[i].parents==[]:
                    buf=boards.pop(i)
                    del buf
                else: i+=1
                

    def negamax(self,board,a=-1000,b=1000):  #a:worst case  b:best case
        if board.children==[]:
            return board.get_value()
        if board.value!=-1000: return board.value
        #childNodes := generateMoves(node)
        #childNodes := orderMoves(childNodes)
        board.value =-1000
        for child in board.children:
            board.value = max(board.value, -(self.negamax(board=child, a=-b, b=-a)))
            a = max(a, board.value)
            if a >= b :
                break #(* cut-off *)
        return board.value





    def step(self,reward,obs):# call this func   rewrite the step function
        if self.color=='black': self.mycolor=-1
        else: self.mycolor=1
        self.obs=obs
        #print(self.obs)
        for boards in self.steps:
            for board in boards:
                board.value=-1000
                #board.used=False
        #self.develop(obs=self.obs,step=stepnow,myturn=1)

        #insert nowboard
        print('create nowboard')
        for i in range(64):
            if not -1<=obs[i]<=1:
                print('Error')
                for i in range(8):
                    for j in range(8):
                        buf=obs[i*8+j]
                        if buf>=0:print('',buf,end='')
                        else:print(buf,end='')
                    print()
                print()
                print('\n\n')
        nowboard=MyBoard(self.obs,self.stepnow,self.mycolor)
        for _ in range(2):
            if len(self.steps)>0: self.steps.pop(0)
        k=None
        while len(self.steps)>0 and k==None:
            k=findindex(nowboard.id,self.steps[0])
            self.steps.pop(0)
        if k==None:
            nowboard.available_action()
            if len(self.steps)>0: 
                for kk in self.steps[0]: del kk
            if len(self.steps)==0: self.steps.append([])
            self.steps[0]=[nowboard]
        else:
            buf=self.steps[0].pop(k)
            for kk in self.steps[0]: del kk
            self.steps[0]=[buf]
            self.stepnow=self.steps[0][0].step
        print(self.steps)
        self.steps[0][0].parents=None
        #self.steps[0][0].used=True
        print('del unused boards')
        self.del_unused()
        #self.develop(step=self.stepnow+len(self.steps)-1,board=steps[0][0])
        
        print('develop new boards')
        for board in self.steps[len(self.steps)-1]:
            
            self.develop(step=board.step,board=board)


        #self.boarddevelop()
        x=-1;y=-1
        print('alpha-beta pruning and negamax algorithm')
        print(self.steps)
        bestv=self.negamax(board=self.steps[0][0],a=-1000,b=1000)
        for i in range(len(self.steps[0][0].children)):
            print(self.steps[0][0].children[i].value)
            if self.steps[0][0].children[i].value==-bestv:
                x=self.steps[0][0].avail_act[i][0]
                y=self.steps[0][0].avail_act[i][1]
        print(x,y,bestv,end='\n\n')
        self.stepnow+=2

        if x==-1 and y==-1: 
            print('Error',end='\n\n\n')
            return self.step2(reward,obs)

        return (self.col_offset + x * self.block_len, self.row_offset + y * self.block_len),pygame.USEREVENT

    
        