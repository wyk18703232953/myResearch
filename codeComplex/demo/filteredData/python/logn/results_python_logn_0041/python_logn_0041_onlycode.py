l,r=tuple(map(int,input().split(" ")))
x=l^r
pow=1
while(pow<=x) :
    pow*=2
    
print(pow-1)