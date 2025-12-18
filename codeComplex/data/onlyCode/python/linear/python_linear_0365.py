n,m=map(int,input().split())
c=list(map(int,input().split()))
a=list(map(int,input().split()))
j,res=0,0
for i in range(n):
    if j < m:
        if c[i] <= a[j]:
            j+=1
            res+=1
print(res)