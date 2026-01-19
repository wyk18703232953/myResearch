n,l,r,x=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
p=1<<n
cnt=0 #no. of ways
for j in range(p):
    list1=[]
    if(j>0 and j&(j-1)!=0):
        for k in range(n):
            if(j&(1<<k)):
                list1.append(c[k])
        if(sum(list1)>=l and sum(list1)<=r and list1[-1]-list1[0]>=x):
            cnt+=1
print(cnt)