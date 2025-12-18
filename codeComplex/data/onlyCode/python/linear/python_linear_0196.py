n,a,b,c,T=map(int,input().split())
arr=list(map(int,input().split()))
Tcnt=arr.count(T);l=n-Tcnt;ans=0;a1=0
for i in range(1,T):
  for j in range(n):
    if arr[j]<=i:a1+=1
 # print(a1)
  ans+=a1*c;a1=0  
b1=0
#print(ans)
#print(ans)
for i in range(n):
  b1=a-((T-arr[i])*b)#;print(b1)
  if b1<=0:ans+=b1;
  else:ans+=b1
ans1=n*a
print(max(ans,ans1))

