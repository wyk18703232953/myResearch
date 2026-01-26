n,m=map(int,input().split())
a=list(map(int,input().split()))
dic={}
for i in range(m):
  if a[i] in dic:
    dic[a[i]]+=1
  else:
    dic[a[i]]=1
for i in range(1,102):
  r=0
  for j in dic:
    r+=dic[j]//i
  if r<n:
    print(i-1)
    break