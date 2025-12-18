n=int(input())
arr=list(map(int,input().split()))
dic={}
for val in arr:
  if val not in dic:
    dic[val]=1
  else:
    dic[val]+=1
flag1=True
if 0 in dic:
  if dic[0]>=2:
    flag1=False
cnt=0
for val in dic.keys():
  if dic[val]>=3:
    flag1=False
    break
  if dic[val]==2:
    cnt+=1
    if val-1 in dic:
      flag1=False
      break
if cnt>=2:
  flag1=False
if flag1==False:
  print('cslnb')
else:
  flag2=(n*(n-1)//2+sum(arr))%2
  if flag2==1:
    print('sjfnb')
  else:
    print('cslnb')