def bit_count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans


def solve(n_str, k):
    n = n_str
    x = len(n)
    if n == '1':
        return int(k == 0)
    if not k:
        return 1
    mod = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[bit_count(i)] + 1
    dp1 = [[0] * (x + 1) for _ in range(x + 1)]
    for i in range(x + 1):
        dp1[i][0] = 1
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            dp1[i][j] = (dp1[i - 1][j - 1] + dp1[i - 1][j]) % mod
    ans = 0
    cou = n.count('1')
    for i in range(1, x + 1):
        if dp[i] != k:
            continue
        se = i
        for j in range(x):
            if n[j] == '0':
                continue
            ans = (ans + dp1[x - 1 - j][se] - (se == 1 and k == 1)) % mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans + 1) % mod
    return ans


def main(n):
    # n 作为规模参数：生成长度为 n 的二进制字符串和对应的 k
    # 生成确定性的 n_str：从 1 到 n 的奇偶性构造
    n_str = ''.join('1' if i % 2 == 0 else '0' for i in range(1, n + 1))
    # k 也由 n 确定性生成，映射到一个较小范围
    if n <= 1:
        k = 0

    else:
        # k 在 [0, max(1, bit_count(n))] 范围内循环
        max_k = max(1, bit_count(n))
        k = (n % (max_k + 1))
    result = solve(n_str, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)