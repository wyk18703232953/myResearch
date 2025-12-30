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


def bitcnt(X):
    res = 0
    v = X
    while v:
        res += v & 1
        v >>= 1
    return res


def main(n):
    """
    n: 规模参数
    这里根据 n 生成测试数据：
      - 构造一个长度为 L 的二进制串 N_str（表示一个大整数），L = min(n, 1000)
      - 构造 K = min( max(1, n // 10), 20 )

    你可以根据需要修改测试数据生成方式。
    """
    MOD = 10**9 + 7

    # ---------- 生成测试数据 ----------
    # 构造一个长度为 L 的二进制串，保证首位为 '1' 以避免前导零
    L = min(max(1, n), 1000)
    import random
    random.seed(1)
    bits = ['1'] + [random.choice(['0', '1']) for _ in range(L - 1)]
    N_str = ''.join(bits)

    # K 的构造：随规模变化的一个小整数
    K = min(max(0, n // 10), 20)

    # ---------- 原逻辑开始（用生成的 N_str, K） ----------
    c = Combi(10000)
    NL = list(map(int, list(N_str)))[::-1]
    N = len(NL)

    dp = [[0] * 1020 for _ in range(1020)]

    dp[0][0] = 1
    for pos, bit in enumerate(NL):
        if bit == 1:
            for b in range(1010):
                # 注意：原代码中 dp[pos][bit - 1] 当 bit=0 会索引到 -1，按原意应保护边界
                if b - 1 >= 0:
                    dp[pos + 1][b] = (dp[pos][b - 1] + c.com(pos, b)) % MOD
                else:
                    dp[pos + 1][b] = c.com(pos, b) % MOD
        else:
            for b in range(1010):
                dp[pos + 1][b] = dp[pos][b]

    INF = 1 << 60
    cnt = [INF] * 1010

    cnt[1] = 0

    for i in range(2, 1010):
        cnt[i] = 1 + cnt[bitcnt(i)]

    if K == 0:
        ans = dp[N][0] % MOD
        print(ans)
        return ans
    else:
        ans = 0
        for bc in range(1010):
            if cnt[bc] == K - 1:
                ans += dp[N][bc]
        if K == 1:
            ans -= 1
        ans %= MOD
        print(ans)
        return ans


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(100)