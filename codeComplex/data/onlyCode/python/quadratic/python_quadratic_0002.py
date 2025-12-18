n,r=list(map(int,input().split()))
x=list(map(int,input().split()))
y=[r]*n
for i in range(1,n):
    for j in range(i):
        d=abs(x[i]-x[j])
        if d<=2*r:
            y[i]=max(y[i],y[j]+(4*r*r-d*d)**(0.5))
print(*y)