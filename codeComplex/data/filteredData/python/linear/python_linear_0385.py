def main(n):
    # 这里根据规模 n 生成测试数据
    # 原程序读取 n, m 和接下来 m 行的 (x, d)
    # 我们固定 m = n，且构造一组简单的测试数据：
    # 第 i 行为 x = i, d = (-1)**i * i
    m = n

    # 计算 posf 和 negf（与原代码一致）
    posf = (n * (n - 1)) // 2
    if n % 2 != 0:
        negf = (n // 2) * (n // 2 + 1)

    else:
        negf = (n // 2) * (n // 2 - 1) + n // 2

    ans = 0
    for i in range(m):
        x = i + 1
        d = (-1) ** (i + 1) * (i + 1)  # 偶数行正，奇数行负
        ans += n * x
        if d >= 0:
            ans += posf * d

        else:
            ans += negf * d

    # print(ans / n)
    pass
if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(5)