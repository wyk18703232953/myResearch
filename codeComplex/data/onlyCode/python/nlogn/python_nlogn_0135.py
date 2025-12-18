n,m,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a = a[::-1]
if m<=k:
    print(0)
else:
    c=0
    while(c<n):
        k = k+a[c]-1
        c+=1
        if k>=m:
            print(c)
            exit()
    else:
        print(-1)
        