n,m = map(int,input().split())

if m<=n:
    print((m-1)//2)
elif m>n:
    if (m-n) in range(1,n+1):
        if(n-(m-n))%2==0:
            print((n-(m-n))//2)
        else:
            print((n-(m-n))//2+1)
    else:
        print(0)