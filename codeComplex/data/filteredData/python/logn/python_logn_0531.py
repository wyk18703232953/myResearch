def main(n: int):
    # 生成测试数据 k，范围设为 [1, 10^n - 1]
    if n <= 0:
        return
    max_k = 10 ** n - 1
    # 简单生成一个中间值作为测试数据
    k = max_k // 2

    s = 0
    i = 1
    # 找出 k 所在的位数区间
    while (s + i * (9 * pow(10, i - 1))) < k:
        s += i * (9 * pow(10, i - 1))
        i += 1
    else:
        i -= 1

    k = k - s - 1
    x = k // (i + 1)
    y = k % (i + 1)
    x = pow(10, i) + x
    ss = str(x)
    print(ss[y])


if __name__ == "__main__":
    # 示例：n = 5
    main(5)