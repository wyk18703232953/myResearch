def main(n):
    # 确定性生成 n, m, arr
    # 约束：m >= 1 且 m <= n（当 n >= 1）。若 n < 2，特殊处理。
    if n <= 0:
        # 对于非正规模，视为最小可运行示例
        n = 1
    # 让 m 随 n 变化且 1 <= m <= n
    # 例如：m 为不超过 n 的奇数，且至少为 1
    m = max(1, (2 * (n // 3) + 1))
    if m > n:
        m = n

    # 生成长度为 n 的数组 arr，元素分布与 m 有关联但完全确定
    # arr[i] = (i * 2 + i // 3) % (2 * m + 1) 只是一个确定的构造
    arr = [(i * 2 + i // 3) % (2 * m + 1) for i in range(n)]

    dp = [[] for _ in range(m)]
    for i in range(n):
        dp[arr[i] % m].append(i)

    res = 0
    k = n // m
    ans = arr.copy()
    s = []
    for _ in range(2):
        for i in range(m):
            if len(dp[i]) < k:
                while len(s) != 0 and len(dp[i]) < k:
                    x = s.pop()
                    y = arr[x] % m
                    if i > y:
                        ans[x] = ans[x] + (i - y)
                        res = res + (i - y)

                    else:
                        ans[x] = ans[x] + (m - 1 - y) + (i + 1)
                        res = res + (m - 1 - y) + (i + 1)
                    dp[i].append("xxx")
            if len(dp[i]) > k:
                while len(dp[i]) > k:
                    s.append(dp[i].pop())

    # print(res)
    pass
    # print(*ans)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以做规模实验
    main(10)