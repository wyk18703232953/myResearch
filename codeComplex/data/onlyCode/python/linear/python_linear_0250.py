n,k=map(int,input().split())
s=[["."]*n for i in range(4)]
if k%2==0:
  for j in range(1,n-1):
    if k==0:
      break
    s[1][j]="#"
    s[2][j]="#"
    k-=2
else:
  cen=n//2
  s[1][cen]="#"
  k-=1
  for i in range(1,3):
    for j in range(1,cen):
      if k>0:
        k-=2
        s[i][j]=s[i][-j-1]="#"
if k==0:
  print("YES")
  for i in range(4):
    print("".join(s[i]))
else:
  print("NO")