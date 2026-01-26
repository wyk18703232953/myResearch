l,r=input().split(" ")
l,r=int(l),int(r)

a,b,c=l,l+1,l+2

if (l % 2 != 0):
    a,b,c=a+1,b+1,c+1
    
if (c > r):
    print(-1)
    
else:
    print(a,b,c)