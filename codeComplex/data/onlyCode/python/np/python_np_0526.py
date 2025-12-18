import sys

# sys.setrecursionlimit(200005)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline().rstrip()
inf = 10**16
md = 10**9+7
# md = 998244353

n, k = LI()
s = [-1 if c == "?" else ord(c)-97 for c in SI()]

def ok(m):
    nxt = [[n]*(n+1) for _ in range(k)]
    for j in range(k):
        cnt = 0
        ni = n
        nxtj = nxt[j]
        for i in range(n)[::-1]:
            if s[i] == -1 or s[i] == j: cnt += 1
            else: cnt = 0
            if cnt >= m: ni = i
            nxtj[i] = ni
    dp = [n+1]*(1 << k)
    dp[0] = 0
    for bit in range(1 << k):
        l = dp[bit]
        if l+m > n: continue
        for j in range(k):
            if bit >> j & 1: continue
            i = nxt[j][l]
            if i+m <= n:
                nbit = bit | 1 << j
                dp[nbit] = min(dp[nbit], i+m)
    return dp[-1] <= n

l, r = 0, n//k+1
while l+1 < r:
    m = (l+r)//2
    if ok(m): l = m
    else: r = m

print(l)
