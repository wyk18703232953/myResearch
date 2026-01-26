from sys import stdin
from bisect import bisect_right as br

from collections import deque
n,m,k=map(int,stdin.readline().strip().split())
s=deque(map(int,stdin.readline().strip().split()))
lim=k
ans=0
while len(s)!=0:
    x=br(s,lim)
    for i in range(x):
        s.popleft()
    if x!=0:
        ans+=1
        lim+=x
    else:
        if len(s)>0:
            x=s[0]-lim
            if x%k==0:
                x=x//k
            else:
                x=(x//k)+1
            lim+=x*k
        
print(ans)
