n,k=map(int,input().split())
s=input();flag=True;lenn=10**10;ans=0
for i in range(n):
  s1=s+s[n-i-1:]*(k-1);cnt=0
  for i in range(len(s1)-len(s)+1):
     if s1[i:i+len(s)]==s:cnt+=1
  if cnt==k and len(s1)<lenn:ans=s1;lenn=len(s1)
print(ans)
