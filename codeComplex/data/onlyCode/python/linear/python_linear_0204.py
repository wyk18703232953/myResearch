n,k = map(int,input().split())
r = 0
for _ in range(n):
    h,m = map(int,input().split())
    t = 60*h+m
    if(t>r+k): 
        break
    r = t+k+1
print(r//60,r%60)