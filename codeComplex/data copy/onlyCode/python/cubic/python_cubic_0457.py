class node:
    def __init__(self,l,r,u,d):
        self.u = u
        self.d = d
        self.l = l
        self.r = r
        if l == 20000001 and r ==20000001 and u == 20000001 and d == 20000001:
            self.marr = [20000001 for i in range(11)]
        else:
            self.marr = [0 for i in range(11)]
            self.marr[1] = min(l,r,u,d)
    def mo(self,st):
        return self.marr[st-1]

n,m,s = (int(i) for i in input().split())
hor = [[20000001 for i in range(m+3)] for j in range(n+2)]
ver = [[20000001 for i in range(m+2)] for j in range(n+3)]
for i in range(1,n+1):
    hor[i][2:1+m] = [int(i) for i in input().split()]
for i in range(2,1+n):
    ver[i][1:m+1] = [int(i) for i in input().split()]
if s%2 == 0 :
    nds = [[node(hor[i][j],hor[i][j+1],ver[i][j],ver[i+1][j]) for j in range(m+2)] for i in range(n+2)]
    for st in range(2,s//2+1):
        for i in range(1,n+1):
            for j in range(1,m+1):
                x = nds[i][j].marr[1]
                l = nds[i][j].l
                r = nds[i][j].r
                u = nds[i][j].u
                d = nds[i][j].d
                nds[i][j].marr[st] = min(x*st,r+nds[i][j+1].mo(st),l+nds[i][j-1].mo(st),u+nds[i-1][j].mo(st),d+nds[i+1][j].mo(st))
    ans = [[nds[i][j].marr[s//2]*2 for j in range(1,m+1)] for i in range(1,n+1)]
    for i in range(n):
        print(*tuple(ans[i]))
else :
    a = [[-1 for i in range(m)] for j in range(n)]
    for i in range(n):
        print(*tuple(a[i]))
    