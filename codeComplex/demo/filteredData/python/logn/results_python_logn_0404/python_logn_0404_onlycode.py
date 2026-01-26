t=int(input())
for _ in range(t):
  n,k=map(int,input().split())
  if n==2 and k==3:
    print('NO')
    continue
  if n<=100:
    curr=0
    for j in range(n):
      curr+=pow(4,j)
    if curr<k:
      print('NO')
      continue
  curr=0
  ans=0
  while curr<k and ans<n:
    ans+=1
    curr+=pow(2,ans)-1
  if curr>k:
    ans-=1
  print('YES',n-ans)