from sys import stdin, stdout
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))

for _ in range(1):#nmbr()):
    r, c=lst()
    a=[input() for i in range(r)]
    pre=[[0 for i in range(c)] for i in range(r)]
    suf=[[0 for i in range(c)] for i in range(r)]
    for i in range(c):
        pre[0][i]=int(a[0][i])
        suf[r-1][i]=int(a[r-1][i])
    for i in range(1, r):
        for j in range(c):
            pre[i][j]=pre[i-1][j]+int(a[i][j])
    # print(*pre, sep='\n')
    for i in range(r-2, -1 ,-1):
        for j in range(c):
            suf[i][j]=suf[i+1][j]+int(a[i][j])
    ans='NO'
    for i in range(r):
        f=1
        for j in range(c):
            up=down=0
            if i-1>=0:up=pre[i-1][j]
            if i+1<r:down=suf[i+1][j]
            if up+down==0:
                f=0
                break
        if f:
            ans="YES"
            break
    print(ans)
