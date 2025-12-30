def main(n):
    # 生成测试数据
    # 这里假设：
    #   - m 为 n 的一个因子（若不是则取 1，避免 m>n 或除零问题）
    #   - k 为一个与 n 相关的常数
    #   - l 为长度为 n 的整数数组，这里简单生成一个包含正负数的序列
    if n <= 0:
        return 0

    # 简单的生成策略，可按需修改
    m = max(1, n // 3)  # 让 m 约为 n/3，但至少为 1
    k = n               # 让 k 与规模 n 同阶

    l = []
    for i in range(n):
        # 让数列在 [-n, n] 中波动
        val = (i * 7 - n * 3) % (2 * n + 1) - n
        l.append(val)

    # 原逻辑
    ma = 0
    # 注意：当 m > n 时，range(n-1, n-m-1, -1) 会为空，因此先限制 m<=n
    m = min(m, n)
    for deb in range(n - 1, n - m - 1, -1):
        cumi = 0
        scu = 0
        for i in range(deb, -1, -1):
            scu += l[i]
            ma = max(ma, scu - cumi - k)
            if (deb - i + 1) % m == 0:
                scu -= k
            if scu < cumi:
                cumi = scu

    return ma


if __name__ == "__main__":
    # 可在此做简单示例调用
    # 例如：n = 10
    result = main(10)
    print(result)