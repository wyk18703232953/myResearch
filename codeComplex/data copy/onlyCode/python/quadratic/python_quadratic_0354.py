import re
import sys
exit=sys.exit
from bisect import bisect_left as bsl,bisect_right as bsr
from collections import Counter,defaultdict as ddict,deque
from functools import lru_cache
cache=lru_cache(None)
from heapq import *
from itertools import *
from math import inf
from pprint import pprint as pp
enum=enumerate
ri=lambda:int(rln())
ris=lambda:list(map(int,rfs()))
rln=sys.stdin.readline
rl=lambda:rln().rstrip('\n')
rfs=lambda:rln().split()
mod=1000000007
d4=[(0,-1),(1,0),(0,1),(-1,0)]
d8=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
########################################################################

m,n=ris()
m,n=m+2,n+2
grid =['.'*n]
grid+=['.'+rl()+'.' for _ in range(m-2)]
grid+=['.'*n]

up=[[0]*n for _ in range(m)]
dw=[[0]*n for _ in range(m)]
lf=[[0]*n for _ in range(m)]
rg=[[0]*n for _ in range(m)]
rs=[[0]*n for _ in range(m)]
cs=[[0]*n for _ in range(m)]

for i in range(1,m-1):
  for j in range(1,n-1):
    if grid[i][j]=='*':
      up[i][j]=1+up[i-1][j]
      lf[i][j]=1+lf[i][j-1]
for i in range(m-1,0,-1):
  for j in range(n-1,0,-1):
    if grid[i][j]=='*':
      dw[i][j]=1+dw[i+1][j]
      rg[i][j]=1+rg[i][j+1]

ans=[]
for i in range(1,m-1):
  for j in range(1,n-1):
    if grid[i][j]=='.':
      continue
    s=min(up[i-1][j],dw[i+1][j],lf[i][j-1],rg[i][j+1])
    if s==0:
      continue
    ans.append((i,j,s))
    rs[i-s][j]+=1
    rs[i+s+1][j]-=1
    cs[i][j-s]+=1
    cs[i][j+s+1]-=1

for i in range(1,m-1):
  for j in range(1,n-1):
    rs[i][j]+=rs[i-1][j]
    cs[i][j]+=cs[i][j-1]

for i in range(1,m-1):
  for j in range(1,n-1):
    if grid[i][j]=='.':
      continue
    if rs[i][j]==0 and cs[i][j]==0:
      print(-1)
      exit()

print(len(ans))
for i,j,s in ans:
  print(i,j,s)
