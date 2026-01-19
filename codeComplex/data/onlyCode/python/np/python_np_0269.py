import sys
import bisect
from bisect import bisect_left as lb
input_=lambda: sys.stdin.readline().strip("\r\n")
from math import log
from math import gcd
from math import atan2,acos
from random import randint
sa=lambda :input_()
sb=lambda:int(input_())
sc=lambda:input_().split()
sd=lambda:list(map(int,input_().split()))
sflo=lambda:list(map(float,input_().split()))
se=lambda:float(input_())
sf=lambda:list(input_())
flsh=lambda: sys.stdout.flush()
#sys.setrecursionlimit(10**6)
mod=10**9+7
mod1=998244353
gp=[]
cost=[]
dp=[]
mx=[]
ans1=[]
ans2=[]
special=[]
specnode=[]
a=0
kthpar=[]
def dfs(root,par):
    if par!=-1:
        dp[root]=dp[par]+1
    for i in range(1,20):
        if kthpar[root][i-1]!=-1:
            kthpar[root][i]=kthpar[kthpar[root][i-1]][i-1]
    for child in gp[root]:
        if child==par:continue
        kthpar[child][0]=root
        dfs(child,root)
ans=0
def setting(s):
    if s=='0':
        return -1
    i=len(s)-1
    cc=0
    while(i>=0 and s[i]=='0'):
        cc+=1
        i-=1
    return cc
def hnbhai(tc):
    n,q=sd()
    up=n+1
    x=len(bin(n)[2:])-1
    for i in range(q):
        v=sb()
        s=sa()
        for j in s:
            temp=bin(v)[2:]
            abe=setting(temp)
            #print(v,abe)
            if j=="U":
                if abe>=x:
                    continue
                p=v+(1<<(abe))
                n=v-(1<<(abe))
                x1=setting(bin(p)[2:])
                #print(p,x1)
                x2=setting(bin(n)[2:])
                if x1==abe+1:
                    v=p
                else:
                    v=n
            elif j=="L":
                if abe<=0:
                    continue
                v=v-(1<<(abe-1))
                #print("v",v)
            else:
                if abe<=0:
                    continue
                v=v+(1<<(abe-1))
        print(v)
for _ in range(1):
    hnbhai(_+1)
