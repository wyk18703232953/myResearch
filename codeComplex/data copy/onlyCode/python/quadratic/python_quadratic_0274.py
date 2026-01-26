import sys
import math
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def minput():   return map(int, sys.stdin.readline().strip().split()) 
def listinput(): return list(map(int, sys.stdin.readline().strip().split())) 
n,m=minput()
x=listinput()
y=listinput()
xx=set(x)
yy=set(y)
common=xx.intersection(yy)
for i in x:
    if i in common:
        print(i,end=' ')