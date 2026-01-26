l,r = map(int,input().split())

x = 64
while x>=0 and  (l&(1<<x)) == (r&(1<<x)):
    x-=1
print((1<<(x+1))-1)