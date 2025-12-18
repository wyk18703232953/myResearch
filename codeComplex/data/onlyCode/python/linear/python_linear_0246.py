n,k=list(map(int,input().split()))

if k%2==0:
    s="."
    s=s+"#"*(k//2)
    s=s+"."*(n-len(s))
    print("YES")
    print("."*n)
    print(s)
    print(s)
    print("."*n)

else:
    if k<=n-2:
        a="#"*k
        s="."*((n-k)//2)+a+"."*((n-k)//2)
        print("YES")
        print("."*n)
        print(s)
        print("."*n)
        print("."*n)
    else:
        k=k-n+3
        a="#"*k
        s="."*((n-k)//2)+a+"."*((n-k)//2)
        print("YES")
        print("."*n)
        print("."+"#"*(n-2)+".")
        s=list(s)
        s[n//2]="."
        s="".join(s)
        print(s)
        print("."*n)