n,K=map(int,input().split())
b=sorted([int(x)for x in input().split()])
l=cur=0
for i in range(1,n):
    if b[i]==b[i-1]:continue
    if b[i]>b[i-1]+K:l=i
    else:cur+=(i-l);l=i
print(n-cur)
