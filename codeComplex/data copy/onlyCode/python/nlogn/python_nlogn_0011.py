n,t=list(map(int,input().split()))
a=sorted([list(map(int,input().split())) for i in range(n)])
b=[a[i][0]-a[i][1]/2-a[i-1][0]-a[i-1][1]/2 for i in range(1,n)]
c=2
for i in range(n-1):
    c+=int(b[i]>t)*2+int(b[i]==t)
print(c)