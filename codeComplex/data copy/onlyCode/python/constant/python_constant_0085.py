n = int(input())
ans = 0
if n==1:
    print(1)
    exit()
if n==2:
    print(2)
    exit()
if n==3:
    print(6)
    exit()
if n%2==0:
    if n%3==0:
        ans=(n-1)*(n-2)*(n-3)
    else:
        ans=n*(n-1)*(n-3)
else:
    ans=n*(n-1)*(n-2)

print(ans)