a,b=map(int,input().split())
x,y,z=map(int,input().split())

yell=2*x+y
blue=y+3*z
res=max(0,yell-a)+max(0,blue-b)

print(res)