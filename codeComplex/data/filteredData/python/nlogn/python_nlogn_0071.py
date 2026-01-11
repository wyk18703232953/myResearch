def main(n):
    # 映射：n 作为元素数量，k 取为 n//2（至少为 1）
    if n <= 0:
        return
    k = max(1, n // 2)

    dp = []
    for i in range(n):
        p = (i * 3 + 7) % (n + 5)
        t = (i * 5 + 11) % (n + 7)
        dp.append((p, -t))

    dp.sort(reverse=True)

    if 1 <= k <= n:
        target = dp[k - 1]
        cnt = dp.count(target)
        # print(cnt)
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)