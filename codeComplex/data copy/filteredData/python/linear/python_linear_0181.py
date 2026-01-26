def main(n):
    # n 作为数组长度规模，k 取 n//2（至少为 1）
    if n <= 0:
        return 0
    k = max(1, n // 2)

    # 确定性生成数据：
    # a[i] = i+1, b[i] = (i % 5) - 2  =>  周期性正负权重
    a = [i + 1 for i in range(n)]
    b = [(i % 5) - 2 for i in range(n)]

    from itertools import accumulate

    ps = list(accumulate(a))
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        ai_1 = a[i - 1]
        bi_1 = b[i - 1]
        dp[i][0] = dp[i - 1][0] + ai_1 * bi_1
        seg_sum = ps[i - 1] - (ps[i - k - 1] if i - k - 1 >= 0 else 0)
        dp0_prev = dp[max(i - k, 0)][0]
        dp[i][1] = max(
            dp[i - 1][1] + ai_1 * bi_1,
            seg_sum + dp0_prev,
        )

    ans = max(max(v) for v in dp)
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)