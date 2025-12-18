from collections import defaultdict
from sys import stdin
input=stdin.readline
t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  dd=defaultdict(int)
  for i in range(n):
    dd[a[i]]+=1
  l=[]
  for aa in a:
    if dd[aa]>=2:
      l.append(aa)
      dd[aa]-=2
  l.sort()
  ans=[-1,-1,-1,-1]
  m=10**18
  for i in range(len(l)-1):
    x=(4*(l[i]+l[i+1])**2)/(l[i]*l[i+1])
    if x<m:
      ans=[l[i],l[i],l[i+1],l[i+1]]
      m=x
  print(*ans)