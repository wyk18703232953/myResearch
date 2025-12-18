fast=lambda:stdin.readline().strip()
zzz=lambda:[int(i) for i in fast().split()]
z,zz=input,lambda:list(map(int,z().split()))
szz,graph,mod,szzz=lambda:sorted(zz()),{},10**9+7,lambda:sorted(zzz())
from re import *
from sys import *
from math import *
from heapq import *
from queue import *
from bisect import *
from string import *
from itertools import *
from collections import *
from math import factorial as f
from bisect import bisect as bs
from bisect import bisect_left as bsl
from collections import Counter as cc
from itertools import accumulate as ac
def lcd(xnum1,xnum2):return (xnum1*xnum2//gcd(xnum1,xnum2))
def prime(x):
    p=ceil(x**.5)+1
    for i in range(2,p):
        if (x%i==0 and x!=2) or x==0:return 0
    return 1
def dfs(u,visit,graph):
    visit[u]=1
    for i in graph[u]:
        if not visit[i]:
            dfs(i,visit,graph)
def output(answer):
    stdout.write(str(answer))
###########################---Test-Case---#################################
"""

  If you Know me , Then you probably don't know me !


"""
###########################---START-CODING---##############################

 
 
n,k=zzz()

arr1=zzz()
arr2=zzz()
ans=0

new_arr=[0]*n

for i in range(n):
    if arr2[i]==0:
        new_arr[i]=arr1[i]
    else:
        ans+=arr1[i]

total=sum(new_arr[:k])
mx=total

j=0
for i in range(k,n):
    total-=new_arr[j]
    total+=new_arr[i]
    mx=max(mx,total)
    j+=1
        
    
print(mx+ans)
    










    








        
        
       
