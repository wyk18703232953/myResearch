import sys

sys.setrecursionlimit(10**5)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.buffer.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
inf = 10**16
# md = 10**9+7
# md = 998244353

n, md = LI()

def nHr(hn, hr):
    return nCr(hn+hr-1, hr-1)

def nPr(com_n, com_r):
    if com_r < 0: return 0
    if com_n < com_r: return 0
    return fac[com_n]*ifac[com_n-com_r]%md

def nCr(com_n, com_r):
    if com_r < 0: return 0
    if com_n < com_r: return 0
    return fac[com_n]*ifac[com_r]%md*ifac[com_n-com_r]%md

n_max = 405
fac = [1]
for i in range(1, n_max+1): fac.append(fac[-1]*i%md)
ifac = [1]*(n_max+1)
ifac[n_max] = pow(fac[n_max], md-2, md)
for i in range(n_max-1, 1, -1): ifac[i] = ifac[i+1]*(i+1)%md
pw = [1]
for i in range(400): pw.append(pw[-1]*2%md)

# dp[i][j]...iにj個目の白を置いたときの場合の数
dp = [[0]*(n//2+2) for _ in range(n+2)]
dp[0][0] = 1
for i in range(1, n+2):
    for j in range(1, n//2+2):
        v = 0
        for k in range(i-2, -1, -1):
            v += dp[k][j-1]*pw[i-k-2]*nCr(i-j, i-k-1)%md
        dp[i][j] = v%md
# p2D(dp)

ans = sum(dp[-1])%md
print(ans)
