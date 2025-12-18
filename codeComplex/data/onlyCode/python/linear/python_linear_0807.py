n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
arr+=[0]*m
ans=0
pos=0
while arr[pos]!=0:
  page=(arr[pos]-pos-1)//k
  tmp=1
  for i in range(1,k):
    if pos+i>=2*m-1:
      break
    if (arr[pos+i]-pos-1)//k==page:
      tmp+=1
    else:
      break
  pos+=tmp
  ans+=1
print(ans)