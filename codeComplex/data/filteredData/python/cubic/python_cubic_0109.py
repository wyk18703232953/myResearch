MOD = 1000000007


def find(c: str) -> int:
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 26
    else:
        return ord(c) - ord('a')


def main(n: int):
    # 1. 生成测试字符串 s，长度为 n
    # 这里简单生成一个周期性重复的 52 字符串（26 小写 + 26 大写）
    base_chars = [chr(ord('a') + i) for i in range(26)] + \
                 [chr(ord('A') + i) for i in range(26)]
    s_list = []
    for i in range(n):
        s_list.append(base_chars[i % 52])
    s = ''.join(s_list)

    # 2. 预设若干询问 q 和 (x, y)
    #    这里设 q = min(n, 10)，随机选一些位置对（示例：固定规则生成）
    q = min(n, 10)
    queries = []
    for i in range(q):
        x = (i * 2) % n + 1        # 保证在 [1, n]
        y = (i * 2 + 3) % n + 1
        queries.append((x, y))

    # ========== 原逻辑开始（去除 input，使用上面生成的 s, queries） ==========
    n = len(s)
    buc = [0] * 101
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    dp = [0] * (n + 1)
    ans = [[0] * 55 for _ in range(55)]

    # 统计频率
    for ch in s:
        buc[find(ch)] += 1

    # 预处理阶乘和逆元
    fac[0] = 1
    for i in range(1, n + 1):
        fac[i] = (fac[i - 1] * i) % MOD
    inv[n] = pow(fac[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    num = pow(fac[n // 2], 2, MOD)
    for i in range(0, 52):
        num = (num * inv[buc[i]]) % MOD

    dp[0] = 1
    for i in range(0, 52):
        if not buc[i]:
            continue
        for j in range(n, buc[i] - 1, -1):
            dp[j] += dp[j - buc[i]]
            if dp[j] >= MOD:
                dp[j] -= MOD

    for i in range(52):
        ans[i][i] = dp[n // 2]

    for i in range(52):
        if not buc[i]:
            continue
        temp_dp = dp.copy()
        for k in range(buc[i], n + 1):
            temp_dp[k] -= temp_dp[k - buc[i]]
            if temp_dp[k] < 0:
                temp_dp[k] += MOD

        for j in range(i + 1, 52):
            if not buc[j]:
                continue
            for k in range(buc[j], n + 1):
                temp_dp[k] -= temp_dp[k - buc[j]]
                if temp_dp[k] < 0:
                    temp_dp[k] += MOD
            ans[i][j] = (2 * temp_dp[n // 2]) % MOD

            for k in range(n, buc[j] - 1, -1):
                temp_dp[k] += temp_dp[k - buc[j]]
                if temp_dp[k] >= MOD:
                    temp_dp[k] -= MOD

    # 处理生成的 queries，并输出结果
    for x, y in queries:
        l = find(s[x - 1])
        r = find(s[y - 1])
        if l > r:
            l, r = r, l
        print(num * ans[l][r] % MOD)


if __name__ == "__main__":
    # 示例调用：n = 20
    main(20)