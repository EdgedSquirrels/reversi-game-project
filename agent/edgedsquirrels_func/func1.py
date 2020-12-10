import random
import pygame
import sys
#from base_agent import BaseAgent

class MyBoard:
    def __init__(self,obs,step,mycolor,myturn=1,lastboard=0):
        self.obs=obs.copy()
        self.value=0
        self.step=step
        self.mycolor=step
        self.avail_act=-1
        self.lastboard=lastboard
        #self.canput=[[[0,0] for i in range(8)] for i in range(8)]
        '''for i in range(64):
            print(obs)
            self.value+=obs[i]
            self.value*=2'''
        self.available_action(mycolor,myturn)
    def available_action(self,mycolor,myturn=1):
        if self.avail_act!=-1: return self.avail_act
        ans=[]
        for i in range(8):
            for j in range(8):
                p=self.is_available(i,j,mycolor,myturn)
                if p!=-1: ans.append(p)

        ans.sort(key=lambda i: i[3],reverse=True)
        self.avail_act=ans
        return ans
        #if exist return file
        #return sorted[[x,y,nextboard,points],...]
    def is_available(self,x,y,mycolor,myturn=1):#mycolor:1 or -1
        #if exist return file(delete)
        if self.obs=={}:return -1
        #print(self.obs)
        if self.obs[(x)+(y*8)]!=0: return -1
        ans=[]
        points=0
        obsnew=self.obs.copy()
        for i in range(-1,2):
            for j in range(-1,2):
                
                bx,by=x+i,y+j
                if 0<=bx<8 and 0<=by<8 and  self.obs[bx+by*8]==-mycolor*myturn:
                    buf=1
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
        if points==0: return -1
        return [x,y,obsnew,points]
        #return [x,y,nextboard,points]
'''
oooob=dict(enumerate([0]*64,0))
oooob[27]=1; oooob[28]=-1
oooob[35]=-1;oooob[36]=1
print(oooob)
A=MyBoard(obs=oooob,step=1,mycolor=1,myturn=1,lastboard=0)
print(A.avail_act)
'''

'''
class Findroute:
    #[[myboard1...], [myboard2...],...]
    def __init__():


    def _is_available(self, label, flip=False):
'''


