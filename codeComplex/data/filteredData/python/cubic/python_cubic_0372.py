class Combination:
    def __init__(self, n, MOD):
        self.f = [1]
        for i in range(1, n + 1):
            self.f.append(self.f[-1] * i % MOD)
        self.inv_f = [0] * (n + 1)
        self.inv_f[n] = pow(self.f[n], MOD - 2, MOD)
        for i in reversed(range(n)):
            self.inv_f[i] = self.inv_f[i + 1] * (i + 1) % MOD
        self.MOD = MOD

    def inv(self, k):
        """get inverse(k)"""
        return (self.inv_f[k] * self.f[k - 1]) % self.MOD

    def fact(self, k):
        """get k!"""
        return self.f[k]

    def inv_fact(self, k):
        """get inverse(k!)"""
        return self.inv_f[k]

    def perm(self, k, r):
        """get kPr"""
        if k < r:
            return 0
        return (self.f[k] * self.inv_f[k - r]) % self.MOD

    def comb(self, k, r):
        """get kCr"""
        if k < r:
            return 0
        return (self.f[k] * self.inv_f[k - r] * self.inv_f[r]) % self.MOD


def combination(k, r, MOD):
    """kCr O(r)"""
    if k < r:
        return 0
    r = min(r, k - r)
    numer, denom = 1, 1
    for l in range(r):
        numer *= (k - l)
        numer %= MOD
        denom *= l + 1
        denom %= MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


def main(n):
    # 生成测试数据：此处仅根据 n 选取一个模数
    # 若有需要可改为随机 MOD 或由外部传入
    MOD = 10 ** 9 + 7

    comb = Combination(10 ** 5, MOD)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][i] = pow(2, i - 1, MOD)

    pows = [pow(2, i, MOD) for i in range(n + 10)]

    for i in range(n + 1):
        for times in range(max(i // 2, 1), i + 1):
            for length in range(1, times + 1):
                nokori = times - length
                ptn = pows[length - 1]
                ptn *= comb.fact(times) * comb.inv_fact(nokori) * comb.inv_fact(length)
                if i - length == 1:
                    continue
                dp[i][times] += ptn * dp[i - length - 1][nokori]
                dp[i][times] %= MOD

    ans = sum(dp[-1]) % MOD
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例：调用 main(n) 进行测试
    main(10)