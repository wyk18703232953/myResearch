n,m=map(int,input().split())
count=[0]*n
a=list(map(int,input().split()))
for i in range(m):
    count[a[i]-1]+=1
print(min(count))