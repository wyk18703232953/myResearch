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
def output(answer):stdout.write(str(answer))
###########################---Test-Case---#################################
"""

  If you think, You Know me, Then you probably don't know me !


"""
###########################---START-CODING---##############################


lst1={}
lst2={}
n=int(z())
lst=set()
for _ in range( n ):
    x,y=zzz()
    lst1[x]=y
    lst.add(x)
    
m=int(z())

for _ in range( m ):
    x,y=zzz()
    lst2[x]=y
    lst.add(x)
    
ans=0
for i in lst:
    try:
        x=lst1[i]
    except:
        x=0

    try:
        y=lst2[i]
    except:
        y=0
    ans+=max(x,y)
print(ans)
    
