import sys
n,s=map(int,input().split())
if 2*s>n*(n+1) or s<2*n-1:
  print('NO')
  sys.exit()
for i in range(n,-1,-1):
  if i==0:
    branch=1
    break
  tmp=0
  tmpn=n
  j=1
  while tmpn-i**(j-1)>=0:
    tmp+=j*(i**(j-1))
    tmpn-=i**(j-1)
    j+=1
  tmp+=j*(tmpn)
  if tmp>s:
    branch=i+1
    break
tmp=0
tmpn=n
j=1
i=branch
dic={}
while tmpn-i**(j-1)>=0:
  tmp+=j*(i**(j-1))
  dic[j]=(i**(j-1))
  tmpn-=i**(j-1)
  j+=1
tmp+=j*(tmpn)
dic[j]=tmpn
maxi=j
while tmp<s:
  for j in range(maxi,-1,-1):
    while dic[j]>1:
      if s-tmp+j<=maxi:
        dic[j]-=1
        dic[s-tmp+j]+=1
        tmp=s
      else:
        dic[j]-=1
        dic[maxi+1]=1
        tmp+=maxi+1-j
        maxi+=1
      if tmp==s:
        break
    if tmp==s:
      break
b=[]
for i in dic:
  for j in range(dic[i]):
    b.append(i)
b.sort()
print('YES')
children=[0]*n
ans=[-1]*n
curr=0
pointer=0
for i in range(1,n):
  while b[i]>b[curr]+1:
    curr+=1
  ans[i]=curr
  children[curr]+=1
  if children[curr]==branch:
    curr+=1
finans=[]
for i in range(1,n):
  finans.append(ans[i]+1)
print(' '.join(map(str,finans)))