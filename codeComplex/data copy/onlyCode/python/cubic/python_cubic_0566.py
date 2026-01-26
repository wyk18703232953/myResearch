fre =[0,0,0,0,0,0,0,0,0,0,0]
a=input();b=input()
c=False
def DFS(aa,bb):
  if int(aa)==len(a):
    print(bb)
    exit()
  global c
  for i in range(9,-1,-1):
    if (fre[i]>0 and i<=int(b[int(aa)])) or (fre[i]>0 and c):
      fre[i]-=1
      if i<int(b[int(aa)]):
        c=True
      DFS(aa+1,bb*10+i)
      fre[i]+=1
      c=False
      


if len(b)>len(a):
  x=sorted(a);
  
  print(*x[::-1],sep='')
else:
  for i in a:
    fre[int(i)]+=1
  DFS(0,0)
