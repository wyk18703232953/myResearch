import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

rn,gn,bn=MI()
rr=LI()
gg=LI()
bb=LI()
rr.sort(reverse=True)
gg.sort(reverse=True)
bb.sort(reverse=True)
dp=[[[-1]*(bn+1) for _ in range(gn+1)] for _ in range(rn+1)]
dp[0][0][0]=0
ans=0
for i in range(rn+1):
    for j in range(gn+1):
        for k in range(bn+1):
            pre=dp[i][j][k]
            if pre==-1:continue
            ans=max(ans,pre)
            if i<rn and j<gn:dp[i+1][j+1][k]=max(dp[i+1][j+1][k],pre+rr[i]*gg[j])
            if i<rn and k<bn:dp[i+1][j][k+1]=max(dp[i+1][j][k+1],pre+rr[i]*bb[k])
            if j<gn and k<bn:dp[i][j+1][k+1]=max(dp[i][j+1][k+1],pre+gg[j]*bb[k])

print(ans)
