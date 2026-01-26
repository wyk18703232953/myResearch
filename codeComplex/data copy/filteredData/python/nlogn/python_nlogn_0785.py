def main(n):
    # 映射：n 为数组长度，k 取为 n//2（至少为 1，且不超过 n）
    if n <= 0:
        return

    k = max(1, min(n, n // 2 if n // 2 > 0 else 1))

    # 生成确定性数据：严格递增序列，间隔为 (i % 5) + 1
    a = []
    cur = 0
    for i in range(n):
        cur += (i % 5) + 1
        a.append(cur)

    ans = a[-1] - a[0]
    delta = [-a[i] + a[i - 1] for i in range(1, n)]
    delta.sort()
    ans += sum(delta[:(k - 1)])
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)