def main(n):
    # 生成测试数据：根据规模 n 构造 totNums 和 mod
    # 这里示例：totNums = n，mod 取一个较大的质数
    totNums = n
    mod = 10**9 + 7

    def Exp(b, exp):
        if exp == 0:
            return 1
        temp = Exp(b, exp >> 1)
        temp = (temp * temp) % mod
        if exp % 2 == 1:
            temp = (temp * b) % mod
        return temp

    # 预估数组大小：原代码中是 410，这里取与 totNums 相关的安全上界
    size = totNums + 5

    # Precompute
    fact = [0] * size
    inv = [0] * size
    fact[0] = 1
    inv[0] = 1
    for i in range(1, totNums + 1):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = Exp(fact[i], mod - 2)

    dp = [[0] * size for _ in range(size)]
    choose = [[0] * size for _ in range(size)]
    for i in range(0, totNums + 1):
        for j in range(0, i + 1):
            choose[i][j] = fact[i] * inv[j] % mod * inv[i - j] % mod

    pow2 = [Exp(2, i) for i in range(size)]

    # dp
    dp[0][0] = 1
    for i in range(totNums):
        for j in range(i + 1):
            if dp[i][j] == 0:
                continue
            for k in range(1, totNums - i + 1):
                val = dp[i][j] * pow2[k - 1] % mod * choose[j + k][k] % mod
                dp[i + k + 1][j + k] = (dp[i + k + 1][j + k] + val) % mod

    ans = 0
    for i in range(0, totNums + 1):
        ans = (ans + dp[totNums + 1][i]) % mod

    # print(ans)
    pass


# 示例运行
if __name__ == "__main__":
    main(10)