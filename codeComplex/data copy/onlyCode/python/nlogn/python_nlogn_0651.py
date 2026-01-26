from bisect import bisect
n, m = map(int, input().split())
vv = sorted([int(input()) for _ in range(n)])
hh = [0] * n
rr = 0
for _ in range(m):
  one, x, _ = map(int, input().split())
  if one == 1:
    if x == 1000000000:
      rr += 1
    else:  
      ind = bisect(vv, x)
      if ind:
        hh[ind-1] += 1
r = n
s = 0
#print(*vv)
#print(*hh) 
for i, h in reversed(list(enumerate(hh))):
  s += h
  #print("~", r, s)
  r = min(r, s+i)
print(r+rr)  
    