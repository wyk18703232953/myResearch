import sys
input = sys.stdin.readline
from itertools import combinations
from collections import defaultdict
n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
mx = max(max(a[i]) for i in range(n))
if n == 1:
  print(1,1)
  exit()
l = 0
r = mx+1
while l+1 < r:
  flg = 0
  x = (l+r)//2
  jud = set()
  dc = defaultdict(int)
  for i in range(n):
    jnum = 0
    for j in range(m):
      if a[i][j] >= x:
        jnum += 1<<j
    if dc[jnum] == 0:
      dc[jnum] = i+1
    if jnum == (1<<m)-1:
      flg = 1
      if i == 0:
        ans = (i+1,i+2)
      else:
        ans = (1,i+1)
    jud.add(jnum)
  for p,q in combinations(jud,2):
    if p|q == (1<<m)-1:
      flg = 1
      ans = (dc[p],dc[q])
  if flg:
    l = x
  else:
    r = x
if l == 0:
  print(1,2)
else:
  print(*ans)