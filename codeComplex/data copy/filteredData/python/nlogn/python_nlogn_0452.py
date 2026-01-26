def main(n):
    MAXN = 200001

    # 映射 n 到输入规模：
    # 令数组长度为 n，m 为数组中值域中间的一个确定性值
    length = n if n > 0 else 1
    m = 0

    # 构造确定性的数组 s，元素分布在 [-k, k]，包含大于、小于、等于 m 的情况
    # 为保持与原算法兼容，数值范围控制在 [-10^5, 10^5] 以内
    k = 100000
    s = [((i * 37) % (2 * k + 1)) - k for i in range(length)]

    f = [0 for _ in range(length + 1)]
    count = [0 for _ in range(-MAXN, MAXN + 1)]

    f[0] = 0
    last = 0
    res = 0

    for i in range(1, length + 1):
        if s[i - 1] == m:
            for j in range(last, i):
                count[f[j]] += 1
            last = i

        if s[i - 1] > m:
            f[i] = f[i - 1] - 1

        else:
            f[i] = f[i - 1] + 1

        res += count[f[i]] + count[f[i] - 1]

    # print(res)
    pass
if __name__ == "__main__":
    main(10)