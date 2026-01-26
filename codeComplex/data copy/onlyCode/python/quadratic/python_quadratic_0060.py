from collections import Counter
from math import *
import sys
mod=1000000007

def pro(arr,q):
    n=len(arr)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                ans+=1
    
    res=ans%2
    for x,y in q:
        k= y-x + 1
        k=k//2
        k=k%2
        res= k^res
        if(res):
            print('odd')
        else:
            print('even')
n=int(input())
arr=list(map(int,input().split()))
t=int(input())
que=[]
for i in range(t):
    que.append(list(map(int,input().split())))
pro(arr,que)