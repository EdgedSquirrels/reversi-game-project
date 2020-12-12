import random
import pygame
import sys
#from base_agent import BaseAgent

def findindex(id,lst):
    for i in range(len(lst)):
        if lst[i].id==id: return i
    return None

class MyBoard:
    def __init__(self,obs,step,mycolor,myturn=1,parents=[]): #lastboard points to the previous MyBoard
        self.obs=obs.copy()
        self.id=myturn
        self.step=step
        self.mycolor=mycolor
        self.myturn=myturn
        self.avail_act=None
        self.parents=parents
        self.children=[]
        self.value=-1000    #self.num[mycolor*myturn]-self.num[-mycolor*myturn]
        self.used=False
        self.num={-1:0,1:0,0:0} #the number of pieces of chess  -1:black 1:white 0: space
        #self.canput=[[[0,0] for i in range(8)] for i in range(8)]
        for i in range(64):
            #print(obs)
            self.id*=2
            self.id+=obs[i]
            self.num[obs[i]]+=1
        #self.available_action(mycolor,myturn)
    def __del__(self):
        for k in self.children:
            kk=findindex(self.id,k.parents)
            if kk!=None:
                k.parents.pop(kk)
                #if k.parents==[]: del k
    def get_value(self):
        mycolor=self.mycolor
        myturn=self.myturn
        self.value=self.num[mycolor*myturn]-self.num[-mycolor*myturn]
        return self.value
    def available_action(self):
        if self.avail_act!=None: return self.avail_act
        ans=[]
        for i in range(8):
            for j in range(8):
                p=self.is_available(i,j)
                if p!=-1: ans.append(p)

        ans.sort(key=lambda i: abs(i[3]),reverse=True)
        self.avail_act=ans
        return ans
        #if exist return file
        #return sorted[[x,y,nextboardobs,points],...]
    def is_available(self,x,y):#mycolor:1 or -1
        #if exist return file(delete)
        if self.obs=={}:return -1
        #print(self.obs)
        if self.obs[(x)+(y*8)]!=0: return -1
        mycolor=self.mycolor
        myturn=self.myturn
        ans=[]
        points=myturn
        obsnew=self.obs.copy()
        for i in range(-1,2):
            for j in range(-1,2):
                
                bx,by=x+i,y+j
                if 0<=bx<8 and 0<=by<8 and  self.obs[bx+by*8]==-mycolor*myturn:
                    buf=0
                    while (0<=bx<8 and 0<=by<8 and self.obs[bx+by*8]!=0):
                        if self.obs[bx+by*8]==mycolor*myturn:
                            points+=buf*myturn
                            obsnew[x+y*8]=mycolor*myturn
                            bx,by=x+i,y+j
                            while(self.obs[bx+by*8]!=mycolor*myturn):
                                obsnew[bx+by*8]=mycolor*myturn
                                bx,by=bx+i,by+j
                            break
                        bx,by,buf=bx+i,by+j,buf+1
        if points==myturn: return -1
        return [x,y,obsnew,points]
        #return [x,y,nextboardobs,points]



'''
#debug
oooob=dict(enumerate([0]*64,0))
oooob[27]=1; oooob[28]=-1
oooob[35]=-1;oooob[36]=-1
oooob[43]=1;
print(oooob)
A=MyBoard(obs=oooob,step=1,mycolor=1,myturn=1)
A.available_action()
for k in A.avail_act:
    print(f'x={k[0]},y={k[1]},point={k[3]}')
    for i in range(8):
        for j in range(8):
            buf=k[2][i*8+j]
            if buf>-1: print('',end=' ')
            print(buf,end='')
        print()
    print('\n')
'''



'''
class MyRoute:
    #[[myboard1-1,myboard1-2...](step1), [myboard2-1,myboard2-2,...](step2),...]
    """
    def __init__(self,obs,step,mycolor,myturn=1,lastboard=0):
        self.nextsteps=[]
    """
    stepnow=0
    stepfind=0
    steps=[]

    def findvalue(self,obs):
    
        
    def develop(self,obs,myturn=1,)  #if can't move step+=2



    def findbeststep(self,obs,mycolor,step):# call this func
        self.mycolor=
        for boards in self.steps:
            for board in boards:
                board.value=0
        self.develop(obs,1,)
'''      



