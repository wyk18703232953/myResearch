import sys
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def minput():   return map(int, sys.stdin.readline().strip().split()) 
def listinput(): return list(map(int, sys.stdin.readline().strip().split())) 
n=iinput()
color=['purple','green','blue','orange','red','yellow']
gem=['Power','Time','Space','Soul','Reality','Mind']
for _ in range(n):
    s=input()
    indexofcolor=color.index(s)
    color.remove(s)
    gem.pop(indexofcolor)
print(len(gem))
for i in gem:
    print(i)