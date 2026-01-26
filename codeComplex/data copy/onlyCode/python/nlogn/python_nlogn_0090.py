n,a,b = map(int,input().split())
c = []
c = list(map(int,input().split()))
c.sort()
l = c[b-1]
r = 0
ok = False
for i in range (b,n-a+1):
  if c[i] > l:
    ok = True 
    r = c[i]
    break
if ok == True: print(r-l) 
else: print(0) 