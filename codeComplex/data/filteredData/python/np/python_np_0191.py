def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设：
    #   - 题目中 d 的元素为 [1, 2, ..., n]
    #   - l, r, x 随 n 设定为:
    #       l = n          （最小总和）
    #       r = n * (n+1)//2  （所有元素之和）
    #       x = n // 2     （最小差值）
    #
    # 如需其它规则，可在此修改生成逻辑。

    d = list(range(1, n + 1))
    l = n
    r = n * (n + 1) // 2
    x = n // 2

    ans = 0
    # 遍历所有非空子集（0 表示空集，不计）
    for i in range(1, 1 << n):
        # 直接用位运算枚举子集，无需把 i 转为二进制字符串
        subset = []
        diff_sum = 0
        for j in range(n):
            if (i >> j) & 1:
                diff_sum += d[j]
                subset.append(d[j])

        if not subset:
            continue

        subset.sort()
        if l <= diff_sum <= r and subset[-1] - subset[0] >= x:
            ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(4)