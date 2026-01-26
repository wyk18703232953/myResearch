for _ in range(int(input())):
    n,k=map(int,input().split())
    if n>31:
        print("YES",n-1)
        continue
    else:
        if k>(4**n-1)//3:
            print("NO")
            continue
    l=(4**n-1)//3
    i=1
    j=0
    k1=k
    while i<=n:
        k-=(2**i-1)
        j=i
        if k<0:
            j=j-1
            k+=(2**i-1)
            break
        i+=1
    k2=k1-k
    k3=(2**(j+1)-1)*((4**(n-j)-1)//3)
    #print(j,k,k1,k2,k3,l)
    if l-k2-k3>=k:
        print("YES",n-i+1)
    else:
        print("NO") 
