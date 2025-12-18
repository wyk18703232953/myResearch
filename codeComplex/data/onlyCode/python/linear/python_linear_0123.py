# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:12:13 2020

@author: lenovo
"""

from collections import defaultdict
from collections import deque

class graph:
    def __init__(self):
        self.g=defaultdict(list)
    def addedge(self,u,v):
        self.g[u].append(v)
def router(values):
    gr=graph()
    for i in range(len(values)):
        gr.addedge(values[i], i+2)
    return gr.g

def isleaf(node,gr):
    if len(gr[node])==0:
        return True
    return False

def christmas(gr,start,visited):
    q=deque()
    q.append(start)
    visited[start]=True
    count=0
    while q:
        count=0
        value=q.popleft()
        for val in gr[value]:
            if not isleaf(val,gr):
                q.append(val)
                visited[val]=True
            else:
                visited[val]=True
                count=count+1
        if count<3:
            return 'No'
    if count<3:
        return 'No'
    return 'Yes'
n=int(input())
values=[]
for i in range(n-1):
    value=int(input())
    values.append(value)
gr=router(values)
visited=[False]*(n+1)
print(christmas(gr, 1, visited))
    