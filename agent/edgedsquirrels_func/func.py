import random
import pygame
import sys
#from base_agent import BaseAgent

def findindex(id,lst):
    for i in range(len(lst)):
        if lst[i].id==id: return i
    return None

class MyBoard:
    def __init__(self,obs,step,mycolor,myturn=1,parents=[]):#lastboard points to the previous MyBoard
        self.obs=obs.copy()
        self.id=myturn
        self.step=step
        self.mycolor=mycolor
        self.myturn=myturn
        #self.avail_act=None
        self.parents=parents
        self.children=None   #[[x,y,MyBoard,flips],...]
        self.value=-1000    #self.num[mycolor*myturn]-self.num[-mycolor*myturn]
        self.num={-1:0,1:0,0:0} #the number of pieces of chess  -1:black 1:white 0: space
        for i in range(64):
            self.id*=2
            self.id+=obs[i]
            self.num[obs[i]]+=1

    def __del__(self):
        return
        if self.children == None: return
        for k in self.children:
            kk=findindex(self.id,k.parents)
            if kk!=None:
                k.parents.pop(kk)

    def get_value(self):
        mycolor=self.mycolor
        myturn=self.myturn
        self.value=self.num[mycolor*myturn]-self.num[-mycolor*myturn]
        return self.value

    def get_children(self):
        if self.children!=None: return self.children
        ans=[]
        for i in range(8):
            for j in range(8):
                p=self.is_available(i,j)
                if p!=-1: ans.append(p)
        if ans==[]:
            ans=[[-1,-1,MyBoard(obs=self.obs,step=self.step+1,mycolor=self.mycolor,myturn=-self.myturn,parents=[self]),[]]]
        k=len(ans)-1
        for _ in range(5): #shuffle
            ans.append(ans.pop(random.randint(0, k)))
        self.children=ans
        return ans

    def is_available(self,x,y):#mycolor:1 or -1
        if self.obs=={}:return -1
        if self.obs[x+y*8]!=0: return -1
        mycolor=self.mycolor
        myturn=self.myturn
        points=myturn*mycolor
        obsnew=self.obs.copy()
        flips=[(x,y)]
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
                                flips.append((bx,by))
                                bx,by=bx+i,by+j
                            break
                        bx,by,buf=bx+i,by+j,buf+1
        if points==myturn*mycolor: return -1
        newboard=MyBoard(obs=obsnew,step=self.step+1,mycolor=self.mycolor,myturn=-self.myturn,parents=[self])
        return [x,y,newboard,flips]
        #return [x,y,nextMyboard,flips]
