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
def dfs2(root,par):
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
vis=[]
tot=0
def dfs(root):
    global tot,vis,gp
    for child in gp[root]:
        if vis[child]==0:
            tot+=1
            vis[child]=1
            dfs(child)
pre=[[] for i in range(3)]
def hnbhai(tc):
    n=sb()
    d,num=0,1
    while num<=n:
        num+=9*(d+1)*(10**d)
        d+=1
    num-=9*(d)*(10**(d-1))
    ans=str(10**(d-1)+(n-num)//d)
    print(ans[(n-num)%d])
for _ in range(1):
    hnbhai(_+1)
