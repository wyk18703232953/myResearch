for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=int(0)
    while a and b:
        a,b=min(a,b),max(a,b)
        ans,b=ans+b//a,b%a
    print(ans)
