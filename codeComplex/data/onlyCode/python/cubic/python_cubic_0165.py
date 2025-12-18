import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    inf=10**9
    n=II()
    aa=LI()
    dp1=[[-1]*n for _ in range(n)]
    dp2=[[inf]*n for _ in range(n)]
    for i in range(n):
        dp1[i][i]=aa[i]
        dp2[i][i]=1
    for w in range(2,n+1):
        for l in range(n-w+1):
            r=l+w-1
            for m in range(l,r):
                if dp1[l][m]!=-1 and dp1[l][m]==dp1[m+1][r]:
                    dp1[l][r]=dp1[l][m]+1
                    dp2[l][r]=1
    for m in range(n):
        for l in range(m+1):
            for r in range(m+1,n):
                dp2[l][r]=min(dp2[l][r],dp2[l][m]+dp2[m+1][r])
    print(dp2[0][n-1])

main()