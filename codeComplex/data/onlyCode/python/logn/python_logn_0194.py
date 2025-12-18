import sys
import bisect
from bisect import bisect_left as lb
from bisect import bisect_right as rb
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
b=[]

def dfs2(root,par,d):
    global gp,dp
    dp[root]=d
    for child in gp[root]:
        if child==par:continue
        dfs2(child,root,d+1)
def hnbhai(tc):
    n,s=sd()
    low=s
    high=n+1
    ans=n+1
    while(low<=high):
        mid=(low+high)//2
        ss=sum(list(map(int,list(str(mid)))))
        if mid-ss<s:
            low=mid+1
        else:
            ans=mid
            high=mid-1
    print(n-ans+1)
for _ in range(1):
    hnbhai(_+1)
