a=int(input())
b=list(map(int,input().split()))
z=max(b)
if z==1:b[b.index(z)]=2
else:b[b.index(z)]=1
print(*sorted(b))