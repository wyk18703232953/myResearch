a,b=map(int,input().split())
if max(a,b)-min(a,b) +1<=2:
    print(-1)
elif max(a,b)-min(a,b) +1==3:
    if a % 2==1 and b %2==1:
        print(-1)
    else:
        print(min(a,b),min(a,b)+1,min(a,b)+2)
else:
    ans=0
    for i in range(a,b+1):
        if i%2==0:
            ans=i
            break
    print(ans,ans+1,ans+2)