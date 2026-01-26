n,m,a,b=map(int,input().split())
z=(n%m)*b
x=((n//m+1)*m-n)*a
y=min(z,x)
print(y if y>0 else 0)