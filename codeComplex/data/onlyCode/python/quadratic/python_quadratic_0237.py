import bisect
n=int(input())
s=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=10**18
for mid in range(1,n-1):
  l1=[c[i] for i in range(mid) if s[i]<s[mid]]+[10**18]
  l2=[c[i] for i in range(mid+1,n) if s[i]>s[mid]]+[10**18]
  ans=min(ans,min(l1)+c[mid]+min(l2))
if ans>=10**18:
  print(-1)
else:
  print(ans)