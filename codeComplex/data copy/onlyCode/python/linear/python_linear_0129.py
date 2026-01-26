class Combi():

    def __init__(self, N, mod=10**9 + 7):
        self.power = [1 for _ in range(N+1)]
        self.rev = [1 for _ in range(N+1)]
        self.mod = mod
        for i in range(2, N+1):
            self.power[i] = (self.power[i-1]*i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod-2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j-1] = (self.rev[j]*j) % self.mod

    def com(self, K, R):
        if not (0 <= R <= K):
            return 0
        else:
            return ((self.power[K])*(self.rev[K-R])*(self.rev[R])) % self.mod

    def perm(self, K, R):
        if not (0 <= R <= K):
            return 0
        else:
            return (self.power[K])*(self.rev[K-R]) % self.mod


def bitcnt(X):
    res = 0
    v = X
    while v:
        res += v & 1
        v >>= 1
    return res


c = Combi(10000)
NL = list(map(int, list(input())))[::-1]
N = len(NL)
K = int(input())
MOD = 10**9 + 7

dp = [[0]*(1020) for i in range(1020)]

dp[0][0] = 1
for pos, bit in enumerate(NL):
    if bit == 1:
        for bit in range(1010):
            dp[pos + 1][bit] = (dp[pos][bit - 1] + c.com(pos, bit)) % MOD
        continue
    else:
        for bit in range(1010):
            dp[pos + 1][bit] = dp[pos][bit]
        continue

INF = 1 << 60
cnt = [INF]*(1010)

cnt[1] = 0
MOD = 10**9 + 7

for i in range(2, 1010):
    cnt[i] = 1 + cnt[bitcnt(i)]

if K == 0:
    print(dp[N][0])
    exit()
else:
    ans = 0
    for bitcnt in range(1010):
        if cnt[bitcnt] == K - 1:
            ans += dp[N][bitcnt]
    if K == 1:
        ans -= 1
    print(ans % MOD)
    exit()
