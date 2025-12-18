'''Author- Akshit Monga'''
from sys import stdin, stdout
from collections import defaultdict
import sys
input = stdin.readline
def gen(temp,i):
    global s,k,outs
    if i==k:
        j=''
        for o in range(k):
            if temp[o]==1:
                j+=s[o]
            else:
                j+='_'
        outs.add(j)
        return
    temp[i]=1
    gen(temp,i+1)
    temp[i]=-1
    gen(temp,i+1)


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack=stack[::-1]
        print("yes")
        for i in stack:
            stdout.write(str(i+1)+" ")


n,m,k=map(int,input().split())
patterns={}
all=[]
for i in range(n):
    s=input()[:-1]
    patterns[s]=i
    all.append(s)
strs=[]
dg=Graph(n)
for i in range(m):
    s,mt=input().split()
    mt=int(mt)-1
    outs=set()
    temp=[0 for o in range(k)]
    gen(temp,0)
    if all[mt] not in outs:
        print("no")
        sys.exit()
    for i in outs:
        if i!=all[mt] and i in patterns:
            dg.addEdge(mt,patterns[i])
if dg.isCyclic():
    print("no")
else:
    dg.topologicalSort()
