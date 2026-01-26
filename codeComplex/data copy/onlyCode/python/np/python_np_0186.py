n,ll,r,x=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
subset = []
for i in range(1,(2**n)):
  sub=[]
  for j in range(n):
    if (1<<j)&i>0:
      sub.append(l[j])
  subset.append(sub)
c=0
# print(*subset,sep="\n")
for i in subset:
  if len(i)>1:
    su=sum(i)
    if (su>=ll and su<=r) and ((max(i)-min(i))>=x):
      c+=1
print(c)