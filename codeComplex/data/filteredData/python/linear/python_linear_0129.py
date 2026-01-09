def bitcnt(X):
    res = 0
    v = X
    while v:
        res += v & 1
        v >>= 1
    return res


class Combi:

    def __init__(self, N, mod=10**9 + 7):
        self.power = [1 for _ in range(N + 1)]
        self.rev = [1 for _ in range(N + 1)]
        self.mod = mod
        for i in range(2, N + 1):
            self.power[i] = (self.power[i - 1] * i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod - 2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j - 1] = (self.rev[j] * j) % self.mod

    def com(self, K, R):
        if not (0 <= R <= K):
            return 0

        else:
            return (self.power[K] * self.rev[K - R] * self.rev[R]) % self.mod

    def perm(self, K, R):
        if not (0 <= R <= K):
            return 0

        else:
            return (self.power[K] * self.rev[K - R]) % self.mod


def main(n):
    MOD = 10**9 + 7
    max_n = 1000
    if n < 1:
        n = 1
    if n > max_n:
        n = max_n
    c = Combi(10000)

    # Generate deterministic NL and K from n
    # NL: binary digits (reversed) of an n-bit pattern derived from n
    NL = []
    for i in range(n):
        NL.append((i ^ n) & 1)
    N = len(NL)
    if N == 0:
        NL = [0]
        N = 1
    K = (n % 15)

    dp = [[0] * 1020 for _ in range(1020)]

    dp[0][0] = 1
    for pos, bit in enumerate(NL):
        if bit == 1:
            for bit_idx in range(1010):
                dp[pos + 1][bit_idx] = (dp[pos][bit_idx - 1] + c.com(pos, bit_idx)) % MOD
            continue

        else:
            for bit_idx in range(1010):
                dp[pos + 1][bit_idx] = dp[pos][bit_idx]
            continue

    INF = 1 << 60
    cnt = [INF] * 1010

    cnt[1] = 0

    for i in range(2, 1010):
        cnt[i] = 1 + cnt[bitcnt(i)]

    if K == 0:
        result = dp[N][0]

    else:
        ans = 0
        for bc in range(1010):
            if cnt[bc] == K - 1:
                ans += dp[N][bc]
        if K == 1:
            ans -= 1
        result = ans % MOD

    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(1000)