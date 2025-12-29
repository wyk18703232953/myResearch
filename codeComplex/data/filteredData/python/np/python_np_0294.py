MOD = 10**9 + 7
MAXV = 10**5 + 5

# 预计算阶乘
fact = [1] * (MAXV + 1)
for i in range(1, MAXV + 1):
    fact[i] = fact[i - 1] * i % MOD


def bino(a, b):
    up = fact[a]
    down = pow(fact[b] * fact[a - b] % MOD, MOD - 2, MOD)
    return up * down % MOD


def find(A):
    dp = [0] * (MAXV + 2)

    # 统计每个值的出现次数
    for x in A:
        if x <= MAXV:
            dp[x] += 1

    # dp[i] = 所有值是 i 的倍数的元素个数
    for i in range(2, len(dp)):
        for j in range(2, len(dp)):
            if i * j > len(dp) - 1:
                break
            dp[i] += dp[i * j]

    # 对每个 i：2^{cnt} - 1
    for i in range(2, len(dp)):
        dp[i] = (pow(2, dp[i], MOD) - 1) % MOD

    # 容斥：去除被倍数计入的
    for i in range(len(dp) - 1, 1, -1):
        for j in range(2, len(dp)):
            if i * j >= len(dp):
                break
            dp[i] -= dp[i * j]
            dp[i] %= MOD

    ans = 0
    for i in range(2, len(dp)):
        ans += dp[i]
        ans %= MOD

    return (pow(2, len(A), MOD) - ans - 1) % MOD


def main(n: int):
    """
    n: 规模，生成长度为 n 的测试数组 A（元素在 [1, MAXV] 内）
    并返回 find(A) 的结果。
    """
    # 生成简单的测试数据：1..n（裁剪到 MAXV）
    # 若希望有重复，可自行修改生成方式
    A = [i % MAXV + 1 for i in range(n)]
    return find(A)


if __name__ == "__main__":
    # 示例：调用 main(10)，真实使用时由外部调用 main(n)
    print(main(10))