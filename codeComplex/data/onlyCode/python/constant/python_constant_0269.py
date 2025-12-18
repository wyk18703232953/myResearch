from sys import stdin, stdout
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))
for _ in range(1):#nmbr()):
    n, cur, l, r=lst()
    if l==1 and r==n:
        print(0)
    elif l==1 and r!=n:
        print(abs(r-cur)+1)
    elif r==n and l!=1:
        print(abs(cur-l)+1)
    else:
        disa=abs(l-cur)
        disb=abs(r-cur)
        ans=min(disa, disb) + (r-l) +2
        print(ans)

