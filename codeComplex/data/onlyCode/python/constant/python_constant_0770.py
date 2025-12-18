def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]

n,k=MI()

b=-(2*n+3)
c=n*n+n-2*k
x=(-b-((b*b-4*c)**0.5))//2
y=(-b+((b*b-4*c)**0.5))//2
x,y=int(x),int(y)
for i in [x-1,x,x+1,y-1,y,y+1]:
    if i**2+b*i+c==0 and 0<=i<=n-1:
        print(i)
        break