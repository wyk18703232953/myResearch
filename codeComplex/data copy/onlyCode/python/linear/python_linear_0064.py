import sys

def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def rinput():   return map(int, sys.stdin.readline().strip().split()) 
def get_list(): return list(map(int, sys.stdin.readline().strip().split())) 


n,s=rinput()
maxi=s
for i in range(n):
    f,t=rinput()
    maxi=max(maxi,f+t)

print(maxi)