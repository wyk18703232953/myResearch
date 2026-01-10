def main(n):
    from itertools import accumulate
    import bisect

    # 定义规模含义：
    # n 为数组 A 的长度
    # 令 q = n，K 的长度与 A 相同，便于规模分析
    q = n

    # 构造确定性数据
    # A 为从 1 到 n 的递增序列
    A = [i + 1 for i in range(n)]
    # K 为从 1 到 n 的递增序列
    K = [i + 1 for i in range(q)]

    C = [0] + A
    C = list(accumulate(C))
    total = 0
    ans = [0] * q

    for i, k in enumerate(K):
        total += k
        j = bisect.bisect_right(C, total)
        if j != n + 1:
            ans[i] = n - (j - 1)
        else:
            ans[i] = n
            total = 0

    print(*ans, sep="\n")


if __name__ == "__main__":
    main(10)